# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PushButton, RadioButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(867, 596)
        self.pushButton = PushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 871, 381))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(390, 430, 221, 111))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = PushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = PushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_4 = PushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = PushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_6 = PushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.pushButton_7 = PushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_7.addWidget(self.pushButton_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(210, 550, 611, 31))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.lineEdit_4 = LineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)

        self.pushButton_8 = PushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_8.addWidget(self.pushButton_8)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 440, 181, 141))
        self.gridLayout = QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = LineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = LineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_3 = LineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.layoutWidget3 = QWidget(Form)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(220, 470, 151, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = RadioButton(self.layoutWidget3)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = RadioButton(self.layoutWidget3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 445, 61, 21))
        self.layoutWidget4 = QWidget(Form)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 390, 831, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit_5 = LineEdit(self.layoutWidget4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_2.addWidget(self.lineEdit_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"PDF\u76ee\u5f55\u751f\u6210\u5668", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165PDF\u6587\u4ef6", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u63d0\u53d6\u56fe\u50cf", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"OCR\u8bc6\u522b", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u4e66\u7b7e\u5199\u5165", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u5b8c\u6210", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u8def\u5f84\uff1a", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"./result/out/", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76ee\u5f55\u8d77\u59cb\u9875\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u76ee\u5f55\u7ed3\u675f\u9875\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6b63\u6587\u5f00\u59cb\u9875\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u5355\u680f", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u53cc\u680f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u76ee\u5f55\u683c\u5f0f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"PDF\u8def\u5f84\uff1a", None))
    # retranslateUi

