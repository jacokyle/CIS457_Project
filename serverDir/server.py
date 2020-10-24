# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kevin Rufino, Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The server program binds to a port and listens to requests from a client.

import os
import socket

HOST = socket.gethostname()  # The socket's hostname or IP address.
PORT = 5000  # The port used by the socket.


# Displays the list of files in the server directory.
def listFiles(connection):
    directory = os.getcwd()
    fileList = os.listdir(directory)
    message = '\n'.join(fileList)
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

    # Initializes the connection with the client.
    conn, addr = s.accept()

    with conn:
        while True:
            # Decodes the client information for the server.
            data = conn.recv(1024).decode()

            # Continue listening to future connections.
            if not data:
                conn, addr = s.accept()

            # Print whenever a client has connected to the server.
            if data == '1':
                print('Connected by:', addr)

            # When client chooses to list files, list the files in the current directory.
            if data == '2':
                print('Listed files for:', addr)
                listFiles(conn)

            # TODO: We need to find out how to send a file to the client.
            # When client chooses to retrieve a file, send the file to the client.
            if data == '3':
                print('Sent a file to:', addr)

            # TODO: We need to find out how to retrieve a file from the client.
            # When client chooses to send a file, accept the file from the client.
            if data == '4':
                print('Received a file from:', addr)

            # When client chooses to close the program, shutdown the server.
            if data == '5':
                print('Disconnected from:', addr)

            # When client chooses to close the program, shutdown the server.
            if data == '6':
                print('Shutting down server...')
                conn.close()
                exit()

