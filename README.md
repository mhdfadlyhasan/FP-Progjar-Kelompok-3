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
0. pip install mysqlclient / kalau python 3.8 pip install mysqlclient-1.4.2-cp38-cp38m-win_amd64.whl
1. ubah .env.example menjadi .env
2. isi env sesuai konfigurasi
3. buka phpmyadmin dari xampp, jalankan mysql
4. buatlah sebuah database sesuai isi dari konfigurasi .env anda
5. python manage.py migrate
6. buka database, import 'db.sql' ke dalam database anda