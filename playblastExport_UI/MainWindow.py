# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\MKF_playblastExport\MKF_playblastExport_UI\MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(385, 297)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(385, 297))
        MainWindow.setMaximumSize(QtCore.QSize(385, 297))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet(_fromUtf8("Qwidget::setFixedSize() "))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbl_title = QtGui.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(120, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.txt_artistName = QtGui.QTextEdit(self.centralwidget)
        self.txt_artistName.setGeometry(QtCore.QRect(70, 100, 251, 41))
        self.txt_artistName.setStatusTip(_fromUtf8(""))
        self.txt_artistName.setWhatsThis(_fromUtf8(""))
        self.txt_artistName.setObjectName(_fromUtf8("txt_artistName"))
        self.lbl_artist = QtGui.QLabel(self.centralwidget)
        self.lbl_artist.setGeometry(QtCore.QRect(160, 150, 71, 31))
        self.lbl_artist.setObjectName(_fromUtf8("lbl_artist"))
        self.btn_accept = QtGui.QPushButton(self.centralwidget)
        self.btn_accept.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.btn_accept.setObjectName(_fromUtf8("btn_accept"))
        self.btn_cancel = QtGui.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(260, 230, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 385, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_title.setText(_translate("MainWindow", "Playblast creator", None))
        self.txt_artistName.setToolTip(_translate("MainWindow", "<html><head/><body><p>ervgretgvbr</p></body></html>", None))
        self.txt_artistName.setAccessibleName(_translate("MainWindow", "accessibleName", None))
        self.txt_artistName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.lbl_artist.setText(_translate("MainWindow", "Artist name", None))
        self.btn_accept.setText(_translate("MainWindow", "&Accept", None))
        self.btn_cancel.setText(_translate("MainWindow", "&Cancel", None))

