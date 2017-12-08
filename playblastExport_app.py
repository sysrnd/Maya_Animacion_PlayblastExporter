"""
StandAlone pyqt4

"""
import sys
import platform
from PySide import QtCore, QtGui
import MKF_playblastExport.playblastExport_UI.MainWindow_v02
reload(MKF_playblastExport.playblastExport_UI.MainWindow_v02)
from MKF_playblastExport.playblastExport_UI.MainWindow_v02 import Ui_PlayblastWindow
import MKF_playblastExport.playblastExport_Core.playblastExportBridge
reload(MKF_playblastExport.playblastExport_Core.playblastExportBridge)
from MKF_playblastExport.playblastExport_Core.playblastExportBridge import *

#reload(MKF_playblastExport.playblastExport_Core.playblastExportBridge)

#Por ventana que hayas disenado

class MyApplication(QtGui.QMainWindow, Ui_PlayblastWindow):

    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)

if __name__ != "__main__":
    try:
        app = QtGui.QApplication(sys.argv)
    except:
        app = QtCore.QCoreApplication.instance()
    window = MyApplication()
    
    
    window.setWindowFlags(
        window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    
    interfaceMacho = BridgeActions(window_interface=window)
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        "error al intentar salir"