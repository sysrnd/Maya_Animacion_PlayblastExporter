# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\MKF_playblastExport\playblastExport_UI\MainWindow_v02.ui'
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

class Ui_PlayblastWindow(object):
    def setupUi(self, PlayblastWindow):
        PlayblastWindow.setObjectName(_fromUtf8("PlayblastWindow"))
        PlayblastWindow.resize(503, 282)
        self.centralwidget = QtGui.QWidget(PlayblastWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lyt_vertical_main = QtGui.QVBoxLayout()
        self.lyt_vertical_main.setObjectName(_fromUtf8("lyt_vertical_main"))
        self.lyt_horizontal_artist = QtGui.QHBoxLayout()
        self.lyt_horizontal_artist.setObjectName(_fromUtf8("lyt_horizontal_artist"))
        spacerItem = QtGui.QSpacerItem(80, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lyt_horizontal_artist.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lyt_horizontal_artist.addItem(spacerItem1)
        self.lbl_artistName = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lbl_artistName.setFont(font)
        self.lbl_artistName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_artistName.setFrameShadow(QtGui.QFrame.Plain)
        self.lbl_artistName.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_artistName.setObjectName(_fromUtf8("lbl_artistName"))
        self.lyt_horizontal_artist.addWidget(self.lbl_artistName)
        self.txt_artistName = QtGui.QLineEdit(self.centralwidget)
        self.txt_artistName.setText(_fromUtf8(""))
        self.txt_artistName.setObjectName(_fromUtf8("txt_artistName"))
        self.lyt_horizontal_artist.addWidget(self.txt_artistName)
        self.lyt_vertical_main.addLayout(self.lyt_horizontal_artist)
        self.lyt_grid_rdbtns = QtGui.QGridLayout()
        self.lyt_grid_rdbtns.setObjectName(_fromUtf8("lyt_grid_rdbtns"))
        self.rdbtn_local = QtGui.QRadioButton(self.centralwidget)
        self.rdbtn_local.setObjectName(_fromUtf8("rdbtn_local"))
        self.lyt_grid_rdbtns.addWidget(self.rdbtn_local, 0, 0, 1, 1)
        self.rdbtn_server = QtGui.QRadioButton(self.centralwidget)
        self.rdbtn_server.setObjectName(_fromUtf8("rdbtn_server"))
        self.lyt_grid_rdbtns.addWidget(self.rdbtn_server, 0, 1, 1, 1)
        self.lyt_vertical_main.addLayout(self.lyt_grid_rdbtns)
        self.lyt_horizontal_path = QtGui.QVBoxLayout()
        self.lyt_horizontal_path.setObjectName(_fromUtf8("lyt_horizontal_path"))
        self.lyt_vertical_path = QtGui.QHBoxLayout()
        self.lyt_vertical_path.setObjectName(_fromUtf8("lyt_vertical_path"))
        self.txt_path = QtGui.QLineEdit(self.centralwidget)
        self.txt_path.setText(_fromUtf8(""))
        self.txt_path.setObjectName(_fromUtf8("txt_path"))
        self.lyt_vertical_path.addWidget(self.txt_path)
        self.btn_path = QtGui.QPushButton(self.centralwidget)
        self.btn_path.setObjectName(_fromUtf8("btn_path"))
        self.lyt_vertical_path.addWidget(self.btn_path)
        self.lyt_horizontal_path.addLayout(self.lyt_vertical_path)
        self.lyt_vertical_main.addLayout(self.lyt_horizontal_path)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lyt_vertical_main.addItem(spacerItem2)
        self.lyt__horizontal_btn_playblastr = QtGui.QVBoxLayout()
        self.lyt__horizontal_btn_playblastr.setObjectName(_fromUtf8("lyt__horizontal_btn_playblastr"))
        self.lyt_vertical_playblast = QtGui.QHBoxLayout()
        self.lyt_vertical_playblast.setObjectName(_fromUtf8("lyt_vertical_playblast"))
        self.btn_accept = QtGui.QPushButton(self.centralwidget)
        self.btn_accept.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.btn_accept.sizePolicy().hasHeightForWidth())
        self.btn_accept.setSizePolicy(sizePolicy)
        self.btn_accept.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.btn_accept.setFont(font)
        self.btn_accept.setObjectName(_fromUtf8("btn_accept"))
        self.lyt_vertical_playblast.addWidget(self.btn_accept)
        self.lyt__horizontal_btn_playblastr.addLayout(self.lyt_vertical_playblast)
        self.lyt_vertical_main.addLayout(self.lyt__horizontal_btn_playblastr)
        self.horizontalLayout.addLayout(self.lyt_vertical_main)
        PlayblastWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PlayblastWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PlayblastWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PlayblastWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PlayblastWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlayblastWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayblastWindow)

    def retranslateUi(self, PlayblastWindow):
        PlayblastWindow.setWindowTitle(_translate("PlayblastWindow", "MainWindow", None))
        self.lbl_artistName.setText(_translate("PlayblastWindow", "Artista", None))
        self.rdbtn_local.setText(_translate("PlayblastWindow", "Salvar a local", None))
        self.rdbtn_server.setText(_translate("PlayblastWindow", "Publicar al servidor", None))
        self.btn_path.setText(_translate("PlayblastWindow", "Path", None))
        self.btn_accept.setText(_translate("PlayblastWindow", "Playblast", None))

