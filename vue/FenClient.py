# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FenClient.ui'
#
# Created: Wed Apr 15 10:07:21 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FenClient(object):
    def setupUi(self, FenClient):
        FenClient.setObjectName(_fromUtf8("FenClient"))
        FenClient.resize(777, 587)
        self.centralwidget = QtGui.QWidget(FenClient)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 751, 28))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_ip = QtGui.QLabel(self.layoutWidget)
        self.label_ip.setObjectName(_fromUtf8("label_ip"))
        self.horizontalLayout.addWidget(self.label_ip)
        self.serveurIP = QtGui.QLineEdit(self.layoutWidget)
        self.serveurIP.setMaximumSize(QtCore.QSize(150, 16777215))
        self.serveurIP.setObjectName(_fromUtf8("serveurIP"))
        self.horizontalLayout.addWidget(self.serveurIP)
        self.label_port = QtGui.QLabel(self.layoutWidget)
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.horizontalLayout.addWidget(self.label_port)
        self.serveurPort = QtGui.QSpinBox(self.layoutWidget)
        self.serveurPort.setMinimumSize(QtCore.QSize(60, 0))
        self.serveurPort.setMinimum(1024)
        self.serveurPort.setMaximum(65535)
        self.serveurPort.setProperty("value", 8000)
        self.serveurPort.setObjectName(_fromUtf8("serveurPort"))
        self.horizontalLayout.addWidget(self.serveurPort)
        self.btnConnexion = QtGui.QPushButton(self.layoutWidget)
        self.btnConnexion.setObjectName(_fromUtf8("btnConnexion"))
        self.horizontalLayout.addWidget(self.btnConnexion)
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 480, 751, 51))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_pseudo = QtGui.QLabel(self.layoutWidget_2)
        self.label_pseudo.setObjectName(_fromUtf8("label_pseudo"))
        self.horizontalLayout_2.addWidget(self.label_pseudo)
        self.pseudo = QtGui.QLineEdit(self.layoutWidget_2)
        self.pseudo.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pseudo.sizePolicy().hasHeightForWidth())
        self.pseudo.setSizePolicy(sizePolicy)
        self.pseudo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pseudo.setObjectName(_fromUtf8("pseudo"))
        self.horizontalLayout_2.addWidget(self.pseudo)
        self.label_msg = QtGui.QLabel(self.layoutWidget_2)
        self.label_msg.setObjectName(_fromUtf8("label_msg"))
        self.horizontalLayout_2.addWidget(self.label_msg)
        self.message = QtGui.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setObjectName(_fromUtf8("message"))
        self.horizontalLayout_2.addWidget(self.message)
        self.btnEnvoyer = QtGui.QPushButton(self.layoutWidget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Downloads/chat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnvoyer.setIcon(icon)
        self.btnEnvoyer.setObjectName(_fromUtf8("btnEnvoyer"))
        self.horizontalLayout_2.addWidget(self.btnEnvoyer)
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.label_online = QtGui.QLabel(self.centralwidget)
        self.label_online.setGeometry(QtCore.QRect(510, 110, 251, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_online.setFont(font)
        self.label_online.setAlignment(QtCore.Qt.AlignCenter)
        self.label_online.setObjectName(_fromUtf8("label_online"))
        self.label_private = QtGui.QLabel(self.centralwidget)
        self.label_private.setGeometry(QtCore.QRect(510, 290, 251, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_private.setFont(font)
        self.label_private.setAlignment(QtCore.Qt.AlignCenter)
        self.label_private.setObjectName(_fromUtf8("label_private"))
        self.ecranOnline = QtGui.QListWidget(self.centralwidget)
        self.ecranOnline.setGeometry(QtCore.QRect(510, 140, 256, 141))
        self.ecranOnline.setObjectName(_fromUtf8("ecranOnline"))
        self.ecranPrivate = QtGui.QListWidget(self.centralwidget)
        self.ecranPrivate.setGeometry(QtCore.QRect(510, 320, 256, 141))
        self.ecranPrivate.setObjectName(_fromUtf8("ecranPrivate"))
        self.ecranMain = QtGui.QTextBrowser(self.centralwidget)
        self.ecranMain.setGeometry(QtCore.QRect(10, 140, 491, 321))
        self.ecranMain.setObjectName(_fromUtf8("ecranMain"))
        self.label_all = QtGui.QLabel(self.centralwidget)
        self.label_all.setGeometry(QtCore.QRect(10, 110, 491, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_all.setFont(font)
        self.label_all.setAlignment(QtCore.Qt.AlignCenter)
        self.label_all.setObjectName(_fromUtf8("label_all"))
        FenClient.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FenClient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        FenClient.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FenClient)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FenClient.setStatusBar(self.statusbar)

        self.retranslateUi(FenClient)
        QtCore.QMetaObject.connectSlotsByName(FenClient)

    def retranslateUi(self, FenClient):
        FenClient.setWindowTitle(_translate("FenClient", "DNC", None))
        self.label_ip.setText(_translate("FenClient", "Server\'s IP adress :", None))
        self.serveurIP.setText(_translate("FenClient", "localhost", None))
        self.label_port.setText(_translate("FenClient", "Server\'s Port :", None))
        self.btnConnexion.setText(_translate("FenClient", "Connexion", None))
        self.label_pseudo.setText(_translate("FenClient", "Login :", None))
        self.label_msg.setText(_translate("FenClient", "Message :", None))
        self.btnEnvoyer.setText(_translate("FenClient", "Send", None))
        self.title.setText(_translate("FenClient", "Dog is Not a Chat", None))
        self.label_online.setText(_translate("FenClient", "Users online", None))
        self.label_private.setText(_translate("FenClient", "Users in private mode", None))
        self.label_all.setText(_translate("FenClient", "All messages", None))

