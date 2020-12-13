from ftplib import FTP
import sys

class Client:
    def __init__(self):
        self.ftp = FTP('')

    def clientConnect(self, hostName, Portnumber, username, ipaddress, speed):

        self.ftp.connect(hostName, Portnumber)

        try:
            self.ftp.login(username, "");
        except:
            return "Error authorizing"
        return "Good"