# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_info_window(object):
    def setupUi(self, info_window):
        if not info_window.objectName():
            info_window.setObjectName(u"info_window")
        info_window.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(info_window.sizePolicy().hasHeightForWidth())
        info_window.setSizePolicy(sizePolicy)
        info_window.setMinimumSize(QSize(960, 540))
        info_window.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        info_window.setFont(font)
        info_window.setStyleSheet(u"QPushButton {\n"
"border-radius: 12px;\n"
"padding-left: 16px;\n"
"padding-right: 16px;\n"
"padding-top: 8 px;\n"
"padding-bottom: 8 px;\n"
"}")
        self.gridLayout = QGridLayout(info_window)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.lb_title = QLabel(info_window)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Vitesco"])
        font1.setPointSize(32)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.lb_title.setFont(font1)
        self.lb_title.setStyleSheet(u"QLabel\n"
"{\n"
"	\n"
"	color: rgb(190, 190, 190);\n"
"}")
        self.lb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_title, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pb_back = QPushButton(info_window)
        self.pb_back.setObjectName(u"pb_back")

        self.gridLayout.addWidget(self.pb_back, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.pb_contacts = QPushButton(info_window)
        self.pb_contacts.setObjectName(u"pb_contacts")

        self.gridLayout.addWidget(self.pb_contacts, 1, 2, 1, 1)

        self.stackedWidget = QStackedWidget(info_window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)


        self.retranslateUi(info_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(info_window)
    # setupUi

    def retranslateUi(self, info_window):
        info_window.setWindowTitle(QCoreApplication.translate("info_window", u"CIIT", None))
        self.lb_title.setText(QCoreApplication.translate("info_window", u"Info", None))
        self.pb_back.setText(QCoreApplication.translate("info_window", u"Go Back", None))
        self.pb_contacts.setText(QCoreApplication.translate("info_window", u"Contacts", None))
    # retranslateUi

