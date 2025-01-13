# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'painter.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from MyPlainTextEdit import MyPlainTextEdit
import image_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1236, 508)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.tab1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(3, -1, 3, -1)
        self.label_9 = QLabel(self.tab1)
        self.label_9.setObjectName(u"label_9")
#if QT_CONFIG(statustip)
        self.label_9.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label_9.setText(u"LOT \u6570\u636e")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)

        self.label_11 = QLabel(self.tab1)
        self.label_11.setObjectName(u"label_11")
#if QT_CONFIG(statustip)
        self.label_11.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label_11.setText(u"\u55b7\u7801 LOT \u6570\u636e")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 4, 1, 1)

        self.plainTextEdit5 = QPlainTextEdit(self.tab1)
        self.plainTextEdit5.setObjectName(u"plainTextEdit5")
        self.plainTextEdit5.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(statustip)
        self.plainTextEdit5.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.plainTextEdit5.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.plainTextEdit5.setReadOnly(True)

        self.gridLayout.addWidget(self.plainTextEdit5, 1, 4, 1, 1)

        self.plainTextEdit3 = MyPlainTextEdit(self.tab1)
        self.plainTextEdit3.setObjectName(u"plainTextEdit3")
        self.plainTextEdit3.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
#if QT_CONFIG(statustip)
        self.plainTextEdit3.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.plainTextEdit3.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.plainTextEdit3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.plainTextEdit3.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout.addWidget(self.plainTextEdit3, 1, 2, 1, 1)

        self.lineEdit2 = QLineEdit(self.tab1)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lineEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit2, 4, 1, 1, 1)

        self.label_8 = QLabel(self.tab1)
        self.label_8.setObjectName(u"label_8")
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label_8.setText(u"\u7ebf\u540d")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.lineEdit4 = QLineEdit(self.tab1)
        self.lineEdit4.setObjectName(u"lineEdit4")
        self.lineEdit4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit4.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit4, 4, 3, 1, 1)

        self.tableWidget = QTableWidget(self.tab1)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(u"\u65e5\u671f");
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setText(u"\u7ebf\u540d");
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"LOT \u7eb8");
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setText(u"MS LOT");
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setText(u"\u55b7\u7801 LOT");
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setText(u"\u6838\u5bf9\u7ed3\u679c");
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setText(u"\u901a\u8baf\u72b6\u6001\u4e00");
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
#if QT_CONFIG(statustip)
        self.tableWidget.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 6, 0, 1, 6)

        self.plainTextEdit4 = MyPlainTextEdit(self.tab1)
        self.plainTextEdit4.setObjectName(u"plainTextEdit4")
        self.plainTextEdit4.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
#if QT_CONFIG(statustip)
        self.plainTextEdit4.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.plainTextEdit4.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.plainTextEdit4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.plainTextEdit4, 1, 3, 1, 1)

        self.label_5 = QLabel(self.tab1)
        self.label_5.setObjectName(u"label_5")
#if QT_CONFIG(statustip)
        self.label_5.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(u"LOT \u7eb8\u539f\u59cb\u6570\u636e")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.lineEdit6 = QLineEdit(self.tab1)
        self.lineEdit6.setObjectName(u"lineEdit6")
        self.lineEdit6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit6.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit6, 4, 5, 1, 1)

        self.lineEdit3 = QLineEdit(self.tab1)
        self.lineEdit3.setObjectName(u"lineEdit3")
        self.lineEdit3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit3.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit3, 4, 2, 1, 1)

        self.label_7 = QLabel(self.tab1)
        self.label_7.setObjectName(u"label_7")
#if QT_CONFIG(statustip)
        self.label_7.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label_7.setText(u"\u65f6\u95f4")
        self.label_7.setTextFormat(Qt.TextFormat.AutoText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.line_4 = QFrame(self.tab1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 5, 0, 1, 6)

        self.label_10 = QLabel(self.tab1)
        self.label_10.setObjectName(u"label_10")
#if QT_CONFIG(statustip)
        self.label_10.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label_10.setText(u"MS \u6807\u7b7e LOT \u6570\u636e")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)

        self.label = QLabel(self.tab1)
        self.label.setObjectName(u"label")
