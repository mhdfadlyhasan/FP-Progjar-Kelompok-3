from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.GroupChat import Ui_group_chat_window
from view.ChatList import Ui_ChatList
from model.GroupChatClientModel import GroupChatClientModel

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customise your application's main window

class ChatList(QMainWindow, Ui_ChatList):

    def __init__(self):
        super(ChatList, self).__init__()
        self.setupUi(self)

        self.chat_click()

    def chat_click(self):
        self.chat = GroupChatWindow()
        self.chat.show()

class GroupChatWindow(QMainWindow, Ui_group_chat_window):

    def __init__(self):
        super(GroupChatWindow, self).__init__()
        self.setupUi(self)

        self.model = GroupChatClientModel()
        self.username = None

        # Client Connect
        self.username = self.model.connect()

        # Panggil function untuk start thread
        self.receive_function()

        # Jika list item di click
        self.input.returnPressed.connect(self.message_input)

    # Custom Functions
    def receive_function(self):
        self.thread = receive_message(self)
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
            self.message_list.append(str(self.username) + ': ' + str(message))
        
        # Send message ke server setelah diproses di client model
        self.model.group_chat(message)    

    
        

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatList()
    window.show() 
    app.exec_()