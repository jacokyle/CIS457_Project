# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin, Kevin Rufino
# Date of Submission: December 16, 2020

# The peertopeer program contains the various elements of the GUI.

import clientH
import hostServer
import ntpath
import socket
import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from random import randint
from threading import Thread

# Assigns a random port number for the client.
value = randint(1024, 49151)

# The socket's hostname or IP address.
HOST = socket.gethostname()

# Initializes the global variables.
isWaitingToConnect = True
USERNAME = ''


# Begins the connection to the host server.
def server():
    hostServer.beginConnect()


# Creates and organizes the GUI components.
class GUI(QWidget):
    def __init__(self, parent=None):
        self.GUIClient = clientH.Client()
        self.layout = QVBoxLayout()
        super(GUI, self).__init__(parent)
        self.setWindowTitle("GV-NAP File Sharing System")

        # Initializes the input parameters.
        self.username = ''
        self.serverHostname = ''
        self.portNumber = 0
        self.hostName = ''
        self.speed = ''

        # Creates layouts for each section of the GUI.
        self.layout2 = QVBoxLayout()
        self.layout3 = QVBoxLayout()
        sublayout1 = QHBoxLayout()
        sublayout2 = QHBoxLayout()
        sublayout3 = QHBoxLayout()
        sublayout4 = QHBoxLayout()
        self.overallLayout = QVBoxLayout()

        # Creates components for the input section.
        self.Label1 = QLabel('Server Hostname:')
        self.IPAddressInput = QLineEdit(socket.gethostbyname(HOST))

        self.Label2 = QLabel('Port:')
        self.PortInput = QLineEdit()
        self.PortInput.setText(str(value))
        self.PortInput.setEnabled(False)

        self.Label3 = QLabel('Username:')
        self.UsernameInput = QLineEdit(str(Path.home()).split('\\').__getitem__(2))

        self.Label4 = QLabel('Hostname:')
        self.HostnameInput = QLineEdit()
        self.HostnameInput.setText(HOST.upper() + "/" + socket.gethostbyname(HOST))

        self.serverSpeed = QComboBox()
        self.serverSpeed.addItem("T1")
        self.serverSpeed.addItem("T3")
        self.serverSpeed.addItem("Modem")
        self.serverSpeed.addItem("Ethernet")

        self.connectButton = QPushButton("Connect")

        # Adds the individual widgets to subLayout 3.
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

        # Create the layout section for the input section.
        self.layout.addLayout(sublayout3)
        self.layout.addLayout(sublayout4)

        # Create components for the search table section.
        self.Label5 = QLabel('Search:')
        self.SearchInput = QLineEdit()
        self.SearchButton = QPushButton("Search")
        self.SearchTable = QTableWidget()
        self.SearchTable.setRowCount(1)
        self.SearchTable.setColumnCount(3)
        self.SearchTable.setItem(0, 0, QTableWidgetItem("Speed"))
        self.SearchTable.setItem(0, 1, QTableWidgetItem("Hostname"))
        self.SearchTable.setItem(0, 2, QTableWidgetItem("Filename"))

        # Adds the individual widgets to subLayout 1.
        sublayout1.addWidget(self.Label5)
        sublayout1.addWidget(self.SearchInput)
        sublayout1.addWidget(self.SearchButton)

        # Create the layout 2 section for the searchTable.
        self.layout2.addLayout(sublayout1)
        self.layout2.addWidget(self.SearchTable)

        # Create components for the command section.
        self.Label6 = QLabel('Enter Command:')
        self.commandInput = QLineEdit()
        self.commandButton = QPushButton("Go")
        self.commandText = QPlainTextEdit()

        # Adds the individual widgets to subLayout 2.
        sublayout2.addWidget(self.Label6)
        sublayout2.addWidget(self.commandInput)
        sublayout2.addWidget(self.commandButton)

        # Create the layout 2 section for the command section.
        self.layout3.addLayout(sublayout2)
        self.layout3.addWidget(self.commandText)

        # Add the 3 primary layouts to the main layout.
        self.overallLayout.addLayout(self.layout)
        self.overallLayout.addLayout(self.layout2)
        self.overallLayout.addLayout(self.layout3)

        # Set the main layout to appear.
        self.setLayout(self.overallLayout)

        # Enables the command and search buttons.
        self.commandButton.setEnabled(False)
        self.SearchButton.setEnabled(False)

        # Allows the connect and command buttons to be clicked.
        self.connectButton.clicked.connect(self.connect_pressed)
        self.commandButton.clicked.connect(self.command_pressed)

    # Provides the functions for the connect button.
    def connect_pressed(self):
        self.serverHostname = self.IPAddressInput.text()
        self.portNumber = self.PortInput.text()
        self.username = self.UsernameInput.text()
        self.hostName = self.HostnameInput.text()
        self.speed = self.serverSpeed.currentText()

        # Check if serverHostname is blank.
        if self.serverHostname == "":
            invalidUsername = QMessageBox()
            invalidUsername.setIcon(QMessageBox.Critical)
            invalidUsername.setText("Please enter an IP address")
            invalidUsername.setWindowTitle("Server Hostname Warning")
            invalidUsername.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            invalidUsername.exec()

        # Check if username is blank.
        if self.username == "":
            invalidUsername = QMessageBox()
            invalidUsername.setIcon(QMessageBox.Critical)
            invalidUsername.setText("Please enter a username.")
            invalidUsername.setWindowTitle("Username Warning")
            invalidUsername.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            invalidUsername.exec()

        # Check if hostName is blank.
        if self.hostName == "":
            invalidUsername = QMessageBox()
            invalidUsername.setIcon(QMessageBox.Critical)
            invalidUsername.setText("Please enter a host name.")
            invalidUsername.setWindowTitle("Hostname Warning")
            invalidUsername.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            invalidUsername.exec()

        # If all fields have information, allow a connection to occur.
        if len(self.serverHostname) > 0 and len(self.username) > 0 and len(self.hostName) > 0:
            self.GUIClient.clientConnect(self.hostName, int(self.portNumber), self.username,
                                         self.serverHostname, self.speed)

            fname, _filter = QFileDialog.getOpenFileName(self, 'Open file', '.', "Text files (*.txt)")
            fname = str(fname)
            fname = ntpath.basename(fname)
            self.GUIClient.updateUsersAndFiles(fname)

            self.connectButton.setEnabled(False)
            self.commandButton.setEnabled(True)
            self.SearchButton.setEnabled(True)

            self.commandText.clear()
            self.commandText.insertPlainText("You have connected to the server.\n")
            self.commandText.insertPlainText(
                "\n>> connect " + socket.gethostbyname(HOST) + " " + self.portNumber + "\n")
            self.commandText.insertPlainText(
                "Connected to " + socket.gethostbyname(HOST) + ":" + self.portNumber + "\n")
            self.commandText.insertPlainText("\nFor commands, use the corresponding number: \n")
            self.commandText.insertPlainText("1: Retrieve a File\n")
            self.commandText.insertPlainText("2: Disconnect from Server\n")
            self.commandText.insertPlainText("3: Close the Program\n")

    # Provides the functions for the command button.
    def command_pressed(self):
        if self.commandInput.text() == "1":
            text, okPressed = QInputDialog.getText(self, "Get Files", "File Name:", QLineEdit.Normal, "")

            if okPressed and text != '':
                try:
                    self.GUIClient.fetchFile(text)
                    self.commandText.insertPlainText("\nDownload successful! \n")
                    self.commandText.insertPlainText("\nFor commands, use the corresponding number: \n")
                    self.commandText.insertPlainText("1: Retrieve a File\n")
                    self.commandText.insertPlainText("2: Disconnect from Server\n")
                    self.commandText.insertPlainText("3: Close the Program\n")
                except:
                    self.commandText.insertPlainText("\nCould not download file. \n")
                    self.commandText.insertPlainText("\nFor commands, use the corresponding number: \n")
                    self.commandText.insertPlainText("1: Retrieve a File\n")
                    self.commandText.insertPlainText("2: Disconnect from Server\n")
                    self.commandText.insertPlainText("3: Close the Program\n")
        elif self.commandInput.text() == "2":
            self.GUIClient.ftp.close()

            self.commandText.clear()
            self.connectButton.setEnabled(True)
            self.commandButton.setEnabled(False)
            self.SearchButton.setEnabled(False)

            self.commandText.insertPlainText("You have disconnected from the server.")
        elif self.commandInput.text() == "3":
            exit(0)
        else:
            self.commandText.insertPlainText("\nWARNING: Please use one of the following commands. \n")
            self.commandText.insertPlainText("\nFor commands, use the corresponding number: \n")
            self.commandText.insertPlainText("1: Retrieve a File\n")
            self.commandText.insertPlainText("2: Disconnect from Server\n")
            self.commandText.insertPlainText("3: Close the Program\n")


# Part of the main method for creating and showing a GUI object.
def main():
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())


# Part of the main method for executing the GUI.
if __name__ == '__main__':
    try:
        Thread(target=server).start()
        Thread(target=main).start()
    except:
        exit(0)