#if QT_CONFIG(statustip)
        self.label.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label.setText(u"\u6700\u7ec8\u55b7\u7801\u4fe1\u606f")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)

        self.plainTextEdit6 = QPlainTextEdit(self.tab1)
        self.plainTextEdit6.setObjectName(u"plainTextEdit6")
        self.plainTextEdit6.setMaximumSize(QSize(16777215, 80))
        self.plainTextEdit6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(statustip)
        self.plainTextEdit6.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.plainTextEdit6.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.plainTextEdit6.setFrameShape(QFrame.Shape.StyledPanel)
        self.plainTextEdit6.setFrameShadow(QFrame.Shadow.Sunken)
        self.plainTextEdit6.setReadOnly(True)
        self.plainTextEdit6.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.plainTextEdit6, 1, 5, 1, 1)

        self.lineEdit5 = QLineEdit(self.tab1)
        self.lineEdit5.setObjectName(u"lineEdit5")
        self.lineEdit5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit5.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit5, 4, 4, 1, 1)

        self.lineEdit1 = QLineEdit(self.tab1)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit1.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit1, 4, 0, 1, 1)

        self.label_4 = QLabel(self.tab1)
        self.label_4.setObjectName(u"label_4")
#if QT_CONFIG(statustip)
        self.label_4.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(u"MS \u6807\u7b7e\u539f\u59cb\u6570\u636e")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_12 = QLabel(self.tab1)
        self.label_12.setObjectName(u"label_12")
#if QT_CONFIG(statustip)
        self.label_12.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.label_12.setText(u"\u6838\u5bf9\u7ed3\u679c")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 3, 5, 1, 1)

        self.line_2 = QFrame(self.tab1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 6)

        self.label_3 = QLabel(self.tab1)
        self.label_3.setObjectName(u"label_3")
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(u"\u55b7\u7801\u4fe1\u606f\u539f\u59cb\u6570\u636e")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.label_17 = QLabel(self.tab1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(350, 75))
        self.label_17.setPixmap(QPixmap(u":/images/image.jpg"))
        self.label_17.setScaledContents(True)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.line = QFrame(self.tab1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton1 = QPushButton(self.tab1)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setMinimumSize(QSize(0, 50))
        self.pushButton1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(statustip)
        self.pushButton1.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton1.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.pushButton1.setText(u"\u83b7\u53d6\u6570\u636e")

        self.verticalLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton(self.tab1)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setMinimumSize(QSize(0, 50))
        self.pushButton2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(statustip)
        self.pushButton2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton2.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.pushButton2.setText(u"\u53d1\u9001\u6570\u636e")

        self.verticalLayout.addWidget(self.pushButton2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab1, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), u"\u6570\u636e\u8bb0\u5f55")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.groupBox_2 = QGroupBox(self.tab2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(150, 0))
        self.groupBox_2.setMaximumSize(QSize(150, 16777215))
#if QT_CONFIG(statustip)
        self.groupBox_2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.groupBox_2.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.groupBox_2.setTitle(u"\u55b7\u7801\u673a\u4e00\u8bbe\u7f6e")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
#if QT_CONFIG(statustip)
        self.label_2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(u"\u4e32\u53e3\u53f7")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBoxSerial1 = QComboBox(self.groupBox_2)
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.addItem("")
        self.comboBoxSerial1.setObjectName(u"comboBoxSerial1")
        self.comboBoxSerial1.setMinimumSize(QSize(80, 0))
        self.comboBoxSerial1.setMaximumSize(QSize(80, 16777215))
#if QT_CONFIG(statustip)
        self.comboBoxSerial1.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBoxSerial1.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.comboBoxSerial1.setCurrentText(u"COM1")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxSerial1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
#if QT_CONFIG(statustip)
        self.label_6.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(u"\u6ce2\u7279\u7387")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBoxSerial2 = QComboBox(self.groupBox_2)
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.addItem("")
        self.comboBoxSerial2.setObjectName(u"comboBoxSerial2")
        self.comboBoxSerial2.setMinimumSize(QSize(80, 0))
        self.comboBoxSerial2.setMaximumSize(QSize(80, 16777215))
#if QT_CONFIG(statustip)
        self.comboBoxSerial2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBoxSerial2.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.comboBoxSerial2.setCurrentText(u"9600")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxSerial2)

        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.horizontalSpacer_3)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer_2)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(150, 0))
        self.groupBox_3.setMaximumSize(QSize(150, 16777215))
        self.formLayout_4 = QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
#if QT_CONFIG(statustip)
        self.label_18.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_18.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_18.setText(u"\u4e32\u53e3\u53f7")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.comboBoxSerial3 = QComboBox(self.groupBox_3)
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.addItem("")
        self.comboBoxSerial3.setObjectName(u"comboBoxSerial3")
        self.comboBoxSerial3.setMinimumSize(QSize(80, 0))
        self.comboBoxSerial3.setMaximumSize(QSize(80, 16777215))
