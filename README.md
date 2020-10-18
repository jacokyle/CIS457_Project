# CIS457 - Building an FTP Server (Project 1)

This project was created by Kyle Jacobson, Logan Jaglowski and Kade O'Laughlin for Data Communications (CIS 457) during the Fall 2020 semester at Grand Valley State University.

This project was programmed using the Python programming language on JetBrains' PyCharm IDE.

It includes a client and server program that can interact with one another.

The client program presents a command line interface that allows a user to:
### Connect 
- Connect to a server.
### List 
- List files stored at the server.
### Retrieve
- Download a file from the server.
### Store 
- Upload a file from the client to the server.
### Quit 
- Terminate the connection to the server.

The server program binds to a port and listens for requests from a client. After a client connects to the server, the server waits for commands. When the client sends a terminate message (quit), the server terminates the connection and waits for the next connection.
