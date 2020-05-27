from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.Ui_group_chat_window import Ui_group_chat_window
from model.GroupChatServerModel import GroupChatServerModel
from model.GroupChatClientModel import GroupChatClientModel

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow, Ui_group_chat_window):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

class ClientStart(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        
        # Instantiation
        client = GroupChatClientModel()
        client.main()

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

#Thread
client_thread = ClientStart()
client_thread.start()

# Start the event loop.
app.exec_()
