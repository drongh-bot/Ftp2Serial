from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QByteArray


class SerialCommunicationError(Exception):
    """当串口通信出现问题时抛出。"""
    pass


class SerialCommunication:
    def __init__(self):
        self.serial = QSerialPort()

    def open_serial_port(self, port, baud_rate):
        ports = [port_info.portName()
                 for port_info in QSerialPortInfo.availablePorts()]
        if port not in ports:
            raise SerialCommunicationError(f"串口 {port} 没找到。")

        self.serial.setPortName(port)
        self.serial.setBaudRate(baud_rate)

        if not self.serial.open(QSerialPort.ReadWrite):
            raise SerialCommunicationError("打开串口失败。")

    def send(self, text):
        try:
            message = QByteArray.fromHex(text.encode('utf-8'))
            message.prepend(b'\x02')
            message.append(b'\x03')
            self.serial.write(message)
            self.__wait_for_acknowledgment()
        except Exception as e:
            raise SerialCommunicationError(f"{e}") from e

    def __wait_for_acknowledgment(self):
        if not self.serial.waitForBytesWritten(1000):
            raise SerialCommunicationError("数据写入超时，发送不成功。")
        if self.serial.bytesToWrite() > 0:
            raise SerialCommunicationError("数据未完全写入，发送不成功。")
        if not self.serial.waitForReadyRead(1000):
            raise SerialCommunicationError("等待响应超时，发送不成功。")
        response = self.serial.read(1)
        if response == b'':
            raise SerialCommunicationError("应该返回 06H，结果无响应，发送不成功。")
        elif response != b'\x06':
            raise SerialCommunicationError(
                f"应该返回 06H，结果是 {response.hex().upper()}，发送不成功。")

    def close_serial_port(self):
        self.serial.close()
