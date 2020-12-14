# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin, Kevin Rufino
# Date of Submission: December 16, 2020

# The clientH takes parameters for the client when executing the connection.
from datetime import datetime
from ftplib import FTP


# Controls many of the interactions for the client.
class Client:
    # Initializes the different variables related to the client.
    def __init__(self):
        self.hostName = ''
        self.portNumber = 0
        self.username = ''
        self.serverHostname = ''
        self.speed = ''
        self.ftp = FTP('')

    # Accepts parameters inputted from central server with anonymous login.
    def clientConnect(self, hostName, portNumber, username, serverHostname, speed):
        self.hostName = hostName
        self.portNumber = portNumber
        self.username = username
        self.serverHostname = serverHostname
        self.speed = speed
        self.ftp.connect("", 4488)

        try:
            self.ftp.login()
        except:
            return "Error authorizing."

    # Allows reading and writing files when the command section is active.
    def updateUsersAndFiles(self, fileUpload):
        filename = "users.txt"

        # Allows appending of new users to the users.txt file.
        file = open(filename, 'ab')
        self.ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
        file.write(("User Information" + "\n"
                    "Username: " + self.username + "\n" +
                    "Host Name: " + self.hostName + "\n" +
                    "Speed: " + self.speed + "\n" +
                    "Time: " + str(datetime.now()) + "\n\n")
                   .encode())
        file.close()

        # Allows file to be opened on the client.
        fileSend = open(filename, 'rb+')
        self.ftp.storbinary('STOR %s' % filename, fileSend)
        fileSend.close()

        # Allows file to be opened on the central server.
        filename2 = fileUpload
        file2 = open(fileUpload, 'rb+')
        self.ftp.storbinary('STOR %s' % filename2, file2)
        file2.close()

    # Opens a file and writes to the appropriate location.
    def fetchFile(self, filename):
        file = open(filename, 'w')
        self.ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
        file.close()
