# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The server program binds to a port and listens to requests from a client.

import os
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 4000  # Port to listen on (non-privileged ports are > 1023)


# Displays the list of files in the directory for the client.
def listFiles(connection):
    directory = os.getcwd()
    fileList = os.listdir(directory)
    message = 'Current Directory:\n'
    message += '\n'.join(fileList)
    connection.sendall(message.encode())


def retrieveFile():
    print("Needs work.")
    # Needs work.


def sendFile():
    print("Needs work.")
    # Needs work.


# Builds the connection with the client and responds to selected options.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()

            # When the client does not send any data, break from the client.
            if not data:
                break

            # When client chooses to list files, list the files in the current directory.
            if data == '2':
                listFiles(conn)

            # When client chooses to retrieve a file, send the file to the client.
            if data == '3':
                continue  # This needs a function for retrieving files.

            # When client chooses to send a file, accept the file from the client.
            if data == '4':
                continue  # This needs a function for sending files.

            # When client chooses to quit the connection, close the server.
            if data == '5':
                conn.close()
                exit()
