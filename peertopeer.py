import sys, re, socket, traceback, threading, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

isUserRegistered = False
username = ''
ipAddress = ''
portNumber = ''
hostName = ''
speed = ''


class GUI(QWidget):
    def __init__(self, parent = None):
        layout = QVBoxLayout()
        super(GUI,self).__init__(parent)
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        sublayout1 = QHBoxLayout()
        sublayout2 = QHBoxLayout()
        sublayout3 = QHBoxLayout()
        sublayout4 = QHBoxLayout()
        overallLayout = QVBoxLayout()

        self.Label1 = QLabel('Server Hostname:');
        self.IPAddressInput = QLineEdit();
        self.Label2 = QLabel('Port:');
        self.PortInput = QLineEdit();
        self.Label3 = QLabel('Username:');
        self.UsernameInput = QLineEdit();
        self.Label4 = QLabel('Hostname:');
        self.HostnameInput = QLineEdit();
        self.serverSpeed = QComboBox()
        self.serverSpeed.addItem("T1")
        self.serverSpeed.addItem("T3")
        self.serverSpeed.addItem("Modem")
        self.serverSpeed.addItem("Ethernet")
        self.connectButton = QPushButton("Connect")
        sublayout3.addWidget(self.Label1)
        sublayout3.addWidget(self.IPAddressInput)
        sublayout3.addWidget(self.Label2)
        sublayout3.addWidget(self.PortInput)
        sublayout3.addWidget(self.Label3)
        sublayout3.addWidget(self.UsernameInput)
        sublayout4.addWidget(self.Label4)
        sublayout4.addWidget(self.HostnameInput)
        sublayout4.addWidget(self.serverSpeed)
        sublayout4.addWidget(self.connectButton)
        layout.addLayout(sublayout3)
        layout.addLayout(sublayout4)
        self.Label5 = QLabel('Search:');
        self.SearchInput = QLineEdit();
        self.SearchButton = QPushButton("Search")
        self.SearchTable = QTableWidget()
        self.SearchTable.setRowCount(1)
        self.SearchTable.setColumnCount(3)
        self.SearchTable.setItem(0,0, QTableWidgetItem("Speed"))
        self.SearchTable.setItem(0, 1, QTableWidgetItem("Hostname"))
        self.SearchTable.setItem(0, 2, QTableWidgetItem("Filename"))
        sublayout1.addWidget(self.Label5)
        sublayout1.addWidget(self.SearchInput)
        sublayout1.addWidget(self.SearchButton)
        layout2.addLayout(sublayout1)
        layout2.addWidget(self.SearchTable)
        self.Label6 = QLabel('Enter Command:')
        self.commandInput = QLineEdit();
        self.commandButton = QPushButton("Go")
        self.commandText = QPlainTextEdit()
        sublayout2.addWidget(self.Label6)
        sublayout2.addWidget(self.commandInput)
        sublayout2.addWidget(self.commandButton)
        layout3.addLayout(sublayout2)
        layout3.addWidget(self.commandText)
        overallLayout.addLayout(layout)
        overallLayout.addLayout(layout2)
        overallLayout.addLayout(layout3)
        self.setLayout(overallLayout)






def main():
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
