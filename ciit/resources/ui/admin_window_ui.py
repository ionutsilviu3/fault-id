# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_admin_overview(object):
    def setupUi(self, admin_overview):
        if not admin_overview.objectName():
            admin_overview.setObjectName(u"admin_overview")
        admin_overview.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(admin_overview.sizePolicy().hasHeightForWidth())
        admin_overview.setSizePolicy(sizePolicy)
        admin_overview.setMinimumSize(QSize(960, 540))
        admin_overview.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Vitesco"])
        font.setPointSize(12)
        admin_overview.setFont(font)
        admin_overview.setStyleSheet(u"QPushButton {\n"
"border-radius: 12px;\n"
"padding-left: 16px;\n"
"padding-right: 16px;\n"
"padding-top: 8 px;\n"
"padding-bottom: 8 px;\n"
"}")
        self.gridLayout = QGridLayout(admin_overview)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.lb_title = QLabel(admin_overview)
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

        self.gridLayout.addWidget(self.lb_title, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.vl_center = QVBoxLayout()
        self.vl_center.setSpacing(16)
        self.vl_center.setObjectName(u"vl_center")
        self.tw_users = QTableWidget(admin_overview)
        if (self.tw_users.rowCount() < 1):
            self.tw_users.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_users.setVerticalHeaderItem(0, __qtablewidgetitem)
        self.tw_users.setObjectName(u"tw_users")
        self.tw_users.setMaximumSize(QSize(512, 16777215))
        self.tw_users.setStyleSheet(u"")

        self.vl_center.addWidget(self.tw_users, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pb_modify_role = QPushButton(admin_overview)
        self.pb_modify_role.setObjectName(u"pb_modify_role")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.pb_modify_role.setFont(font2)
        self.pb_modify_role.setStyleSheet(u"background-color: rgb(161, 172, 177);\n"
"color: rgb(255, 0, 0);")

        self.vl_center.addWidget(self.pb_modify_role, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pb_delete = QPushButton(admin_overview)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_delete.sizePolicy().hasHeightForWidth())
        self.pb_delete.setSizePolicy(sizePolicy1)
        self.pb_delete.setMaximumSize(QSize(256, 16777215))
        self.pb_delete.setFont(font2)
        self.pb_delete.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"	background-color: rgb(215,0,75)\n"
"    }\n"
"QPushButton:disabled {\n"
"	background-color: rgba(170, 35, 0, 150);\n"
"    }\n"
"    QPushButton:hover {\n"
"	background-color: rgb(193, 35, 0);\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"	background-color: rgb(129, 24, 0);\n"
"    }")

        self.vl_center.addWidget(self.pb_delete, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lb_message = QLabel(admin_overview)
        self.lb_message.setObjectName(u"lb_message")

        self.vl_center.addWidget(self.lb_message, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.le_users = QLineEdit(admin_overview)
        self.le_users.setObjectName(u"le_users")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_users.sizePolicy().hasHeightForWidth())
        self.le_users.setSizePolicy(sizePolicy2)
        self.le_users.setMinimumSize(QSize(128, 34))
        self.le_users.setMaximumSize(QSize(512, 34))
        self.le_users.setSizeIncrement(QSize(0, 0))
        self.le_users.setFont(font2)
        self.le_users.setStyleSheet(u"color: black;\n"
"background-color: #A1ACB1;\n"
"border-radius: 12px;\n"
"padding: 8px 32px;\n"
"")
        self.le_users.setInputMask(u"")
        self.le_users.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vl_center.addWidget(self.le_users)

        self.hl_center = QHBoxLayout()
        self.hl_center.setSpacing(8)
        self.hl_center.setObjectName(u"hl_center")
        self.pb_add = QPushButton(admin_overview)
        self.pb_add.setObjectName(u"pb_add")
        sizePolicy1.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setKerning(True)
        self.pb_add.setFont(font3)
        self.pb_add.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(37, 132, 46);\n"
"    }\n"
"QPushButton:disabled {\n"
"	background-color: rgba(170, 35, 0, 150);\n"
"    }\n"
"    QPushButton:hover {\n"
"	\n"
"	background-color: rgb(30, 107, 36);\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(27, 97, 33);\n"
"    }")

        self.hl_center.addWidget(self.pb_add, 0, Qt.AlignmentFlag.AlignHCenter)


        self.vl_center.addLayout(self.hl_center)


        self.gridLayout.addLayout(self.vl_center, 1, 1, 1, 1)

        self.pb_main_app = QPushButton(admin_overview)
        self.pb_main_app.setObjectName(u"pb_main_app")

        self.gridLayout.addWidget(self.pb_main_app, 1, 3, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.vl_chart = QVBoxLayout()
        self.vl_chart.setObjectName(u"vl_chart")

        self.gridLayout.addLayout(self.vl_chart, 1, 2, 1, 1)


        self.retranslateUi(admin_overview)

        QMetaObject.connectSlotsByName(admin_overview)
    # setupUi

    def retranslateUi(self, admin_overview):
        admin_overview.setWindowTitle(QCoreApplication.translate("admin_overview", u"CIIT", None))
        self.lb_title.setText(QCoreApplication.translate("admin_overview", u"Admin", None))
        self.pb_modify_role.setText(QCoreApplication.translate("admin_overview", u"Remove manager role", None))
        self.pb_delete.setText(QCoreApplication.translate("admin_overview", u"Delete User", None))
        self.lb_message.setText(QCoreApplication.translate("admin_overview", u"User added!", None))
        self.le_users.setText("")
        self.le_users.setPlaceholderText(QCoreApplication.translate("admin_overview", u"Add user by email", None))
        self.pb_add.setText(QCoreApplication.translate("admin_overview", u"Add user", None))
        self.pb_main_app.setText(QCoreApplication.translate("admin_overview", u"Go to main app", None))
    # retranslateUi

