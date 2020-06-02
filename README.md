# FP-Progjar-Kelompok-3

## Instalation
```bash
pip install -r requirements.txt
```
## Run
```bash
python manage.py runserver 8080
```
## Database mysql!
0. pip install mysqlclient 
1. ubah .env.example menjadi .env
2. isi env sesuai konfigurasi
3. buka phpmyadmin dari xampp, jalankan mysql
4. buatlah sebuah database dengan nama sesuai isi dari konfigurasi .env anda
5. jalankan query yang ada di db.sql kedalam database anda!

### Using FTPClient
1. ```cd GUI/FTPClient```
2. Jalankan ```python FTPServerModel.py```
3. Jalankan ```python app.py```
4. Input:
    * Host (default: 127.0.0.1)
    * Username (default: dex)
    * Password (default: 123)
    * Port (default 8009)
5. Optional - Ganti akun di FTPServerModel.py, parameter init


#### Register
1. ```python manage.py runserver``` pastikan sudah menjalankan dan mempersiapkan database mysql 
2. buka localhost. 
3. verifikasi email

#### Using Chat
1. ```python server.py```
2. jalankan ```cd GUI/FTPClient``` untuk membuka aplikasi
3. login


#### Fitur
* Drag and drop dari local filesystem ke remote
* Directory listing local
* Directory listing remote
* Delete, Download, Upload File remote