#if QT_CONFIG(statustip)
        self.comboBoxSerial3.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBoxSerial3.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.comboBoxSerial3.setCurrentText(u"COM1")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.comboBoxSerial3)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
#if QT_CONFIG(statustip)
        self.label_19.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_19.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_19.setText(u"\u6ce2\u7279\u7387")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.comboBoxSerial4 = QComboBox(self.groupBox_3)
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.addItem("")
        self.comboBoxSerial4.setObjectName(u"comboBoxSerial4")
        self.comboBoxSerial4.setMinimumSize(QSize(80, 0))
        self.comboBoxSerial4.setMaximumSize(QSize(80, 16777215))
#if QT_CONFIG(statustip)
        self.comboBoxSerial4.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBoxSerial4.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.comboBoxSerial4.setCurrentText(u"9600")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.comboBoxSerial4)

        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(50, 0))
        self.checkBox.setMaximumSize(QSize(50, 16777215))

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.checkBox)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout_4.setItem(2, QFormLayout.FieldRole, self.horizontalSpacer)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.tab2)
        self.groupBox.setObjectName(u"groupBox")
#if QT_CONFIG(statustip)
        self.groupBox.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.groupBox.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle(u"FTP \u8bbe\u7f6e")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
#if QT_CONFIG(statustip)
        self.label_13.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_13.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText(u"\u5730\u5740")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.lineEditFtp1 = QLineEdit(self.groupBox)
        self.lineEditFtp1.setObjectName(u"lineEditFtp1")
        sizePolicy.setHeightForWidth(self.lineEditFtp1.sizePolicy().hasHeightForWidth())
        self.lineEditFtp1.setSizePolicy(sizePolicy)
        self.lineEditFtp1.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
#if QT_CONFIG(statustip)
        self.lineEditFtp1.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEditFtp1.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.lineEditFtp1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEditFtp1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
#if QT_CONFIG(statustip)
        self.label_14.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_14.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText(u"\u7528\u6237\u540d")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.lineEditFtp2 = QLineEdit(self.groupBox)
        self.lineEditFtp2.setObjectName(u"lineEditFtp2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditFtp2.sizePolicy().hasHeightForWidth())
        self.lineEditFtp2.setSizePolicy(sizePolicy1)
        self.lineEditFtp2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
#if QT_CONFIG(statustip)
        self.lineEditFtp2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEditFtp2.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.lineEditFtp2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEditFtp2)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
#if QT_CONFIG(statustip)
        self.label_15.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_15.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_15.setText(u"\u5bc6\u7801")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.lineEditFtp3 = QLineEdit(self.groupBox)
        self.lineEditFtp3.setObjectName(u"lineEditFtp3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditFtp3.sizePolicy().hasHeightForWidth())
        self.lineEditFtp3.setSizePolicy(sizePolicy2)
        self.lineEditFtp3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
#if QT_CONFIG(statustip)
        self.lineEditFtp3.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEditFtp3.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.lineEditFtp3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEditFtp3)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
#if QT_CONFIG(statustip)
        self.label_16.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_16.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_16.setText(u"\u8def\u5f84")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.lineEditFtp4 = QLineEdit(self.groupBox)
        self.lineEditFtp4.setObjectName(u"lineEditFtp4")
        sizePolicy2.setHeightForWidth(self.lineEditFtp4.sizePolicy().hasHeightForWidth())
        self.lineEditFtp4.setSizePolicy(sizePolicy2)
        self.lineEditFtp4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
