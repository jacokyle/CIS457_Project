# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The client program presents a command menu with actions for the user.

import socket

# programState initializes at normal, changes depending on actions.
programState = "normal"

# isConnected defines if the client is connected to the server.
isConnected = False

HOST = '127.0.0.1'  # The server's hostname or IP address.
PORT = 4000  # The port used by the server.


# Function for displaying the option menu for the client.
def displayMenuClient():
    print("\nChoose an option for the client:\n")

    print("1 - (Connect)    Connect to the server.")
    print("6 - (Close)      Close the client program.")


# Function for displaying the option menu for the server.
def displayMenuServer():
    print("\nChoose an option for the client and server:\n")

    print("2 - (List)       List files stored at the server.")
    print("3 - (Retrieve)   Retrieve a file from the server.")
    print("4 - (Store)      Store a file from the client to the server.")
    print("5 - (Quit)       Terminate the connection with the server.")
    print("6 - (Close)      Close the client and server program.")


# Display the options menu during startup.
displayMenuClient()

# While the programState is normal, perform basic actions.
while programState == "normal":
    # Displays a prompt for the user to input their choice.
    option = input("\nEnter a number: ").strip()

    # If the input is not a number or too long, warn the user.
    if not option.isdigit() or len(option) >= 2:
        if isConnected:
            print("Please choose a number between 2 through 6.")
        else:
            print("Please choose 1 or 6.")

    # If the input is a number, convert it to type integer.
    if option.isdigit() and len(option) == 1:
        option = int(option)

    # If the input is an integer, continue to the next step.
    if isinstance(option, int):

        # Warn the user what options are available based on which menu is displayed..
        if isConnected:
            if option <= 1 or option >= 7:
                print("Please choose a number between 2 through 6.")
        else:
            if option != 1 and option != 6:
                print("Please choose 1 or 6.")

        # If option 1 is selected, connect to a server.
        if option == 1:

            # Connect the client to the server.
            if not isConnected:
                print("Connecting to the server...")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                isConnected = True

                displayMenuServer()

        # If option 2 is selected, list files stored at the server.
        if option == 2:

            # List all files in the server directory.
            if isConnected:
                print("Listing contents of current directory...\n")
                s.sendall('2'.encode())

                data = s.recv(1024).decode()

                print(data)

        # If option 3 is selected, download (retrieve) a file from the server.
        if option == 3:
            programState = "retrieveFile"

            # Enter the retrieveFile state.
            while programState == "retrieveFile":
                print("What file would you like to retrieve?")

                retrieveFileInput = input("\nEnter a file to retrieve from the server: ").strip()

                # Retrieve a specified file from the server for the client.
                if isConnected:
                    s.sendall('2'.encode())
                    s.sendall('3'.encode())

                    data = s.recv(1024).decode()

                    # Notifies the user when a file has been retrieved.
                    if data.__contains__(retrieveFileInput):
                        print("You have retrieved the file: ", retrieveFileInput)

                        programState = "normal"
                    else:
                        print("IMPORTANT: The file does not exist in the directory.\n")

        # If option 4 is selected, upload (store) a file from the client to the server.
        if option == 4:
            programState = "sendFile"

            # Enter the sendFile state.
            while programState == "sendFile":
                print("What file would you like to send?")

                sendFileInput = input("\nEnter a filename to send to the server: ").strip()

                # Send a specified file to the server from the client.
                if isConnected:
                    s.sendall('2'.encode())
                    s.sendall('3'.encode())

                    data = s.recv(1024).decode()

                    # Notifies the user when a file has been sent.
                    if data.__contains__(sendFileInput):
                        print("You have sent the file: ", sendFileInput)

                        programState = "normal"
                    else:
                        print("IMPORTANT: The file does not exist in the directory.\n")

        # If option 5 is selected, terminate (quit) the connection to the server.
        if option == 5:

            # Terminate the connection between the client and server.
            if isConnected:
                # Label the client disconnected from server.
                isConnected = False

                print("Terminating client and server connection...")
                s.sendall('5'.encode())

                data = s.recv(0).decode()
                s.close()

                displayMenuClient()

        # If option 6 is selected, a close interface will be displayed for the client.
        if option == 6:
            # closeMenu will display the close menu.
            programState = "closeMenu"

            # While the programState is in the close menu, ask the user to confirm.
            while programState == "closeMenu":

                # Confirm with the user that they would like to close the program.
                if not isConnected:
                    print('Would you like to close the client program?')
                else:
                    print('Would you like to close the client and server program?')

                closeConfirm = input("\nEnter Y or N: ").upper().strip()

                # Checks if the input is Y or N, which continues closing function.
                if closeConfirm == 'Y' or closeConfirm == 'N':

                    # Conducts close operations when server connection does not exist.
                    if not isConnected:

                        # If the user says yes, close the entire program.
                        if closeConfirm == 'Y':
                            # Notify to the user the program is closing.
                            print("Closing the client program...")

                            # Set the program to exit.
                            programState = "exit"

                        # If the user says no, redisplay the options menu and set back to active.
                        if closeConfirm == 'N':
                            # Redisplay the options menu.
                            displayMenuClient()

                            # Set the program back to normal.
                            programState = "normal"

                    # Conducts close operations when server connection does exist.
                    else:

                        # If the user says yes, warn the user to end the connection with server first.
                        if closeConfirm == 'Y':
                            # Label the client disconnected from server.
                            isConnected = False

                            # Notify to the user the program is closing.
                            print("Closing client and server programs...")
                            s.sendall('6'.encode())

                            data = s.recv(0).decode()
                            s.close()

                            # Set the program to exit.
                            programState = "exit"

                        # If the user says no, redisplay the options menu and set back to active.
                        if closeConfirm == 'N':
                            # Redisplay the options menu.
                            displayMenuServer()

                            # Set the program back to normal.
                            programState = "normal"

                # Checks if the input is not Y or N, otherwise warn the user.
                else:
                    print("\nIMPORTANT: Please choose Y or N.")

# While the programState is exit, shutdown the programs.
if programState == "exit":
    exit()
