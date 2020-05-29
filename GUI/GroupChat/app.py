from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.GroupChatWindow import Ui_group_chat_window
from view.ChatList import Ui_ChatList
# from model.GroupChatServerModel import GroupChatServerModel
from model.GroupChatClientModel import GroupChatClientModel

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow, Ui_ChatList):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Panggil function untuk start thread
        self.receive_function()

        # Jika list item di click
        self.chat_list.itemActivated.connect(self.chat_click)

        # Menampung windows
        self.popups = []

    def receive_function(self):
        self.thread = receive_message(self)
        self.thread.start()

    def chat_click(self):
        self.chat = GroupChatWindow()
        self.hide()
        self.chat.show()

class GroupChatWindow(QMainWindow, Ui_group_chat_window):

    def __init__(self):
        super(GroupChatWindow, self).__init__()
        self.setupUi(self)

# Untuk thread ambil message dari DB
class receive_message(QThread, GroupChatClientModel):

    def __init__(self, *args, **kwargs):
        super(receive_message, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs
        print('ready to read init')

    def run(self):
        self.ready_to_read()
        # print(message)

def start():
    window = MainWindow()
    window.show() 

    return window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = start()
    app.exec_()