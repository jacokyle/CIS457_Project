# Project 1 - Building an FTP Server
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: October 26, 2020

# The client program presents a command line interface with actions for the user.

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4000  # The port used by the server

print("\nChoose an option for the client:\n")
print("1 - (Connect)    Connect to the server.")
print("2 - (List)       List contents of the current directory.")
print("3 - (Retrieve)   Retrieve a file from the server.")
print("4 - (Store)      Send a file to server.")
print("5 - (Quit)       Terminate the control connection.\n")

option = input("Enter a number: ")

if option.isalpha() or len(option) >= 2:
    print("The input you provided was not an option. Try again.")

if isinstance(option, int):
    if option <= 0 or option >= 6:
        print("The number you provided is not a choice. Try again.")

    if option == 1:
        print("\nConnecting to server.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))

    if option == 2:
        print("\nListing contents of current directory.")

    if option == 3:
        print("\nRetrieving file from the server.")

    if option == 4:
        print("\nSending file to the server.")

    if option == 5:
        print("\nTerminating client and server programs.")
