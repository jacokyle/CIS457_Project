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
    print("6 - (Close)      Close the FTP Server program.")


# Display the options menu during startup.
displayMenu()

# While the programState is active, perform basic actions.
while programState == 1:
    # Displays a prompt for the user to input their choice.
    option = input("\nEnter a number: ").strip()

    # If the input is not a number or too long, warn the user.
    if not option.isdigit() or len(option) >= 2:
        print("Please choose a number between 1 through 6.")

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

            # Notify the user that they are already connected to the server.
            if isConnected:
                print("You are already connected to the server.")

            # Connect the client to the server.
            if not isConnected:
                print("Connecting to the server...")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                isConnected = True

        # If option 2 is selected, list files stored at the server.
        if option == 2:

            # Notify the user that they need to connect to server first.
            if not isConnected:
                print("Please connect to the server.")

            # List all files in the server directory.
            else:
                print("Listing contents of current directory...\n")
                s.sendall('2'.encode())

                data = s.recv(1024).decode()

                print(data)

        # If option 3 is selected, download (retrieve) a file from the server.
        if option == 3:

            # Notify the user that they need to connect to server first.
            if not isConnected:
                print("Please connect to the server.")

            # Retrieve a specified file from the server for the client.
            else:
                print("What file would you like to retrieve?\n")
                s.sendall('3'.encode())

                data = s.recv(1024).decode()

                print(data)

        # If option 4 is selected, upload (store) a file from the client to the server.
        if option == 4:

            # Notify the user that they need to connect to server first.
            if not isConnected:
                print("Please connect to the server.")

            # Send a specified file from the client to the server.
            else:
                print("Sending file to the server...\n")
                s.sendall('4'.encode())

                data = s.recv(1024).decode()

                print('Received', repr(data))

        # If option 5 is selected, terminate (quit) the connection to the server.
        if option == 5:

            # Notify the user that they need to connect to server first.
            if not isConnected:
                print("Please connect to the server.")

            # Terminate the connection between the client and server.
            else:
                # Label the client disconnected from server.
                isConnected = False

                print("Terminating client and server connection...")
                s.sendall('5'.encode())

                data = s.recv(0).decode()
                s.close()

        # If option 6 is selected, a close interface will be displayed for the client.
        if option == 6:
            # programState of 2 means the program is in the close menu.
            programState = 2

            # While the programState is in the close menu, ask the user to confirm.
            while programState == 2:
                # Confirm with the user that they would like to close the program.
                print('Would you like to close the FTP Server program?')
                closeConfirm = input("\nEnter Y or N: ").upper().strip()

                # Checks if the input is Y or N, which continues closing function.
                if closeConfirm == 'Y' or closeConfirm == 'N':

                    # Conducts close operations when server connection does not exist.
                    if not isConnected:

                        # If the user says yes, close the entire program.
                        if closeConfirm == 'Y':
                            # Notify to the user the program is closing.
                            print("Closing the FTP Server program...")

                            # Set the program to close.
                            programState = 0

                        # If the user says no, redisplay the options menu and set back to active.
                        if closeConfirm == 'N':
                            # Redisplay the options menu.
                            displayMenu()

                            # Set the program back to active.
                            programState = 1

                    # Conducts close operations when server connection does exist.
                    else:

                        # If the user says yes, warn the user to end the connection with server first.
                        if closeConfirm == 'Y':
                            # Label the client disconnected from server.
                            isConnected = False

                            # Notify to the user the program is closing.
                            print("Closing FTP Server program...")
                            s.sendall('6'.encode())

                            data = s.recv(0).decode()
                            s.close()

                            # Set the program back to active.
                            programState = 0

                        # If the user says no, redisplay the options menu and set back to active.
                        if closeConfirm == 'N':
                            # Redisplay the options menu.
                            displayMenu()

                            # Set the program back to active.
                            programState = 1

                # Checks if the input is not Y or N, otherwise warn the user.
                else:
                    print("\nIMPORTANT: Please choose Y or N.")

# While the programState is set to close, exit the program.
if programState == 0:
    exit()
