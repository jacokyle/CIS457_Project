# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The server program binds to a port and listens to requests from a client.

import os
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 4000  # Port to listen on (non-privileged ports are > 1023)


def listFiles(connection):
    directory = os.getcwd()
    fileList = os.listdir(directory)
    message = 'Current Directory:\n'
    message += '\n'.join(fileList)
    connection.sendall(message.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            if data == '2':
                listFiles(conn)
            if data == '3':
                continue  # This needs a function for retrieving files.
            if data == '4':
                continue  # This needs a function for sending files.
            if data == '5':
                conn.close()
                exit()
