# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin, Kevin Rufino
# Date of Submission: December 16, 2020

# The centralServer program begins the connection with user for the central server.

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

def main():

        user = DummyAuthorizer()
        user.add_anonymous("/Project_2/Host", 'elradfmwMT')
        user.add_user('', '', '/Project_2/Host', 'elradfmwMT')
        handler = FTPHandler
        handler.authorizer = user

        server = FTPServer(("", 4488), handler)
        server.max_cons = 256
        server.max_cons_per_ip = 5
        server.serve_forever()

if __name__ == '__main__':
    try:
        Thread(target=main).start()
    except:
        exit(0)
