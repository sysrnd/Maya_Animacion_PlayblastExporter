# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\MKF_playblastExport\playblastExport_UI\MainWindow_v02.ui'

#

# Created by: PyQt4 UI code generator 4.11.4

#

# WARNING! All changes made in this file will be lost!



from Modules.Qt import QtCore, QtGui, QtWidgets


try:

    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig)



class Ui_PlayblastWindow(object):

    def setupUi(self, PlayblastWindow):

        PlayblastWindow.setObjectName("PlayblastWindow")

        PlayblastWindow.resize(503, 282)

        self.centralwidget = QtWidgets.QWidget(PlayblastWindow)

        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lyt_vertical_main = QtWidgets.QVBoxLayout()

        self.lyt_vertical_main.setObjectName("lyt_vertical_main")

        self.lyt_horizontal_artist = QtWidgets.QHBoxLayout()

        self.lyt_horizontal_artist.setObjectName("lyt_horizontal_artist")

        spacerItem = QtWidgets.QSpacerItem(80, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.lyt_horizontal_artist.addItem(spacerItem)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.lyt_horizontal_artist.addItem(spacerItem1)

        self.lbl_artistName = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()

        font.setPointSize(10)

        font.setBold(False)

        font.setItalic(True)

        font.setWeight(50)

        self.lbl_artistName.setFont(font)

        self.lbl_artistName.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.lbl_artistName.setFrameShadow(QtWidgets.QFrame.Plain)

        self.lbl_artistName.setAlignment(QtCore.Qt.AlignCenter)

        self.lbl_artistName.setObjectName("lbl_artistName")

        self.lyt_horizontal_artist.addWidget(self.lbl_artistName)

        self.txt_artistName = QtWidgets.QLineEdit(self.centralwidget)

        self.txt_artistName.setText("")

        self.txt_artistName.setObjectName("txt_artistName")

        self.lyt_horizontal_artist.addWidget(self.txt_artistName)

        self.lyt_vertical_main.addLayout(self.lyt_horizontal_artist)

        self.lyt_grid_rdbtns = QtWidgets.QGridLayout()

        self.lyt_grid_rdbtns.setObjectName("lyt_grid_rdbtns")

        self.rdbtn_local = QtWidgets.QRadioButton(self.centralwidget)

        self.rdbtn_local.setObjectName("rdbtn_local")

        self.lyt_grid_rdbtns.addWidget(self.rdbtn_local, 0, 0, 1, 1)

        self.rdbtn_server = QtWidgets.QRadioButton(self.centralwidget)

        self.rdbtn_server.setObjectName("rdbtn_server")

        self.lyt_grid_rdbtns.addWidget(self.rdbtn_server, 0, 1, 1, 1)

        self.lyt_vertical_main.addLayout(self.lyt_grid_rdbtns)

        self.lyt_horizontal_path = QtWidgets.QVBoxLayout()

        self.lyt_horizontal_path.setObjectName("lyt_horizontal_path")

        self.lyt_vertical_path = QtWidgets.QHBoxLayout()

        self.lyt_vertical_path.setObjectName("lyt_vertical_path")

        self.txt_path = QtWidgets.QLineEdit(self.centralwidget)

        self.txt_path.setText("")

        self.txt_path.setObjectName("txt_path")

        self.lyt_vertical_path.addWidget(self.txt_path)

        self.btn_path = QtWidgets.QPushButton(self.centralwidget)

        self.btn_path.setObjectName("btn_path")

        self.lyt_vertical_path.addWidget(self.btn_path)

        self.lyt_horizontal_path.addLayout(self.lyt_vertical_path)

        self.lyt_vertical_main.addLayout(self.lyt_horizontal_path)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.lyt_vertical_main.addItem(spacerItem2)

        self.lyt__horizontal_btn_playblastr = QtWidgets.QVBoxLayout()

        self.lyt__horizontal_btn_playblastr.setObjectName("lyt__horizontal_btn_playblastr")

        self.lyt_vertical_playblast = QtWidgets.QHBoxLayout()

        self.lyt_vertical_playblast.setObjectName("lyt_vertical_playblast")

        self.btn_accept = QtWidgets.QPushButton(self.centralwidget)

        self.btn_accept.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

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

        self.btn_accept.setObjectName("btn_accept")

        self.lyt_vertical_playblast.addWidget(self.btn_accept)

        self.lyt__horizontal_btn_playblastr.addLayout(self.lyt_vertical_playblast)

        self.lyt_vertical_main.addLayout(self.lyt__horizontal_btn_playblastr)

        self.horizontalLayout.addLayout(self.lyt_vertical_main)

        PlayblastWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(PlayblastWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 21))

        self.menubar.setObjectName("menubar")

        PlayblastWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(PlayblastWindow)

        self.statusbar.setObjectName("statusbar")

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



