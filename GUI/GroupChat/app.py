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
isConnected = False

class ChatList(QMainWindow, Ui_ChatList):

    def __init__(self,connection):
        super(ChatList, self).__init__()
        self.setupUi(self)
        # Panggil function untuk start thread
        self.client_run(connection)
        
        # Listener click list widget item
        self.chat_list.itemActivated.connect(self.item_click)

        # Listener click create group
        self.create_group.clicked.connect(self.create_group_click)

    # Custom Functions
    def client_run(self,connection):
        self.thread = client_thread(self)
        self.thread.start()

    def item_click(self):
        self.chat = GroupChatWindow('1')#ini harusnya diisi dengan nilai room yang barusan di click
        self.chat.show()

    def create_group_click(self):
        message, result = QInputDialog.getText(self, 'Room Name', 'Please enter the room name:')
        if result == True:
            message = '<create>,' + message
            sys.stdin = io.StringIO(message)
            print(message)

# Untuk thread client
class client_thread(QThread):

    global username
    connected = False

    def __init__(self, connection):
        super(client_thread, self).__init__()
        print('Client running args' + str(connection))
        
    def run(self):
        while True:
            connection.group_chat()

class client_thread_get(QThread):

    global username
    connected = False
    object_gui = ""
    def __init__(self, connection,object_gui):
        self.object_gui = object_gui
        super(client_thread_get, self).__init__()
        print('Client_get')
        
    def run(self):
        while True:
            connection.group_chat_get_message(1,self.object_gui)#ini juga harus disamaain id room sekarang
            
class GroupChatWindow(QMainWindow, Ui_group_chat_window):

    def __init__(self,room_id):
        super(GroupChatWindow, self).__init__()
        self.setupUi(self)
        print(room_id)
        # When enter is clicked
        self.input.returnPressed.connect(self.message_input)
        
        #get message from db put to message_list, untuk nampilin history chat!
        print("sending!")
        connection.server.send(("<history> " + room_id).encode())
        print("sended!!")
        message = connection.server.recv(2048).decode()
        self.message_list.append(message)

        #maybe nambah thread disini idk :/
        self.client_run(connection,self)

    def client_run(self,connection,object_gui):
        self.thread = client_thread_get(connection,object_gui)
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
            self.message_list.append(str(connection.username) + ': ' + str(message))
        
        # Send message ke thread client
        sys.stdin = io.StringIO(message) 

        # model.stdinprint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    connection = GroupChatClientModel()
    window = ChatList(connection)
    window.show()
    app.exec_()