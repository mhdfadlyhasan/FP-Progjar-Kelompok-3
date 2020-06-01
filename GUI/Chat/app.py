from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view.GroupChat import Ui_group_chat_window
from view.ChatList import Ui_ChatList
from view.login import Ui_Login
from model.GroupChatClientModel import GroupChatClientModel

# Only needed for access to command line arguments
import sys
import io
import signal
import time

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
        self.password.setEchoMode(QLineEdit.Password)
        # Detect input
        self.login.clicked.connect(self.login_clicked)

    def login_clicked(self):
        self.username_value = self.username.text()
        self.password_value = self.password.text()
        if self.username_value != None and self.password_value != None:
            connection.send_login(self.username_value, self.password_value)

            connected = connection.server.recv(2048).decode()
            print(connected)
            if connected == '1':
                print('connected')
                self.chatlist = ChatList(connection)
                self.chatlist.show()
                self.hide()
            else:
                message = QMessageBox()
                message.setWindowTitle('Login Failed')
                message.setText('Incorrect username or password')
                message.setIcon(QMessageBox.Critical)
                message.exec_()

class ChatList(QMainWindow, Ui_ChatList):

    connection = None

    def __init__(self,connection):
        super(ChatList, self).__init__()
        self.connection = connection
        self.setup_ui(self.connection)

    def setup_ui(self,connection):
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

        # Listener click create group
        self.create_group.clicked.connect(self.create_group_click)

    # Custom Functions
    def client_run(self,connection):
        self.thread = client_thread(self)
        self.thread.start()

    def item_click(self):
        roomname = self.chat_list.currentItem().text()
        if(not roomname == "Empty!"): 
            index = roomname.find('.')
            print(index)
            chat_room_sekarang = roomname[:index]
            connection.current_chat_room = chat_room_sekarang
            self.chat = GroupChatWindow(chat_room_sekarang)#ini harusnya diisi dengan nilai room yang barusan di click
            self.chat.show()
        
    def create_group_click(self):
        message, result = QInputDialog.getText(self, 'Room Name', 'Please enter the room name:')
        if result == True:
            message = '<create>,' + message
            sys.stdin = io.StringIO(message)

            time.sleep(1)
            # Recreate UI
            self.setup_ui(self.connection)

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
        print(str(room_id) + "this is room id")
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login()
    # window = ChatList(connection)
    window.show()
    app.exec_()