# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin, Kevin Rufino
# Date of Submission: December 14, 2020

from ftplib import FTP


class Client:
    def __init__(self):
        self.ftp = FTP('')

    def clientConnect(self, hostName, portNumber, username, ipAddress, speed):
        self.ftp.connect(hostName, portNumber)

        try:
            self.ftp.login(username, "")
        except:
            return "Error authorizing."
        return "Good."
