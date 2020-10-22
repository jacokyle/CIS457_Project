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

HOST = socket.gethostname()  # The server's hostname or IP address.
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


# Display the client menu during startup.
displayMenuClient()

# While the programState is normal, perform basic actions.
while programState == "normal":
    # Displays a prompt for the user to input their menu option.
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
        if not isConnected and option == 1:
            # Notify to the user the client has connected to the server.
            print("Connecting to the server...")

            # Create a socket that the client and server interact with.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))

            # Sets the client to connected with the server.
            isConnected = True

            # Return the user to the server menu.
            displayMenuServer()

        # If option 2 is selected, list files stored at the server.
        if isConnected and option == 2:
            # Notify to the user the server has listed the contents of the directory.
            print("Listing contents of current directory...\n")

            # Performs the directory listing function from the server.
            s.sendall('2'.encode())

            # Decodes the server information for the client.
            data = s.recv(1024).decode()

            # Print the list from the server.
            print(data)

            # Return the user to the server menu.
            displayMenuServer()

        # If option 3 is selected, download (retrieve) a file from the server.
        if isConnected and option == 3:
            programState = "retrieveFile"

            # Enter the retrieveFile state.
            while programState == "retrieveFile":
                print("What file would you like to retrieve?")

                # Displays a prompt for the user to input a file to retrieve.
                retrieveFileInput = input("\nEnter a file to retrieve from the server: ").strip()

                # Obtains the list from the server.
                s.sendall('2'.encode())

                # Performs the file retrieval function from the server.
                s.sendall('3'.encode())

                # Decodes the server information for the client.
                data = s.recv(1024).decode()

                # Notifies the user a file has been retrieved and returns the user to the server menu.
                if data.__contains__(retrieveFileInput) and len(retrieveFileInput) >= 1:
                    print("You have retrieved the file: ", retrieveFileInput)
                    programState = "normal"
                    displayMenuServer()
                # Warn the user a file doesn't exist and try again.
                elif not data.__contains__(retrieveFileInput) and len(retrieveFileInput) >= 1:
                    print("\nIMPORTANT: The file does not exist in the directory.")
                # Refuse whitespace.
                else:
                    print("\nIMPORTANT: Please input a filename.")

        # If option 4 is selected, upload (store) a file from the client to the server.
        if isConnected and option == 4:
            programState = "sendFile"

            # Enter the sendFile state.
            while programState == "sendFile":
                print("What file would you like to send?")

                # Displays a prompt for the user to input a file to send.
                sendFileInput = input("\nEnter a file to send to the server: ").strip()

                # Obtains the list from the server.
                s.sendall('2'.encode())

                # Performs the file sending function from the server.
                s.sendall('4'.encode())

                # Decodes the server information for the client.
                data = s.recv(1024).decode()

                # Notifies the user a file has been sent and returns the user to the server menu.
                if data.__contains__(sendFileInput) and len(sendFileInput) >= 1:
                    print("You have sent the file: ", sendFileInput)
                    programState = "normal"
                    displayMenuServer()
                # Warn the user a file doesn't exist and try again.
                elif not data.__contains__(sendFileInput) and len(sendFileInput) >= 1:
                    print("\nIMPORTANT: The file does not exist in the directory.")
                # Refuse whitespace.
                else:
                    print("\nIMPORTANT: Please input a filename.")

        # If option 5 is selected, terminate (quit) the connection to the server.
        if isConnected and option == 5:
            # Notify to the user the connection between client and server has terminated.
            print("Disconnecting from the server...")

            # Decodes the server information for the client.
            data = s.recv(0).decode()

            # Closes the socket between client and server.
            s.close()

            # Return the user to the client menu..
            isConnected = False
            displayMenuClient()

        # If option 6 is selected, a close operation will be displayed for the user.
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

                # Displays a prompt for the user to input shutdown confirmation.
                closeConfirm = input("\nEnter Y or N: ").upper().strip()

                # If the user says yes, close the program.
                if closeConfirm == 'Y':

                    # Perform the appropriate shutdown based on connectivity.
                    if isConnected:
                        # Notify to the user the program is closing.
                        print("Closing client and server programs...")

                        # Performs the shutdown action for the server.
                        s.sendall('6'.encode())

                        # Decodes the server information for the client.
                        data = s.recv(0).decode()

                        # Closes the socket between client and server.
                        s.close()

                        # Set the program to exit.
                        isConnected = False
                        programState = "exit"
                    else:
                        # Notify to the user the program is closing.
                        print("Closing the client program...")

                        # Set the program to exit.
                        programState = "exit"

                # If the user says no, sets the program back to normal.
                elif closeConfirm == 'N':

                    # Display the correct menu based on connectivity.
                    if isConnected:
                        displayMenuServer()
                    else:
                        displayMenuClient()

                    # Set the program back to normal.
                    programState = "normal"

                # Checks if the input is not Y or N, otherwise warn the user.
                else:
                    print("\nIMPORTANT: Please choose Y or N.")

# While the programState is exit, shutdown the programs.
if programState == "exit":
    exit()
