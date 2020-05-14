import os
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer


def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('dex', '123', os.path.abspath('../../static/files'), perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ('127.0.0.1', 8009)
    server = FTPServer(address, handler)

    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()
