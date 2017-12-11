try:
    from PySide import QtGui, QtCore
except:
    from PySide2 import QtGui, QtCore
import os

import Animacion.Maya_Animacion_PlayblastExporter.playblastExport_Core.MKF_playblastCore
reload(Animacion.Maya_Animacion_PlayblastExporter.playblastExport_Core.MKF_playblastCore) 
from Animacion.Maya_Animacion_PlayblastExporter.playblastExport_Core.MKF_playblastCore import playblastExport
import Animacion.Maya_Animacion_PlayblastExporter.playblastExport_Core.MKF_SlackMessages
reload(Animacion.Maya_Animacion_PlayblastExporter.playblastExport_Core.MKF_SlackMessages)
from Animacion.Maya_Animacion_PlayblastExporter.playblastExport_Core.MKF_SlackMessages import Slack


class BridgeActions():
    def __init__(self, window_interface):
        """
        Start Interfaces control.

        This method creates buttons to analize what actions
        will evaluate the class.
        """
        self.master_window = window_interface

        # Create buttons identifiers main window
        self.txt_artistName = window_interface.txt_artistName
        self.txt_path = window_interface.txt_path
        self.btn_accept = window_interface.btn_accept
        self.btn_path = window_interface.btn_path
        self.rdbtn_local = window_interface.rdbtn_local
        self.rdbtn_server = window_interface.rdbtn_server
        # Make buttons connections
        self.rdbtn_local.setChecked(True)
        self.btn_accept.clicked.connect(self.accept)
        self.btn_path.clicked.connect(self.path)
        self.rdbtn_local.toggled.connect(self.changeRadioSignal)
        self.rdbtn_server.toggled.connect(self.changeRadioSignal)


        self.playblast = playblastExport()
        self.slack = Slack()
        self.path = self.playblast.getDocsPath()
        self.autoComplete()

    def accept(self):
        """
        """
        txt = self.txt_artistName.text()
        path = self.txt_path.text()
        self.writeLocalInfo(self.path + '/artist.txt', txt)

        
        name = self.playblast.fileName()
        if self.rdbtn_server.isChecked():
            if path.find('Z:/') != -1 or path.find('//master') != -1: 
                self.playblast.main(txt, path)
                self.slack.MessageSlack(Message = 'Se ha salvado el playblast *' + name + '* del animador *' + txt + '*.\n En la ruta: *' + path +'*', channel = 'playblasts')
                #self.slack.MessageSlack(Message = 'ya no funciona esta chingadera', channel = 'tickets_test')
            else:
                self.playblast.warnings(txt)
        else:
            self.playblast.main(txt, path)

    def path(self):

        local = self.rdbtn_local.isChecked()
        path = self.playblast.path()

        if local:
            self.txt_path.setText(path)
            self.writeLocalInfo(self.path + '/localpath.txt', self.txt_path.text())
        else:
            self.txt_path.setText(path)
            self.writeLocalInfo(self.path + '/serverpath.txt', self.txt_path.text())
    def autoComplete(self):
        self.readLocalInfo(self.path + '/localpath.txt', self.txt_path)
        self.readLocalInfo(self.path + '/artist.txt', self.txt_artistName)

    def readLocalInfo(self, file, txt):
        if os.path.exists(file + '.txt'):
            with open(file + '.txt' ,'r') as f:
                data = f.read()
            txt.setText(data)
            return True
        else:
            return False
    def writeLocalInfo(self, file, txt):
        with open(file + '.txt' ,'w') as f:
            data = f.write(txt)
    def changeRadioSignal(self):

        if self.rdbtn_local.isChecked():
            self.readLocalInfo(self.path + '/localpath.txt', self.txt_path)
        else:
            self.readLocalInfo(self.path + '/serverpath.txt', self.txt_path)





