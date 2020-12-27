# CIS457 - Building an FTP Server (Project 1)

This project was created by Kyle Jacobson and Logan Jaglowski for Data Communications (CIS 457) during the Fall 2020 semester at Grand Valley State University.

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

# CIS457 - GV-NAP File Sharing System (Project 2)

This project was created by Kyle Jacobson and Logan Jaglowski for Data Communications (CIS 457) during the Fall 2020 semester at Grand Valley State University.

This project was programmed using the Python programming language on JetBrains' PyCharm IDE.

It includes a Graphical User Interface (GUI) that uses a centralized directory indexing service to implement a P2P architecture. 

The program utilizes two components:
### Host System
- Query the server for files using keywords.  The host also has a file transfer client and server.  The ftp client allows a user to access files stored at the remote user locations.  The ftp server is responsible for providing file transfer services requested by a remote client.
### Centralized Server
- Provides a search facility that can be used to perform simple keyword searches.  The result of the search is the location of the remote resource.
