# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The client program presents a command line interface with actions for the user.

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4000  # The port used by the server

# Displays the client options for the user.
print("\nChoose an option for the client:\n")
print("1 - (Connect)    Connect to the server.")
print("2 - (List)       List contents of the current directory.")
print("3 - (Retrieve)   Retrieve a file from the server.")
print("4 - (Store)      Send a file to server.")
print("5 - (Quit)       Terminate the control connection.\n")

# Displays a prompt for the user to input their choice.
option = input("Enter a number: ")

# Checks if the option the user provided is not a number or too long.
if option.isalpha() or len(option) >= 2:
    print("The input you provided was not an option. Try again.")

# If the input is a number, convert it to type integer.
if option.isdigit():
    option = int(option)

# If the input is an integer, continue to the next step.
if isinstance(option, int):

    # If the integer is not an available choice, warn the user.
    if option <= 0 or option >= 6:
        print("The number you provided is not a choice. Try again.")

    # If the integer is 1, connect to the server.
    if option == 1:
        print("\nConnecting to server.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))

    # If the integer is 2, list the contents of the directory.
    if option == 2:
        print("\nListing contents of current directory.")

    # If the integer is 3, retrieve a file from the server.
    if option == 3:
        print("\nRetrieving file from the server.")

    # If the integer is 4, send a file to the server.
    if option == 4:
        print("\nSending file to the server.")

    # If the integer is 5, terminate the client and server.
    if option == 5:
        print("\nTerminating client and server programs.")
