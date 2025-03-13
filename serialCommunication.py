import logging
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QByteArray

# 配置日志记录
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class SerialCommunicationError(Exception):
    '''当串口通信出现问题时抛出。'''
    pass


class SerialCommunication:
    def __init__(self):
        self.serial = QSerialPort()

    def openSerialport(self, port: str, baud_rate: int) -> None:
        ports = [port_info.portName()
                 for port_info in QSerialPortInfo.availablePorts()]
        if port not in ports:
            raise SerialCommunicationError(f'串口 {port} 没找到。')

        self.serial.setPortName(port)
        self.serial.setBaudRate(baud_rate)

        if not self.serial.open(QSerialPort.ReadWrite):
            raise SerialCommunicationError('打开串口失败。')
        logging.info(f'串口 {port} 已打开，波特率为 {baud_rate}。')

    def send(self, text: str) -> None:
        try:
            message = QByteArray(text.encode('utf-8'))
            message.prepend(b'\x02')
            message.append(b'\x03')
            self.serial.write(message)
            self.__wait_for_acknowledgment()
            logging.info(f'发送数据成功：{text}')
        except (ValueError, SerialCommunicationError) as e:
            logging.error(f'发送数据时出错：{e}')
            raise SerialCommunicationError(f'发送数据时出错：{e}') from e
        except Exception as e:
            logging.error(f'未知错误：{e}')
            raise SerialCommunicationError(f'未知错误：{e}') from e

    def __wait_for_acknowledgment(self) -> None:
        if not self.serial.waitForBytesWritten(1000):
            raise SerialCommunicationError('数据写入超时，发送不成功。')
        if self.serial.bytesToWrite() > 0:
            raise SerialCommunicationError('数据未完全写入，发送不成功。')
        if not self.serial.waitForReadyRead(1000):
            raise SerialCommunicationError('等待响应超时，发送不成功。')
        response = self.serial.read(1)
        if response == b'':
            raise SerialCommunicationError('应该返回 06H，结果无响应，发送不成功。')
        elif response != b'\x06':
            raise SerialCommunicationError(
                f'应该返回 06H，结果是 {response.hex().upper()}，发送不成功。')

    def close_serial_port(self) -> None:
        if self.serial.isOpen():
            self.serial.close()
            logging.info('串口已关闭。')
