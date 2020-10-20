# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The client program presents a command line interface with actions for the user.

import socket

# programState of 1 means the program is active.
programState = 1

# isConnected defines if the client is connected to the server.
isConnected = False

HOST = '127.0.0.1'  # The server's hostname or IP address.
PORT = 4000  # The port used by the server.


# Function for displaying the option menu when appropriate.
def displayMenu():
    print("\nChoose an option for the client:\n")
    print("1 - (Connect)    Connect to the server.")
    print("2 - (List)       List files stored at the server.")
    print("3 - (Retrieve)   Retrieve a file from the server.")
    print("4 - (Store)      Store a file from the client to the server.")
    print("5 - (Quit)       Terminate the connection with the server.")
    print("6 - (Close)      Close the FTP Server program")


# Display the options during startup.
displayMenu()

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
        if option <= 0 or option >= 7:
            print("Please choose a number between 1 through 6.")

        # If option 1 is selected, connect to a server.
        if option == 1:
            if isConnected:
                print("You are already connected to the server.")

            if not isConnected:
                print("Connecting to server...")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                isConnected = True

        # If option 2 is selected, list files stored at the server.
        if option == 2:
            if not isConnected:
                print("Please connect to the server.")
            else:
                print("Listing contents of current directory...\n")
                s.sendall('2'.encode())

                data = s.recv(1024).decode()

                print(data)

        # If option 3 is selected, download (retrieve) a file from the server.
        if option == 3:
            if not isConnected:
                print("Please connect to the server.")
            else:
                print("\nWhat file would you like to retrieve?\n")
                s.sendall('3'.encode())

                data = s.recv(1024).decode()

                print(data)

        # If option 4 is selected, upload (store) a file from the client to the server.
        if option == 4:
            if not isConnected:
                print("Please connect to the server.")
            else:
                print("Sending file to the server...\n")
                s.sendall('4'.encode())

                data = s.recv(1024).decode()

                print('Received', repr(data))

        # If option 5 is selected, terminate the connection to the server.
        if option == 5:
            if not isConnected:
                print("Please connect to the server.")
            else:
                isConnected = False

                print("Terminating client and server connection...\n")
                s.sendall('5'.encode())

                data = s.recv(0).decode()
                s.close()

                print('Received', repr(data))

        if option == 6:
            programState = 2

            if programState == 2:
                print('Would you like to close the FTP Server program?')
                closeConfirm = input("\nEnter Y or N: ")

                if not isConnected:
                    if closeConfirm == 'Y':
                        print("Closing the FTP Server program...")

                        programState = 0
                    if closeConfirm == 'N':
                        displayMenu()
                        programState = 1
                else:
                    if closeConfirm == 'Y':
                        print('\nPlease use option 5 to disconnect from server first.')
                        displayMenu()

                        programState = 1
                    if closeConfirm == 'N':
                        displayMenu()
                        programState = 1

# programState of 0 means the program will shutdown.
if programState == 0:
    exit()
