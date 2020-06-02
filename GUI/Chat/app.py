from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from view.Chat import Ui_chat_window
from view.ChatList import Ui_ChatList
from view.login import Ui_Login
from view.MemberList import Ui_member
from model.ChatClientModel import ChatClientModel

from FTPClient.app import MainWindow as FTPClient

# Only needed for access to command line arguments
import sys
import io
import time

# Subclass QMainWindow to customise your application's main window

username = None
isConnected = False
connection = ChatClientModel()


# Window untuk login
class login(QMainWindow, Ui_Login):
    # Value awal username dan password
    username_value = ''
    password_value = ''

    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        self.actionExit.triggered.connect(qApp.quit)
        self.actionLaunchFTP.triggered.connect(self.launch_ftp)
        self.ftp = FTPClient()
        # Password hidden
        self.password.setEchoMode(QLineEdit.Password)

        # Listener login button
        self.login.clicked.connect(self.login_clicked)

    def launch_ftp(self):
        self.ftp.show()


    # Function login button
    def login_clicked(self):

        # Memasukkan username dan password yang sudah diisikan
        self.username_value = self.username.text()
        self.password_value = self.password.text()

        # Jika username dan password tidak kosong
        if self.username_value != '' and self.password_value != '':

            # Mengirim data ke client
            connection.send_login(self.username_value, self.password_value)

            # Menerima response dari server
            connected = connection.server.recv(2048).decode()

            # Jika username dan password benar
            if connected == '1':
                print('Login Successful')
                self.chatlist = ChatList(connection)
                self.chatlist.show()
                self.hide()

            # Jika username atau password salah
            else:
                message = QMessageBox()
                message.setWindowTitle('Login Failed')
                message.setText('Incorrect username or password')
                message.setIcon(QMessageBox.Critical)
                message.exec_()

        # Jika salah satu data kosong
        else:
            message = QMessageBox()
            message.setWindowTitle('Login Failed')
            message.setText('Username and Password must be filled')
            message.setIcon(QMessageBox.Critical)
            message.exec_()


# Window untuk chatlist
class ChatList(QMainWindow, Ui_ChatList):
    connection = None

    def __init__(self, connection):
        super(ChatList, self).__init__()
        self.connection = connection
        self.setup_ui(self.connection)

    def setup_ui(self, connection):
        self.setupUi(self)

        # Panggil function untuk start running client thread
        self.client_run(connection)

        # Mengambil roomlist user
        connection.server.send(("<roomlist> " + connection.your_id).encode())
        print("Getting Room list")
        message = connection.server.recv(2048).decode()

        # List untuk roomlist
        split = message.split(',')
        for room in split:
            if room != '':
                item = QListWidgetItem()
                item.setText(room)
                self.chat_list.addItem(item)

        # Listener click item di list widget 
        self.chat_list.itemClicked.connect(self.item_click)

        # Listener click personal chat button
        self.personal_chat.clicked.connect(self.personal_chat_click)

        # Listener click create group button
        self.create_group.clicked.connect(self.create_group_click)

        # Listener click refresh button
        self.refresh.clicked.connect(self.refresh_click)

    # Function run untuk client thread
    def client_run(self, connection):
        self.thread = client_thread(self)
        self.thread.start()

    # Function klik pada item di list
    def item_click(self):
        roomname = self.chat_list.currentItem().text()

        # Jika sudah ada chat sebelumnya
        if (not roomname == "Empty!"):
            index = roomname.find('.')
            chat_room_sekarang = roomname[:index]
            connection.current_chat_room = chat_room_sekarang

            # Membuka chat window sesuai dengan index item yang diklik
            self.chat = ChatWindow(chat_room_sekarang)
            self.chat.show()

    # Function personal chat button
    def personal_chat_click(self):
        # Meminta input dari user
        message, result = QInputDialog.getText(self, 'Personal Chat',
                                               'Please enter the user\'s ID that will be invited:')
        if result is True:
            message = '<createpersonal>,' + message
            sys.stdin = io.StringIO(message)
            time.sleep(1)

            # Recreate UI
            self.setup_ui(self.connection)

    # Function create group button
    def create_group_click(self):
        # Meminta input dari user
        message, result = QInputDialog.getText(self, 'Room Name', 'Please enter the room name:')
        if result == True:
            message = '<create>,' + message
            sys.stdin = io.StringIO(message)
            time.sleep(1)

            # Recreate UI
            self.setup_ui(self.connection)

    # Function refresh button
    def refresh_click(self):
        time.sleep(1)

        # Recreate UI
        self.setup_ui(self.connection)


