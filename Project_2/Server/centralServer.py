from threading import Thread
import sys
import socket
import os
import sys
from ftplib import FTP
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

HOST = socket.gethostname()

def beginConnect():

        user = DummyAuthorizer()
        user.add_anonymous(os.getcwd())
        user.add_user('', '', '.')
        handler = FTPHandler
        handler.authorizer = user

        server = FTPServer(("", 4488), handler)
        server.max_cons = 256
        server.max_cons_per_ip = 5
        server.serve_forever()
