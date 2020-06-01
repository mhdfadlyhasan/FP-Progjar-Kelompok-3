from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.GroupChat import Ui_group_chat_window
from view.PersonalChat import Ui_personal_chat_window
from view.ChatList import Ui_ChatList
from view.login import Ui_Login
from model.GroupChatClientModel import GroupChatClientModel

import time

# Only needed for access to command line arguments
import sys
import io
import signal

# Subclass QMainWindow to customise your application's main window

username = None
isConnected = False
connection = GroupChatClientModel()

class login(QMainWindow, Ui_Login):

    username_value = None
    password_value = None

    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)

        # Detect input
        self.login.clicked.connect(self.login_clicked)

    def login_clicked(self):
        self.username_value = self.username.text()
        self.password_value = self.password.text()
        if self.username_value != None and self.password_value != None:
            connection.send_login(self.username_value, self.password_value)
            self.chatlist = ChatList(connection)
            self.chatlist.show()
            self.hide()

class ChatList(QMainWindow, Ui_ChatList):

    def __init__(self,connection):
        super(ChatList, self).__init__()
        self.setupUi(self)
        # Panggil function untuk start thread
        self.client_run(connection)
        
        connection.server.send(("<roomlist> " + connection.your_id).encode())
        print("sending all room details!!!")
        message = connection.server.recv(2048).decode()
        count = message.count(',')
        print(count)

        # List for roomlist
        split = message.split(',')

        for room in split:
            # Add item
            if room != '':
                item = QListWidgetItem()
                item.setText(room)
                self.chat_list.addItem(item)

        # Listener click list widget item
        self.chat_list.itemClicked.connect(self.item_click)

        # Listener click Personal chat
        self.personal_chat.clicked.connect(self.personal_chat_click)

        # Listener click create group
        self.create_group.clicked.connect(self.create_group_click)

    # Custom Functions
    def client_run(self,connection):
        self.thread = client_thread(self)
        self.thread.start()

    def item_click(self):
        roomname = self.chat_list.currentItem().text()
        if(not roomname == "Empty!"): 
            print(roomname)
            chat_room_sekarang = roomname[13:-1]
            connection.current_chat_room = chat_room_sekarang
            self.chat = GroupChatWindow(chat_room_sekarang)#ini harusnya diisi dengan nilai room yang barusan di click
            self.chat.show()
    
    def personal_chat_click(self):
        message, result = QInputDialog.getText(self, 'Personal Chat', 'Please enter the user\'s ID that will be invited:')
        if result is True:
            message = '<createpersonal>,' + message
            sys.stdin = io.StringIO(message)
            print(message)
            time.sleep(1)

            # pass room ID here
            print(connection.current_chat_room)
            self.personal_chat = PersonalChatWindow(connection.current_chat_room)
            self.personal_chat.show()

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
        print("main thread killed!")

class client_thread_get(QThread):
    
    global username
    connected = False
    object_gui = ""
    room_id=""
    def __init__(self, connection,object_gui,room_id):
        self.object_gui = object_gui
        self.room_id = room_id
        super(client_thread_get, self).__init__()
        print('start new get thread!')
        
    def run(self):
        while self.object_gui.running:
            try:
                connection.group_chat_get_message(self.object_gui,self.room_id)#ini juga harus disamaain id room sekarang
            except:
                print("closing get thread! somethings wrong!")
                break
        else:
            print("thread closed!")
        
            
class GroupChatWindow(QMainWindow, Ui_group_chat_window):

    def __init__(self,room_id):
        super(GroupChatWindow, self).__init__()
        self.running = True
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

        # Listener click list widget item
        self.invite.clicked.connect(self.invite_click)

        # nambah thread disini
        self.client_run(connection,self,room_id)

    def client_run(self,connection,object_gui,room_id):
        self.thread = client_thread_get(connection,object_gui,room_id)
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

    def invite_click(self):
        message, result = QInputDialog.getText(self, 'Invite Person', "Please enter the person's ID:")
        if result == True:
            message = '<invite> ' + message
            sys.stdin = io.StringIO(message)
            print(message)

    def closeEvent(self, event):
        # do stuff
        if True:
            print("window closed!")
            self.running = False
            event.accept() # let the window close
        else:
            event.ignore()

# testing: PersonalChatWindow.  
class PersonalChatWindow(QMainWindow, Ui_personal_chat_window):

    def __init__(self, room_id):
        super(PersonalChatWindow, self).__init__()
        self.running = True
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

        # Listener click list widget item
        # self.invite.clicked.connect(self.invite_click)

        # nambah thread disini
        self.client_run(connection,self,room_id)

    def client_run(self,connection,object_gui,room_id):
        self.thread = client_thread_get(connection,object_gui,room_id)
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

    # def invite_click(self):
    #     message, result = QInputDialog.getText(self, 'Invite Person', "Please enter the person's ID:")
    #     if result == True:
    #         message = '<invite> ' + message
    #         sys.stdin = io.StringIO(message)
    #         print(message)

    def closeEvent(self, event):
        # do stuff
        if True:
            print("window closed!")
            self.running = False
            event.accept() # let the window close
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login()
    # window = ChatList(connection)
    window.show()
    app.exec_()