# Untuk thread client
class client_thread(QThread):
    global username
    connected = False

    def __init__(self, connection):
        super(client_thread, self).__init__()
        print('Client Running')

    def run(self):
        while True:
            connection.chat()
        print("Main thread killed!")


# Untuk menjalankan thread get dari client thread
class client_thread_get(QThread):
    global username
    connected = False
    object_gui = ""
    room_id = ""

    def __init__(self, connection, object_gui, room_id):
        self.object_gui = object_gui
        self.room_id = room_id
        super(client_thread_get, self).__init__()
        print('Starting a new get thread!')

    def run(self):
        while self.object_gui.running:
            try:
                connection.chat_get_message(self.object_gui, self.room_id)
            except:
                print("Closing get thread! Error occurred!")
                break
        else:
            print("Thread closed!")


# Window untuk chat
class ChatWindow(QMainWindow, Ui_chat_window):
    room_id = ''

    def __init__(self, room_id):
        super(ChatWindow, self).__init__()
        self.running = True
        self.setupUi(self)
        self.room_id = room_id

        # Menampilkan history chat
        connection.server.send(("<history> " + self.room_id).encode())
        print("Getting chat history")
        message = connection.server.recv(2048).decode()
        self.message_list.append(message)

        # Saat user melakukan klik enter untuk mengirim message
        self.input.returnPressed.connect(self.message_input)

        # Listener click invite
        self.invite.clicked.connect(self.invite_click)

        # Listener click member
        self.show_member.clicked.connect(self.member_click)

        # Untuk memanggil function menjalankan thread get di client
        self.client_run(connection, self, room_id)

    # Function menjalankan thread get
    def client_run(self, connection, object_gui, room_id):
        self.thread = client_thread_get(connection, object_gui, room_id)
        self.thread.start()

    # Function untuk mengambil input dari user
    def message_input(self):

        # Mengambil input dari GUI
        message = self.input.text()
        self.input.clear()

        # Print input user di message list
        if (message[0] == '<'):
            pass
        else:
            self.message_list.append(str(connection.username) + ':' + str(message))

        # Send message ke thread client
        sys.stdin = io.StringIO(message)

        # Function invite button

    def invite_click(self):
        message, result = QInputDialog.getText(self, 'Invite Person', "Please enter the person's ID:")
        if result == True:
            message = '<invite> ' + message
            sys.stdin = io.StringIO(message)

    # Function member button
    def member_click(self):
        message = '<member> ' + self.room_id
        sys.stdin = io.StringIO(message)
        response = connection.server.recv(2048).decode()

        # List untuk roomlist
        split = response.split(',')

        # Panggil Member Window
        self.member_window = MemberWindow(split)
        self.member_window.show()

    # Close Window Chat
    def closeEvent(self, event):
        if True:
            time.sleep(0.2)
            print("Chat window closed!")
            self.running = False
            event.accept()

        else:
            event.ignore()


# Untuk window menampilkan member
class MemberWindow(QMainWindow, Ui_member):
    def __init__(self, split):
        super(MemberWindow, self).__init__()
        self.setupUi(self)

        # Menambahkan nama member di list widget
        for member in split:
            if member != '':
                item = QListWidgetItem()
                item.setText(member)
                self.member_list.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec_()
