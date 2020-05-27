from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from view.UiFtpClient import UiFTPClient
from model.FTPClientModel import FTPClientModel
import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow, UiFTPClient):
    client = None
    username = "dex"
    password = "123"
    host = '127.0.0.1'
    port = 8009

    fsModel = None
    remoteModel = None

    remoteDir = []
    localDir = []

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.client = FTPClientModel()
        self.setupUi(self)

        self.connectBtn.pressed.connect(self.connect_slot)
        self.filesystem_model()
        self.localTreeDir.clicked.connect(
            self.clicked_tree_view_local)

    # Slot for input
    def connect_slot(self):
        if not self.client.isConnected:
            self.username = self.usernameInput.text()
            self.password = self.passwordInput.text()
            self.host = self.hostInput.text()
            self.port = int(self.portInput.text())

            self.client.connect(self.username, self.password,
                                self.host, self.port)
            self.connectBtn.setText('Disconnect')

            list_dir = self.client.list_dir('.')

            self.remote_filesystem_model()
        else:
            self.client.disconnect()
            self.connectBtn.setText('Connect')

    def filesystem_model(self, path="."):
        self.fsModel = QFileSystemModel()
        self.fsModel.setRootPath(path)

        self.render_tree_view(self.fsModel, QDir(path), self.localTreeDir)

    @staticmethod
    def render_tree_view(fsModel: QFileSystemModel, path: QDir, view: QTreeView):
        view.setModel(fsModel)
        view.setRootIndex(fsModel.index(path.absolutePath()))

    def clicked_tree_view_local(self, index):
        path = self.fsModel.fileInfo(index).absoluteFilePath()
        self.render_tree_view(self.fsModel, path, self.localTreeDir)

    # REMOTE
    def get_list_dir_remote(self, path="."):
        self.remoteDir = self.client.list_dir()

    def change_dir_remote(self, path):
        self.remoteDir = self.client.change_dir(path)

    def remote_filesystem_model(self, path="."):
        self.fsModel = QFileSystemModel()
        self.fsModel.setRootPath(path)

        self.render_tree_view(self.fsModel, QDir(path), self.remoteTreeDir)

    def clicked_tree_view_remote(self, index):
        path = self.fsModel.fileInfo(index).absoluteFilePath()
        self.render_tree_view(self.fsModel, path, self.remoteTreeDir)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
