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
        self.fileUpload = ''

    # Accepts parameters inputted from central server with anonymous login.
    def clientConnect(self, hostName, portNumber, username, serverHostname, speed):
        self.hostName = hostName
        self.portNumber = portNumber
        self.username = username
        self.serverHostname = serverHostname
        self.speed = speed
        self.ftp.connect("", 4488)

        # Try the login process.
        try:
            self.ftp.login()
        except:
            return "Error authorizing."

    # Allows reading and writing files when the command section is active.
    def updateUsersAndFiles(self, fileUpload):
        self.fileUpload = fileUpload
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

        fileDescriptors = "fileDescriptors.txt"
        # Allows appending of new users to the users.txt file.
        file1 = open(fileDescriptors, 'ab')
        self.ftp.retrbinary('RETR ' + fileDescriptors, open(fileDescriptors, 'wb').write)
        file1.write((fileUpload + " " + self.username + ' ' + self.hostName + ' ' + self.speed + ' ' + str(self.portNumber) + '\n')
                    .encode())
        file1.close()

        # Allows file to be opened on the client.
        fileSend = open(filename, 'rb+')
        self.ftp.storbinary('STOR %s' % filename, fileSend)
        fileSend.close()

        # Allows file to be opened on the central server.
        filename2 = fileUpload
        file2 = open(fileUpload, 'rb+')
        self.ftp.storbinary('STOR %s' % filename2, file2)
        file2.close()

        file3 = open(fileDescriptors, 'rb+')
        self.ftp.storbinary('STOR %s' % fileDescriptors, file3)
        file3.close()

    # Opens a file and writes to the appropriate location.
    def fetchFile(self, filename):
        file = open(filename, 'w')
        self.ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
        file.close()

    def downloadFromOtherPort(self, portName, fileName):
        thisFTP = FTP('')
        thisFTP.connect("", portName)
        thisFTP.login()
        file1 = open(fileName, 'rb+')
        thisFTP.retrbinary('RETR ' + fileName, open(fileName, 'wb').write)
        file1.close()
        thisFTP.quit()

    def getRidOfDescriptor(self):
        self.fetchFile("fileDescriptors.txt")
        # Searches file descriptors text file to populate QTable with data.
        checkFile = open("fileDescriptors.txt", 'r')
        lines = checkFile.readlines()
        checkFile.close()

        newFile = open('fileDescriptors.txt', 'w')
        for line in lines:
            if self.fileUpload not in line:
                newFile.write(line)
        newFile.close()

        file3 = open('fileDescriptors.txt', 'rb+')
        self.ftp.storbinary('STOR fileDescriptors.txt', file3)
        file3.close()
