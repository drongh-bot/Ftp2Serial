import logging
import sys
from datetime import date
from ftplib import FTP

from PySide6.QtCore import Qt, Slot, QSettings
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

from ftp2Serial_ui import Ui_Ftp2Serial
from serialCommunication import SerialCommunication, SerialCommunicationError


# 配置日志记录
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Form(QDialog, Ui_Ftp2Serial):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(480, 360)
        self.setWindowFlags(Qt.Window)
        self.settings = QSettings("Rogers", "Ftp2SerialPort")
        self.plainTextEdit0.setReadOnly(True)

        self.buttonReadData.clicked.connect(self.readData)
        self.buttonSendData.clicked.connect(self.sendData)
        self.buttonSavePara.clicked.connect(self.saveSettings)
        self.restoreSettings()

    @Slot()
    def readData(self):
        ftpServer = self.lineEditFtp0.text().strip()
        username = self.lineEditFtp1.text().strip()
        password = self.lineEditFtp2.text().strip()
        remoteFilePath = self.lineEditFtp3.text().strip()

        text = ''
        try:
            with FTP(ftpServer) as ftp:
                ftp.login(username, password)
                content = bytearray()

                def callback(data):
                    content.extend(data)

                ftp.retrbinary('RETR ' + remoteFilePath, callback)
                text = content.decode('utf-8').strip()
        except Exception as e:
            logging.error(f'FTP 错误: {e}')
            QMessageBox.warning(self, 'FTP 错误', str(e))
            return
        self.plainTextEdit0.setPlainText(self.__format_string(text.strip()))

    @Slot()
    def sendData(self):
        text = self.plainTextEdit0.toPlainText()
        if text == '':
            QMessageBox.warning(self, '发送文本错误', '无发送文本。')
            return
        port = self.comboBoxSerial0.currentText()
        baudrate = int(self.comboBoxSerial1.currentText())

        serialComm = None
        try:
            serialComm = SerialCommunication()
            serialComm.openSerialport(port, baudrate)
            serialComm.send(text)
        except SerialCommunicationError as e:
            logging.error(f'串口{port}错误: {e}')
            QMessageBox.warning(self, f'串口{port}错误', str(e))
        except Exception as e:
            logging.error(f'串口{port}一般错误: {e}')
            QMessageBox.warning(self, f'串口{port}一般错误', str(e))
        finally:
            if serialComm:
                serialComm.close_serial_port()
        self.plainTextEdit0.clear()

    def __format_string(self, text):
        parts = text.split('|')
        current_date = self.__format_date_english(date.today())
        formatted_str = 'ROG|'
        for i, part in enumerate(parts):
            formatted_str += part.strip() + '|'
            if i == 1:
                formatted_str += current_date + '|'
        formatted_str += '%%%'
        return formatted_str

    def __format_date_english(self, dateValue):
        month_mapping = {
            1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR',
            5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG',
            9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'
        }
        eng_month = month_mapping[dateValue.month]
        day = dateValue.day
        year_two_digits = str(dateValue.year)[-2:]
        return f'{day}{eng_month}{year_two_digits}'.upper()

    @Slot()
    def closeEvent(self, event):
        self.saveSettings()
        event.accept()

    @Slot()
    def saveSettings(self):
        self.settings.setValue('lineEditFtp0/text', self.lineEditFtp0.text())
        self.settings.setValue('lineEditFtp1/text', self.lineEditFtp1.text())
        self.settings.setValue('lineEditFtp2/text', self.lineEditFtp2.text())
        self.settings.setValue('lineEditFtp3/text', self.lineEditFtp3.text())
        self.settings.setValue(
            'comboBoxSerial0/currentIndex', self.comboBoxSerial0.currentIndex())
        self.settings.setValue(
            'comboBoxSerial1/currentIndex', self.comboBoxSerial1.currentIndex())

    @Slot()
    def restoreSettings(self):
        text0 = self.settings.value(
            'lineEditFtp0/text', defaultValue='', type=str)
        text1 = self.settings.value(
            'lineEditFtp1/text', defaultValue='', type=str)
        text2 = self.settings.value(
            'lineEditFtp2/text', defaultValue='', type=str)
        text3 = self.settings.value(
            'lineEditFtp3/text', defaultValue='', type=str)
        index0 = self.settings.value(
            'comboBoxSerial0/currentIndex', defaultValue=0, type=int)
        index1 = self.settings.value(
            'comboBoxSerial1/currentIndex', defaultValue=0, type=int)
        self.lineEditFtp0.setText(text0)
        self.lineEditFtp1.setText(text1)
        self.lineEditFtp2.setText(text2)
        self.lineEditFtp3.setText(text3)
        self.comboBoxSerial0.setCurrentIndex(index0)
        self.comboBoxSerial1.setCurrentIndex(index1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec())
