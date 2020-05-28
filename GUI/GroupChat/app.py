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
        self.receive_function()

    def receive_function(self):
        self.thread = receive_message(self)
        self.thread.start()

class receive_message(QThread, GroupChatClientModel):

    message = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(receive_message, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.ready_to_read()
        # print(message)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
