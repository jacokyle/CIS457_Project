# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kevin Rufino, Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The server program binds to a port and listens to requests from a client.

import os
import socket

HOST = socket.gethostname()  # The socket's hostname or IP address.
PORT = 5000  # The port used by the socket.

# Initializes the filename for file retrieval and file sending.
fileName = " "


# Allow the server to engage in the send file action.
def sendFile():
    programState = "retrieveFile"

    while programState == "retrieveFile":

        # Displays the list of files in the client directory.
        global fileName
        serverFileList = os.listdir(os.getcwd())
        serverDir = '\n'.join(serverFileList)

        # Parse through each file in the list.
        for _ in serverDir:
            fileName = serverDir.splitlines()

        print("\nServer Directory Files:")
        print(serverDir)

        sendingFile = input(str("\nEnter a file to send to the client: "))

        if sendingFile in fileName and len(sendingFile) >= 1:
            fileSelection = open(sendingFile, "rb")
            fileData = fileSelection.read(1024)
            conn.send(fileData)

            print('\nSent a file to:', addr)
            programState = "normal"

        # Warn the user a file doesn't exist and try again.
        elif sendingFile not in fileName and len(sendingFile) >= 1:
            print("\nIMPORTANT: The file does not exist in the directory.")
        # Refuse whitespace.
        else:
            print("\nIMPORTANT: Please input a filename.")


def retrieveFile():
    print()


# Displays the list of files in the server directory.
def listFiles(connection):
    directory = os.getcwd()
    fileList = os.listdir(directory)
    message = '\n'.join(fileList)
    connection.sendall(message.encode())
    print('Listed files for:', addr)


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
                listFiles(conn)

            # When client chooses to retrieve a file, send the file to the client.
            if data == '3':
                sendFile()

            # When client chooses to send a file, accept the file from the client.
            if data == '4':
                retrieveFile()

            # When client chooses to close the program, shutdown the server.
            if data == '5':
                print('Disconnected from:', addr)

            # When client chooses to close the program, shutdown the server.
            if data == '6':
                print('Shutting down server...')
                conn.close()
                exit()