#if QT_CONFIG(statustip)
        self.lineEditFtp4.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEditFtp4.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.lineEditFtp4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEditFtp4)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton3 = QPushButton(self.tab2)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setMinimumSize(QSize(0, 50))
        self.pushButton3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(statustip)
        self.pushButton3.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton3.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.pushButton3.setText(u"\u4fdd\u5b58\u53c2\u6570")

        self.verticalLayout_2.addWidget(self.pushButton3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), u"\u8bbe\u7f6e")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)
        self.comboBoxSerial1.setCurrentIndex(0)
        self.comboBoxSerial2.setCurrentIndex(2)
        self.comboBoxSerial3.setCurrentIndex(0)
        self.comboBoxSerial4.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u55b7\u7801", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u901a\u8baf\u72b6\u6001\u4e8c", None));
        self.label_17.setText("")
        self.comboBoxSerial1.setItemText(0, QCoreApplication.translate("Dialog", u"COM1", None))
        self.comboBoxSerial1.setItemText(1, QCoreApplication.translate("Dialog", u"COM2", None))
        self.comboBoxSerial1.setItemText(2, QCoreApplication.translate("Dialog", u"COM3", None))
        self.comboBoxSerial1.setItemText(3, QCoreApplication.translate("Dialog", u"COM4", None))
        self.comboBoxSerial1.setItemText(4, QCoreApplication.translate("Dialog", u"COM5", None))
        self.comboBoxSerial1.setItemText(5, QCoreApplication.translate("Dialog", u"COM6", None))
        self.comboBoxSerial1.setItemText(6, QCoreApplication.translate("Dialog", u"COM7", None))
        self.comboBoxSerial1.setItemText(7, QCoreApplication.translate("Dialog", u"COM8", None))
        self.comboBoxSerial1.setItemText(8, QCoreApplication.translate("Dialog", u"COM9", None))
        self.comboBoxSerial1.setItemText(9, QCoreApplication.translate("Dialog", u"COM10", None))

        self.comboBoxSerial2.setItemText(0, QCoreApplication.translate("Dialog", u"2400", None))
        self.comboBoxSerial2.setItemText(1, QCoreApplication.translate("Dialog", u"4800", None))
        self.comboBoxSerial2.setItemText(2, QCoreApplication.translate("Dialog", u"9600", None))
        self.comboBoxSerial2.setItemText(3, QCoreApplication.translate("Dialog", u"14400", None))
        self.comboBoxSerial2.setItemText(4, QCoreApplication.translate("Dialog", u"19200", None))
        self.comboBoxSerial2.setItemText(5, QCoreApplication.translate("Dialog", u"38400", None))
        self.comboBoxSerial2.setItemText(6, QCoreApplication.translate("Dialog", u"56000", None))
        self.comboBoxSerial2.setItemText(7, QCoreApplication.translate("Dialog", u"57600", None))
        self.comboBoxSerial2.setItemText(8, QCoreApplication.translate("Dialog", u"115200", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u55b7\u7801\u673a\u4e8c\u8bbe\u7f6e", None))
        self.comboBoxSerial3.setItemText(0, QCoreApplication.translate("Dialog", u"COM1", None))
        self.comboBoxSerial3.setItemText(1, QCoreApplication.translate("Dialog", u"COM2", None))
        self.comboBoxSerial3.setItemText(2, QCoreApplication.translate("Dialog", u"COM3", None))
        self.comboBoxSerial3.setItemText(3, QCoreApplication.translate("Dialog", u"COM4", None))
        self.comboBoxSerial3.setItemText(4, QCoreApplication.translate("Dialog", u"COM5", None))
        self.comboBoxSerial3.setItemText(5, QCoreApplication.translate("Dialog", u"COM6", None))
        self.comboBoxSerial3.setItemText(6, QCoreApplication.translate("Dialog", u"COM7", None))
        self.comboBoxSerial3.setItemText(7, QCoreApplication.translate("Dialog", u"COM8", None))
        self.comboBoxSerial3.setItemText(8, QCoreApplication.translate("Dialog", u"COM9", None))
        self.comboBoxSerial3.setItemText(9, QCoreApplication.translate("Dialog", u"COM10", None))

        self.comboBoxSerial4.setItemText(0, QCoreApplication.translate("Dialog", u"2400", None))
        self.comboBoxSerial4.setItemText(1, QCoreApplication.translate("Dialog", u"4800", None))
        self.comboBoxSerial4.setItemText(2, QCoreApplication.translate("Dialog", u"9600", None))
        self.comboBoxSerial4.setItemText(3, QCoreApplication.translate("Dialog", u"14400", None))
        self.comboBoxSerial4.setItemText(4, QCoreApplication.translate("Dialog", u"19200", None))
        self.comboBoxSerial4.setItemText(5, QCoreApplication.translate("Dialog", u"38400", None))
        self.comboBoxSerial4.setItemText(6, QCoreApplication.translate("Dialog", u"56000", None))
        self.comboBoxSerial4.setItemText(7, QCoreApplication.translate("Dialog", u"57600", None))
        self.comboBoxSerial4.setItemText(8, QCoreApplication.translate("Dialog", u"115200", None))

        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
    # retranslateUi

