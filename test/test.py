# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowwZvuok.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.frame)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(500, 200))
        self.top.setMaximumSize(QSize(16777215, 200))
        self.top.setStyleSheet(u"background-color: rgb(113, 113, 113);")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left = QFrame(self.top)
        self.left.setObjectName(u"left")
        self.left.setStyleSheet(u"")
        self.left.setFrameShape(QFrame.StyledPanel)
        self.left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.left)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:30px;")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.left)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:25px;")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.left, 0, Qt.AlignLeft|Qt.AlignTop)

        self.center = QFrame(self.top)
        self.center.setObjectName(u"center")
        self.center.setFrameShape(QFrame.StyledPanel)
        self.center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.center)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../data/torvolds.jpg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.center)

        self.right = QFrame(self.top)
        self.right.setObjectName(u"right")
        self.right.setStyleSheet(u"")
        self.right.setFrameShape(QFrame.StyledPanel)
        self.right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.right)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size:30px;")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.textBrowser = QTextBrowser(self.right)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_4.addWidget(self.textBrowser)


        self.horizontalLayout_2.addWidget(self.right, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.top)

        self.bottom = QFrame(self.frame)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.bottom)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget = QTableWidget(self.bottom)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.bottom)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Linus Torvalds", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bio", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A Free Software Developer, with more decades of experience than we care to admit</span></p></body></html>", None))
    # retranslateUi

