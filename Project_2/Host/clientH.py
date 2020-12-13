# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin, Kevin Rufino
# Date of Submission: December 16, 2020

# The clientH takes parameters for the client when executing connection.

from ftplib import FTP
import sys

class Client:
    def __init__(self):
        self.speed = ''
        self.portNumber = 0
        self.hostName = ''
        self.serverHostname = ''
        self.username = ''
        self.ftp = FTP('')
    def clientConnect(self, hostName, Portnumber, username, serverHostname, speed):
        self.hostName = hostName
        self.portNumber = Portnumber
        self.username = username
        self.serverHostname = serverHostname
        self.speed = speed
        self.ftp.connect('', 4488)
        try:
            self.ftp.login("", "");
        except:
            return "Error authorizing"
        return "Good"
    def updateUsersAndFiles(self, fileUpload):
        filename = "users.txt"
        file = open(filename, 'wb')
        self.ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
        file.write((self.username+ " " + self.hostName + "" + self.speed + "\n").encode())
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
        ftp.retrbinary('RETR ' + filename, open(filename, 'w').write)
        file.close()
