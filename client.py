# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The client program presents a command line interface with actions for the user.

import socket

# programState of 1 means the program is active.
programState = 1

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4000  # The port used by the server

# Displays the client options for the user.
print("\nChoose an option for the client:\n")
print("1 - (Connect)    Connect to the server.")
print("2 - (List)       List files stored at the server.")
print("3 - (Retrieve)   Retrieve a file from the server.")
print("4 - (Store)      Store a file from the client to the server.")
print("5 - (Quit)       Terminate the connection with the server.")

while programState == 1:
    # Displays a prompt for the user to input their choice.
    option = input("\nEnter a number: ")

    # If the input is not a number or too long, warn the user.
    if not option.isdigit() or len(option) >= 2:
        print("Please choose a number between 1 through 5.")

    # If the input is a number, convert it to type integer.
    if option.isdigit() and len(option) == 1:
        option = int(option)

    # If the input is an integer, continue to the next step.
    if isinstance(option, int):

        # If the integer is not an available choice, warn the user.
        if option <= 0 or option >= 6:
            print("Please choose a number between 1 through 5.")

        # If option 1 is selected, connect to a server.
        if option == 1:
            print("Connecting to server...\n")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b'You have connected to the server!')

                data = s.recv(1024)

            print('Received', repr(data))

        # If option 2 is selected, list files stored at the server.
        if option == 2:
            print("Listing contents of current directory...\n")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b'You have displayed the contents of the current directory!')

                data = s.recv(1024)

            print('Received', repr(data))

        # If option 3 is selected, download (retrieve) a file from the server.
        if option == 3:
            print("Retrieving file from the server...\n")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b'You have received a file from the server!')

                data = s.recv(1024)

            print('Received', repr(data))

        # If option 4 is selected, upload (store) a file from the client to the server.
        if option == 4:
            print("Sending file to the server...\n")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b'You have sent a file to the server!')

                data = s.recv(1024)

            print('Received', repr(data))

        # If option 5 is selected, terminate the connection to the server.
        if option == 5:
            programState = 0

            print("Terminating client and server programs...\n")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b'You have terminated the client and server!')

                data = s.recv(0)
                s.close()

            print('Received', repr(data))

# programState of 0 means the program will shutdown.
if programState == 0:
    exit()
