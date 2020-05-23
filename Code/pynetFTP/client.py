import os
from ftplib import FTP
from pathlib import Path
from pathlib import PurePath
from zipfile import ZipFile


class ClientFtp:
    def __init__(self):
        self.server = FTP()

    def connect(self):
        self.server.connect('127.0.0.1', 8009)
        self.server.login('dex', '123')

    def listdir(self, *args):
        list_res = []
        dirs = args[0]
        # Using mlsd not retrlines. Kalau mau buat callback di retrlines, terserah.
        dir_yield = self.server.mlsd(dirs, facts=['types', 'size', 'perm'])
        for path in dir_yield:
            abs_path = os.path.abspath(path[0])
            file_path = PurePath(abs_path).as_uri()
            print(file_path)
            list_res.append(file_path)
        return list_res

    # def download(self, *args):
    #     res = []
    #
    #     for arg in args:
    #         fname = f"{arg}"
    #         if Path(arg).is_dir():
    #             with ZipFile(arg) as z:
    #                 fname = f"{arg}.zip"
    #                 z.write(filename=fname)
    #
    #         p = PurePath(fname).as_uri()
    #         res.append(p)
    #     return res


if __name__ == '__main__':
    client = ClientFtp()
    client.connect()
    client.listdir('.')
