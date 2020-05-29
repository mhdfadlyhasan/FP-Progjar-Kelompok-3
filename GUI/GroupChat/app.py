from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.GroupChat import Ui_group_chat_window
from view.ChatList import Ui_ChatList
from model.GroupChatClientModel import GroupChatClientModel

# Only needed for access to command line arguments
import sys
import io

# Subclass QMainWindow to customise your application's main window

username = None

class ChatList(QMainWindow, Ui_ChatList):

    def __init__(self):
        super(ChatList, self).__init__()
        self.setupUi(self)

        # Client Connect
        print('here')
        model = GroupChatClientModel()
        username = model.connect()
        
        # Temp
        self.chat_click()

    def chat_click(self):
        self.chat = GroupChatWindow()
        self.chat.show()

class GroupChatWindow(QMainWindow, Ui_group_chat_window):

    def __init__(self):
        super(GroupChatWindow, self).__init__()
        self.setupUi(self)

        # Panggil function untuk start thread
        self.client_run()

        # When list item is clicked
        self.input.returnPressed.connect(self.message_input)

    # Custom Functions
    def client_run(self):
        self.thread = client_thread(self)
        self.thread.start()

    # Detect Message Input
    def message_input(self):
        # Ambil input dari GUI
        message = self.input.text()
        self.input.clear()

        # Print input user di message list
        if (message[0] == '<'):
            pass
        else:
            self.message_list.append(str(username) + ': ' + str(message))
        
        # Send message ke thread client
        sys.stdin = io.StringIO(message) 
        # model.stdinprint()

# Untuk thread ambil message dari DB
class client_thread(QThread, GroupChatClientModel):

    def __init__(self, *args, **kwargs):
        super(client_thread, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs
        print('Client running')

    def run(self):
        self.group_chat()
        # print(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatList()
    window.show()
    app.exec_()