# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindFDZNa.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(294, 219)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.chkCondition = QCheckBox(self.centralwidget)
        self.chkCondition.setObjectName(u"chkCondition")
        self.chkCondition.setGeometry(QRect(90, 90, 120, 20))
        self.lbStatus = QLabel(self.centralwidget)
        self.lbStatus.setObjectName(u"lbStatus")
        self.lbStatus.setGeometry(QRect(10, 10, 270, 61))
        font = QFont()
        font.setPointSize(15)
        self.lbStatus.setFont(font)
        self.lbStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(110, 130, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 294, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.chkCondition.setText(QCoreApplication.translate("MainWindow", u"Condition Check", None))
        self.lbStatus.setText(QCoreApplication.translate("MainWindow", u"Click The Button", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

