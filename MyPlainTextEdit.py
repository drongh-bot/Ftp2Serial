from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtCore import Signal, Qt


class MyPlainTextEdit(QPlainTextEdit):
    enterPressed = Signal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:

            self.enterPressed.emit()
        else:
            super().keyPressEvent(event)
