# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin, Kevin Rufino
# Date of Submission: December 16, 2020

# The clientH takes parameters for the client when executing connection.

from ftplib import FTP


class Client:
    def __init__(self):
        self.hostName = ''
        self.portNumber = 0
        self.username = ''
        self.serverHostname = ''
        self.speed = ''
        self.ftp = FTP('')

    def clientConnect(self, hostName, portNumber, username, serverHostname, speed):
        self.hostName = hostName
        self.portNumber = portNumber
        self.username = username
        self.serverHostname = serverHostname
        self.speed = speed
        self.ftp.connect('', 4488)

        try:
            self.ftp.login("", "")
        except:
            return "Error authorizing."

    def updateUsersAndFiles(self, fileUpload):
        filename = "users.txt"

        file = open(filename, 'ab')
        self.ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
        file.write((self.username + " " + self.hostName + " " + self.speed + "\n").encode())
        file.close()

        fileSend = open(filename, 'rb+')
        self.ftp.storbinary('STOR %s' % filename, fileSend)
        fileSend.close()

        filename2 = fileUpload
        file2 = open(fileUpload, 'rb+')
        self.ftp.storbinary('STOR %s' % filename2, file2)
        file2.close()

    def fetchFile(self, filename):
        file = open(filename, 'w')
        self.ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
        file.close()
