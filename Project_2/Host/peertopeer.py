import sys, re, socket, traceback, threading, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import socket
import hostServer
import clientH
from pathlib import Path
from threading import Thread
HOST = socket.gethostname()
isWaitingToConnect = True
USERNAME = ''

def server():
    hostServer.beginConnect()
class GUI(QWidget):
    def __init__(self, parent = None):
        self.GUIClient = clientH.Client()

        self.username = ''
        self.serverHostname = ''
        self.portNumber = 0
        self.hostName = ''
        self.speed = ''
        self.layout = QVBoxLayout()
        super(GUI,self).__init__(parent)
        self.layout2 = QVBoxLayout()
        self.layout3 = QVBoxLayout()
        sublayout1 = QHBoxLayout()
        sublayout2 = QHBoxLayout()
        sublayout3 = QHBoxLayout()
        sublayout4 = QHBoxLayout()
        self.overallLayout = QVBoxLayout()

        self.Label1 = QLabel('Server Hostname:');
        self.IPAddressInput = QLineEdit();
        self.Label2 = QLabel('Port:');
        self.PortInput = QLineEdit();
        self.PortInput.setText("2288")
        self.PortInput.setEnabled(False)
        self.Label3 = QLabel('Username:');
        self.UsernameInput = QLineEdit();
        self.Label4 = QLabel('Hostname:');
        self.HostnameInput = QLineEdit();
        self.HostnameInput.setText(HOST)
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
        self.layout.addLayout(sublayout3)
        self.layout.addLayout(sublayout4)
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
        self.layout2.addLayout(sublayout1)
        self.layout2.addWidget(self.SearchTable)
        self.Label6 = QLabel('Enter Command:')
        self.commandInput = QLineEdit();
        self.commandButton = QPushButton("Go")
        self.commandText = QPlainTextEdit()
        sublayout2.addWidget(self.Label6)
        sublayout2.addWidget(self.commandInput)
        sublayout2.addWidget(self.commandButton)
        self.layout3.addLayout(sublayout2)
        self.layout3.addWidget(self.commandText)
        self.overallLayout.addLayout(self.layout)
        self.overallLayout.addLayout(self.layout2)
        self.overallLayout.addLayout(self.layout3)
        self.setLayout(self.overallLayout)
        self.commandButton.setEnabled(False)
        self.SearchButton.setEnabled(False)

        self.connectButton.clicked.connect(self.connect_pressed)
        self.commandButton.clicked.connect(self.command_pressed)

    def connect_pressed(self):
        self.hostName = self.HostnameInput.text()
        self.portNumber = self.PortInput.text()
        self.username = self.UsernameInput.text()
        self.serverHostname = self.IPAddressInput.text()
        self.speed = self.serverSpeed.currentText()

        returnValue = self.GUIClient.clientConnect(self.hostName, int(self.portNumber), self.username, self.serverHostname, self.speed)
        if returnValue == "Good":
            print("Connected")
        else:
            print("not good")

        self.connectButton.setEnabled(False)
        self.commandButton.setEnabled(True)
        self.SearchButton.setEnabled(True)
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '.', "Text files (*.txt)")
        self.commandText.insertPlainText(">>connect " + self.hostName + " " + self.portNumber + "\n");
        self.commandText.insertPlainText("Connected to " + self.hostName + " " + self.portNumber + "\n");
        self.commandText.insertPlainText("For commands, use the following: \n");
        self.commandText.insertPlainText("1: Retrieve \n");
        self.commandText.insertPlainText("2: Quit and Exit\n");

    def command_pressed(self):
        if self.commandInput.text() == "1":
            text, okPressed = QInputDialog.getText(self, "Get Files", "File name:", QLineEdit.Normal, "")
            if okPressed and text != '':
                try:

                    self.commandText.insertPlainText("Download successful! \n");
                    self.commandText.insertPlainText("For commands, use the following: \n");
                    self.commandText.insertPlainText("1: Retrieve \n");
                    self.commandText.insertPlainText("2: Quit and Exit\n");
                except:
                    self.commandText.insertPlainText("Could not download file\n");
                    self.commandText.insertPlainText("For commands, use the following: \n");
                    self.commandText.insertPlainText("1: Retrieve \n");
                    self.commandText.insertPlainText("2: Quit and Exit\n");
            else:
                self.commandText.insertPlainText("For commands, use the following: \n");
                self.commandText.insertPlainText("1: Retrieve \n");
                self.commandText.insertPlainText("2: Quit and Exit\n");
        elif self.commandInput.text() == "2":
            system.exit();
        else:
            self.commandText.insertPlainText("For commands, use the following: \n");
            self.commandText.insertPlainText("1: Retrieve \n");
            self.commandText.insertPlainText("2: Quit and Exit\n");


def main():
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        Thread(target=server).start()
        Thread(target = main).start()
    except:
        exit(0)
