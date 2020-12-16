# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin, Kevin Rufino
# Date of Submission: December 16, 2020

# The centralServer program begins the connection with user for the central server.

import os
import socket
from threading import Thread
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# The socket's hostname or IP address.
HOST = socket.gethostname()


# Part of the main method for initializing the central server.
def main():
    user = DummyAuthorizer()
    user.add_anonymous(os.getcwd(), perm='elradfmwM')
    user.add_user('', '', '.', perm='elradfmwM')
    handler = FTPHandler
    handler.authorizer = user

    server = FTPServer(("", 4488), handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()


# Part of the main method for executing the central server.
if __name__ == '__main__':
    try:
        Thread(target=main).start()
    except:
        exit(0)
