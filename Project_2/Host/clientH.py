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
        self.ftp.connect(hostName, 4488)

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
        filename2 = fileUpload
        file2 = open(fileUpload, 'w')
        self.ftp.storbinary('STOR %s' % filename2, file2)
        file2.close()

    def fetchFile(self, filename):
        file = open(filename, 'w')
        ftp.retrbinary('RETR ' + filename, open(filename, 'w').write)
        file.close()
