# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski
# Date of Submission: December 16, 2020

# The hostServer program begins the connection with user for the host.

import os
import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# The socket's hostname or IP address.
HOST = socket.gethostname()


# Allows connection to the central server using specified information.
def beginConnect(value):
    user = DummyAuthorizer()
    user.add_anonymous(os.getcwd())
    user.add_user('', '', '.')
    handler = FTPHandler
    handler.authorizer = user

    server = FTPServer(("", value), handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()
