# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FenClient.ui'
#
# Created: Thu Apr 16 11:34:21 2015
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
        FenClient.resize(614, 587)
        self.centralwidget = QtGui.QWidget(FenClient)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-60, 10, 751, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Showcard Gothic"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.ecranMain = QtGui.QTextBrowser(self.centralwidget)
        self.ecranMain.setGeometry(QtCore.QRect(10, 80, 591, 381))
        self.ecranMain.setObjectName(_fromUtf8("ecranMain"))
        self.label_all = QtGui.QLabel(self.centralwidget)
        self.label_all.setGeometry(QtCore.QRect(70, 50, 491, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_all.setFont(font)
        self.label_all.setAlignment(QtCore.Qt.AlignCenter)
        self.label_all.setObjectName(_fromUtf8("label_all"))
        self.message = QtGui.QLineEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(60, 480, 281, 49))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setObjectName(_fromUtf8("message"))
        self.btnEnvoyer = QtGui.QPushButton(self.centralwidget)
        self.btnEnvoyer.setGeometry(QtCore.QRect(370, 490, 171, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/chat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnvoyer.setIcon(icon)
        self.btnEnvoyer.setObjectName(_fromUtf8("btnEnvoyer"))
        self.label_msg = QtGui.QLabel(self.centralwidget)
        self.label_msg.setGeometry(QtCore.QRect(10, 490, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName(_fromUtf8("label_msg"))
        FenClient.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FenClient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        FenClient.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FenClient)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FenClient.setStatusBar(self.statusbar)

        self.retranslateUi(FenClient)
        QtCore.QMetaObject.connectSlotsByName(FenClient)

    def retranslateUi(self, FenClient):
        FenClient.setWindowTitle(_translate("FenClient", "DNC", None))
        self.title.setText(_translate("FenClient", "Dog is Not a Chat", None))
        self.label_all.setText(_translate("FenClient", "Chat console", None))
        self.btnEnvoyer.setText(_translate("FenClient", "Send", None))
        self.label_msg.setText(_translate("FenClient", "Input", None))

