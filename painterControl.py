import csv
import json
import logging
import sys
from collections import namedtuple
from datetime import datetime, date
from ftplib import FTP

from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QDialog, QTableWidgetItem, QHeaderView, QMessageBox

from painter_ui import Ui_Dialog
from serialCommunication import SerialCommunication, SerialCommunicationError

# 配置日志记录
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 定义 namedtuple
SerialConfig = namedtuple('SerialConfig', ['port', 'baud_rate', 'use_port'])


class Painter(QDialog, Ui_Dialog):
    CLEAR_COMMAND = ('10 31 10 32 10 33 10 34 10 35 10 36 10 37 10 38 10 39 10 3A'
                     '10 3B 10 3C 10 3D 10 3E 10 3F 10 40 10 41 10 42 10 43 10 44'
                     '10 45 10 46 10 47 10 48 10 49 10 4A 10 4B 10 4C 10 4D 10 4E'
                     '10 4F')

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1200, 600)
        self.setWindowFlags(Qt.Window)

        self.inputs = [self.lineEdit1, self.lineEdit2, self.lineEdit3,
                       self.lineEdit4, self.lineEdit5, self.lineEdit6]
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 动态生成CSV文件名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        csv_filename = f'output_{timestamp}.csv'
        self.csv_file = open(csv_filename, mode='w',
                             newline='', encoding='utf-8-sig')
        self.csv_writer = csv.writer(self.csv_file)

        # 获取表头并写入CSV文件
        headers = [self.tableWidget.horizontalHeaderItem(
            i).text() for i in range(self.tableWidget.columnCount())]
        self.csv_writer.writerow(headers)

        # 设置定时器每秒更新一次时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 每秒更新一次

        self.pushButton1.clicked.connect(self.get_data)
        self.pushButton2.clicked.connect(self.send_data)
        self.pushButton3.clicked.connect(self.save_settings)
        self.plainTextEdit3.enterPressed.connect(
            self.plainTextEdit3_enterPressed)
        self.plainTextEdit4.enterPressed.connect(
            self.plainTextEdit4_enterPressed)
        self.plainTextEdit6.textChanged.connect(
            self.plainTextEdit6_textChanged)
        self.lineEdit3.textChanged.connect(self.check_content)
        self.lineEdit4.textChanged.connect(self.check_content)
        self.lineEdit5.textChanged.connect(self.check_content)

        self.load_settings()

    @Slot()
    def get_data(self):
        ftp_server = self.lineEditFtp1.text().strip()
        username = self.lineEditFtp2.text().strip()
        password = self.lineEditFtp3.text().strip()
        remote_file_path = self.lineEditFtp4.text().strip()

        text = ''
        try:
            with FTP(ftp_server) as ftp:
                ftp.login(username, password)
                content = bytearray()

                def callback(data):
                    content.extend(data)

                ftp.retrbinary('RETR ' + remote_file_path, callback)
                text = content.decode('utf-8').strip()
        except Exception as e:
            logging.error(f'FTP 错误: {e}')
            QMessageBox.warning(self, 'FTP 错误', str(e))
            return
        self.plainTextEdit5.setPlainText(text)
        self.plainTextEdit6.setPlainText(Painter.format_string(text))

    @Slot()
    def check_content(self):
        text3 = self.lineEdit3.text().strip()
        text4 = self.lineEdit4.text().strip()
        text5 = self.lineEdit5.text().strip()
        result_status = ''
        if '' in (text3, text4, text5):
            result_status = ''
        elif text3 == text4 == text5:
            result_status = 'OK'
        else:
            result_status = 'NG'
        self.lineEdit6.setText(result_status)
        self.lineEdit6.setStyleSheet(
            'QLineEdit {background-color:red}'
            if result_status == 'NG' else 'QLineEdit {background-color:white}')

    @Slot()
    def plainTextEdit3_enterPressed(self):
        trimmed_text = self.plainTextEdit3.toPlainText().strip()
        text = trimmed_text[-8:].strip() if trimmed_text else ''
        self.lineEdit3.setText(text)
        self.plainTextEdit4.setFocus()

    @Slot()
    def plainTextEdit4_enterPressed(self):
        trimmed_text = self.plainTextEdit4.toPlainText().strip()
        text = Painter.extract_substring(trimmed_text, 'LOT', 8)
        self.lineEdit4.setText(text)
        self.get_data()

    @Slot()
    def plainTextEdit6_textChanged(self):
        trimmed_text = self.plainTextEdit6.toPlainText().strip()
        text = Painter.extract_substring(trimmed_text, 'LR', 9)
        self.lineEdit5.setText(text)

    @staticmethod
    def extract_substring(original_text, marker_text, length):
        '''
        从原始字符串中提取子字符串。
        :param original_text: 原始字符串
        :param start_marker: 待查找的字符串
        :param length: 返回字符串的长度
        :return: 提取的子字符串
        '''
        result_text = ''
        if original_text:
            index = original_text.find(marker_text)
            if index != -1:
                start_index = index + len(marker_text)
                result_text = original_text[start_index:start_index + length].strip()
        return result_text

    @Slot()
    def update_time(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.lineEdit1.setText(current_time)

    @Slot()
    def send_data(self):
        '''
        发送数据到串口。根据用户界面的设置，向两个不同的串口发送指定的文本数据。
        如果核对状态为 'NG'，则只发送清空命令；如果核对状态为 'OK'，则发送清空命令后跟随文本数据。
        '''
        check_status = self.lineEdit6.text().strip()
        if not check_status:
            QMessageBox.warning(self, '核对错误', '核对没完成，不进行任何操作。')
            return

        if check_status == 'NG':
            QMessageBox.warning(self, '核对错误', f'核对结果为 {check_status}，仅清空喷码。')

        serial1_config = SerialConfig(
            self.comboBoxSerial1.currentText().strip(),
            int(self.comboBoxSerial2.currentText().strip()),
            True
        )

        serial2_config = SerialConfig(
            self.comboBoxSerial3.currentText().strip(),
            int(self.comboBoxSerial4.currentText().strip()),
            self.checkBox.isChecked()
        )

        text = Painter.insert_control_characters(
            self.plainTextEdit6.toPlainText().strip())

        serial1_status = self._operate_serial_port(
            serial1_config, Painter.CLEAR_COMMAND, text, check_status)
        serial2_status = self._operate_serial_port(
            serial2_config, Painter.CLEAR_COMMAND, text, check_status)

        self.add_row(serial1_status, serial2_status)
        self._clear_inputs()

    def _clear_inputs(self):
        '''
        清空输入框内容。
        '''
        self.plainTextEdit3.clear()
        self.plainTextEdit4.clear()
        self.plainTextEdit5.clear()
        self.plainTextEdit6.clear()

    def _operate_serial_port(self, config, clear_command, text_to_send, check_status):
        '''
        根据提供的配置，操作指定的串口。发送清空命令，如果核对状态为 'OK'，则发送额外的文本数据。

        :param config: SerialConfig namedtuple，包含串口配置信息。
        :param clear_command: 清空命令字符串。
        :param text_to_send: 需要发送的文本数据。
        :param check_status: 核对状态，决定是否发送text_to_send。
        :return: 串口操作状态，'Good' 表示成功，'' 表示未使用串口，'Bad' 表示操作失败。
        '''
        serial_comm = None
        if not config.use_port:
            return ''
        status = 'Bad'
        try:
            serial_comm = SerialCommunication()
            serial_comm.open_serial_port(config.port, config.baud_rate)
            serial_comm.send(clear_command)
            if check_status == 'OK':
                serial_comm.send(text_to_send)
            status = 'Good'
        except SerialCommunicationError as e:
            logging.error(f'串口{config.port}错误: {e}')
            QMessageBox.warning(self, f'串口{config.port}错误', str(e))
        except Exception as e:
            logging.error(f'串口{config.port}一般错误: {e}')
            QMessageBox.warning(self, f'串口{config.port}一般错误', str(e))
        finally:
            if serial_comm:
                serial_comm.close_serial_port()
        return status

    @staticmethod
    def insert_control_characters(text):
        control_number = 49
        char_count_since_last_insert = 0
        control_char = '10' + format(control_number, 'x')
        result = control_char

        for char in text:
            if char == '|':
                control_number += 1
                control_char = '10' + format(control_number, 'x')
                result += format(ord(' '), 'x') + control_char
                char_count_since_last_insert = 0
            elif char_count_since_last_insert == 10:
                control_number += 1
                control_char = '10' + format(control_number, 'x')
                result += control_char + format(ord(char), 'x')
                char_count_since_last_insert = 0
            else:
                result += format(ord(char), 'x')
                char_count_since_last_insert += 1
        return result

    def add_row(self, serial1_status, serial2_status):
        row_data = [input_field.text() for input_field in self.inputs]
        row_data.extend([serial1_status, serial2_status])

        # 在表格的第一行插入新数据
        self.tableWidget.insertRow(0)
        for i, text in enumerate(row_data):
            item = QTableWidgetItem(text)
            if item.text() in ['Bad', 'NG']:
                item.setBackground(QColor('red'))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(0, i, item)

        # 将数据写入CSV文件
        self.csv_writer.writerow(row_data)

    @Slot()
    def closeEvent(self, event):
        # 关闭应用时，关闭CSV文件
        self.csv_file.close()
        event.accept()

    @staticmethod
    def format_string(text):
        parts = text.split('|')
        current_date = Painter.format_date_english(date.today())
        formatted_str = 'ROG|'
        for i, part in enumerate(parts):
            formatted_str += part.strip() + '|'
            if i == 1:
                formatted_str += current_date + '|'
        formatted_str += '%%%'
        return formatted_str

    @staticmethod
    def format_date_english(date_value):
        month_mapping = {
            1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR',
            5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG',
            9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'
        }
        eng_month = month_mapping[date_value.month]
        day = date_value.day
        year_two_digits = str(date_value.year)[-2:]
        return f'{day}{eng_month}{year_two_digits}'.upper()

    @Slot()
    def save_settings(self):
        settings = {
            'comboBoxSerial1': self.comboBoxSerial1.currentText().strip(),
            'comboBoxSerial2': self.comboBoxSerial2.currentText().strip(),
            'comboBoxSerial3': self.comboBoxSerial3.currentText().strip(),
            'comboBoxSerial4': self.comboBoxSerial4.currentText().strip(),
            'checkBox': self.checkBox.isChecked(),
            'lineEditFtp1': self.lineEditFtp1.text().strip(),
            'lineEditFtp2': self.lineEditFtp2.text().strip(),
            'lineEditFtp3': self.lineEditFtp3.text().strip(),
            'lineEditFtp4': self.lineEditFtp4.text().strip(),
            'lineEdit2': self.lineEdit2.text().strip(),

        }
        # 将设置保存到JSON文件
        with open('settings.json', 'w', encoding='utf-8') as file:
            json.dump(settings, file, ensure_ascii=False, indent=4)

    def load_settings(self):
        try:
            # 从JSON文件中读取设置
            with open('settings.json', 'r', encoding='utf-8') as file:
                settings = json.load(file)
            # 将设置应用到控件
            self.comboBoxSerial1.setCurrentText(
                settings.get('comboBoxSerial1', ''))
            self.comboBoxSerial2.setCurrentText(
                settings.get('comboBoxSerial2', ''))
            self.comboBoxSerial3.setCurrentText(
                settings.get('comboBoxSerial3', ''))
            self.comboBoxSerial4.setCurrentText(
                settings.get('comboBoxSerial4', ''))
            self.checkBox.setChecked(settings.get('checkBox', False))
            self.lineEditFtp1.setText(settings.get('lineEditFtp1', ''))
            self.lineEditFtp2.setText(settings.get('lineEditFtp2', ''))
            self.lineEditFtp3.setText(settings.get('lineEditFtp3', ''))
            self.lineEditFtp4.setText(settings.get('lineEditFtp4', ''))
            self.lineEdit2.setText(settings.get('lineEdit2', ''))
        except FileNotFoundError:
            logging.error('配置文件没找到。')
            QMessageBox.warning(self, '其它错误', '配置文件没找到。')
        except json.JSONDecodeError:
            logging.error('错误的编码文件。')
            QMessageBox.warning(self, '其它错误', '错误的编码文件。')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Painter()
    window.show()
    sys.exit(app.exec())
