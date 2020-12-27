# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kyle Jacobson, Logan Jaglowski
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
    hostServer.beginConnect(value)


# Creates and organizes the GUI components.
class GUI(QWidget):
    def __init__(self, parent=None):
        self.GUIClient = clientH.Client()
        self.layout = QVBoxLayout()
        super(GUI, self).__init__(parent)
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

        # Sets specifications for the GUI window.
        self.setFixedSize(1000, 800)
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

        # Creates components for the server host name input components.
        self.Label1 = QLabel('Server Hostname:')
        self.IPAddressInput = QLineEdit(socket.gethostbyname(HOST))

        # Creates components for the port number input components.
        self.Label2 = QLabel('Port:')
        self.portInput = QLineEdit()
        self.portInput.setText(str(value))

        # Creates components for the username input components.
        self.Label3 = QLabel('Username:')
        self.usernameInput = QLineEdit(str(Path.home()).split('\\').__getitem__(2))

        # Creates components for the host name input components.
        self.Label4 = QLabel('Hostname:')
        self.hostnameInput = QLineEdit()
        self.hostnameInput.setText(HOST.upper() + "/" + socket.gethostbyname(HOST))

        # Creates components for the speed input components.
        self.serverSpeed = QComboBox()
        self.serverSpeed.addItem("T1")
        self.serverSpeed.addItem("T3")
        self.serverSpeed.addItem("Modem")
        self.serverSpeed.addItem("Ethernet")

        # Creates button for connection action.
        self.connectButton = QPushButton("Connect")

        # Adds the individual widgets to subLayout 3.
        sublayout3.addWidget(self.Label1)
        sublayout3.addWidget(self.IPAddressInput)
        sublayout3.addWidget(self.Label2)
        sublayout3.addWidget(self.portInput)
        sublayout3.addWidget(self.Label3)
        sublayout3.addWidget(self.usernameInput)
        sublayout4.addWidget(self.Label4)
        sublayout4.addWidget(self.hostnameInput)
        sublayout4.addWidget(self.serverSpeed)
        sublayout4.addWidget(self.connectButton)

        # Create the layout section for the input section.
        self.layout.addLayout(sublayout3)
        self.layout.addLayout(sublayout4)

        # Create components for the search table section.
        self.Label5 = QLabel('Search:')
        self.searchInput = QLineEdit()
        self.searchButton = QPushButton("Search")
        self.searchTable = QTableWidget()
        self.searchTable.setRowCount(1)
        self.searchTable.setColumnCount(3)
        self.searchTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Custom)
        self.searchTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.searchTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Custom)
        self.searchTable.setItem(0, 0, QTableWidgetItem("Speed"))
        self.searchTable.setItem(0, 1, QTableWidgetItem("Hostname"))
        self.searchTable.setItem(0, 2, QTableWidgetItem("Filename"))
        self.searchTable.horizontalHeader().setStretchLastSection(True)

        # Adds the individual widgets to subLayout 1.
        sublayout1.addWidget(self.Label5)
        sublayout1.addWidget(self.searchInput)
        sublayout1.addWidget(self.searchButton)

        # Create the layout 2 section for the searchTable.
        self.layout2.addLayout(sublayout1)
        self.layout2.addWidget(self.searchTable)

        # Create components for the command section.
        self.Label6 = QLabel('Enter Command:')
        self.commandInput = QLineEdit()
        self.commandButton = QPushButton("Go")
        self.commandText = QPlainTextEdit()
        self.commandText.setReadOnly(True)

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

        # Disables certain components of the GUI at launch.
        self.portInput.setEnabled(False)
        self.commandButton.setEnabled(False)
        self.commandInput.setEnabled(False)
        self.searchButton.setEnabled(False)
        self.searchInput.setEnabled(False)

        # Allows the connect and command buttons to be clicked.
        self.connectButton.clicked.connect(self.connect_pressed)
        self.searchButton.clicked.connect(self.search_pressed)
        self.commandButton.clicked.connect(self.command_pressed)

    def closeEvent(self, event):
        self.GUIClient.getRidOfDescriptor()
        self.GUIClient.ftp.close()
        event.accept()

    # Provides the functions for the connect button.
    def connect_pressed(self):
        # Enables the search and command components.
        self.searchInput.setEnabled(True)
        self.commandInput.setEnabled(True)

        # Takes the inputs at the top of the GUI and assigns them to variables.
        self.serverHostname = self.IPAddressInput.text()
        self.portNumber = self.portInput.text()
        self.username = self.usernameInput.text()
        self.hostName = self.hostnameInput.text()
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

            # Opens a menu for opening files you would like to use in the GUI.
            fname, _filter = QFileDialog.getOpenFileName(self, 'Open file', '.', "Text files (*.txt)")
            fname = str(fname)
            fname = ntpath.basename(fname)
            self.GUIClient.updateUsersAndFiles(fname)

            # Enables the command and search buttons.
            self.connectButton.setEnabled(False)
            self.commandButton.setEnabled(True)
            self.searchButton.setEnabled(True)

            # Clears and displays the appropriate information in the command message box.
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

    # Provides the functions for the search button.
    def search_pressed(self):

        # Resets the search table to default when the user inputs whitespace.
        if self.searchInput.text() == "":
            self.searchTable.setRowCount(1)
            self.searchTable.setItem(0, 0, QTableWidgetItem("Speed"))
            self.searchTable.setItem(0, 1, QTableWidgetItem("Hostname"))
            self.searchTable.setItem(0, 2, QTableWidgetItem("Filename"))

        # Fetches the fileDescriptors.txt file from the client.
        self.GUIClient.fetchFile("fileDescriptors.txt")
        counter = 1

        # Searches file descriptors text file to populate QTable with data.
        with open('fileDescriptors.txt', 'r') as file:
            for line in file:
                words = line.split()
                if words:
                    self.GUIClient.fetchFile(words[0])
                    with open(words[0], 'r') as innerFile:
                        for line2 in innerFile:
                            for word in line2.split():
                                if word == '\'' + self.searchInput.text() + '\'':
                                    self.searchTable.setRowCount(counter + 1)
                                    self.searchTable.setItem(counter, 0, QTableWidgetItem(line.split()[3]))
                                    self.searchTable.setItem(counter, 1, QTableWidgetItem(line.split()[2]))
                                    self.searchTable.setItem(counter, 2, QTableWidgetItem(line.split()[0]))
                                    self.searchTable.horizontalHeader().setStretchLastSection(True)
                                    counter += 1
                previousLine = line

    # Provides the functions for the command button.
    def command_pressed(self):
        # When the user selects 1, go through the retrieve file process.
        if self.commandInput.text() == "1":
            # Displays a input dialog box for retrieving specific files from the directory.
            text, okPressed = QInputDialog.getText(self, "Get Files", "File Name:", QLineEdit.Normal, "")

            # If okay was pressed in input dialog box and their was an input, continue.
            if okPressed and text != '':
                # If the file exist in the directory, the download will be successful.
                self.GUIClient.fetchFile("fileDescriptors.txt")
                portNumber = 0

                # Searches file descriptors text file to determine if download is successful.
                with open('fileDescriptors.txt', 'r') as file:
                    for line in file:
                        words = line.split()
                        if words:
                            self.GUIClient.fetchFile(words[0])
                            with open(words[0], 'r') as innerFile:
                                for line2 in innerFile:
                                    for word in line2.split():
                                        if word == text:
                                            portNumber = int(line.split()[4])
                                            isFound = True

                # If the file does exist in the directory, the download will be successful.
                try:
                    self.GUIClient.downloadFromOtherPort(portNumber, text)
                    self.commandText.clear()
                    self.commandText.insertPlainText("Download successful! \n")
                    self.commandText.insertPlainText("\nFor commands, use the corresponding number: \n")
                    self.commandText.insertPlainText("1: Retrieve a File\n")
                    self.commandText.insertPlainText("2: Disconnect from Server\n")
                    self.commandText.insertPlainText("3: Close the Program\n")

                # If the file does not exist in the directory, the download will be unsuccessful.
                except:
                    self.commandText.clear()
                    self.commandText.insertPlainText("Could not download file. \n")
                    self.commandText.insertPlainText("\nFor commands, use the corresponding number: \n")
                    self.commandText.insertPlainText("1: Retrieve a File\n")
                    self.commandText.insertPlainText("2: Disconnect from Server\n")
                    self.commandText.insertPlainText("3: Close the Program\n")

        # When the user selects 2, disconnect from the central server.
        elif self.commandInput.text() == "2":
            self.GUIClient.getRidOfDescriptor()
            self.GUIClient.ftp.close()

            # Reset the search components.
            self.searchInput.setText("")
            self.searchTable.setRowCount(1)
            self.searchTable.setColumnCount(3)
            self.searchTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Custom)
            self.searchTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            self.searchTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Custom)
            self.searchTable.setItem(0, 0, QTableWidgetItem("Speed"))
            self.searchTable.setItem(0, 1, QTableWidgetItem("Hostname"))
            self.searchTable.setItem(0, 2, QTableWidgetItem("Filename"))
            self.searchTable.horizontalHeader().setStretchLastSection(True)

            # Reset the command components.
            self.commandText.clear()
            self.commandInput.setText("")

            # Disables the command and search buttons.
            self.connectButton.setEnabled(True)
            self.commandButton.setEnabled(False)
            self.commandInput.setEnabled(False)
            self.searchButton.setEnabled(False)
            self.searchInput.setEnabled(False)

            self.commandText.insertPlainText("You have disconnected from the server.")

        # When the user selects 3, close down the entire program.
        elif self.commandInput.text() == "3":
            self.GUIClient.getRidOfDescriptor()
            self.GUIClient.ftp.close()

            exit(0)

        # When the user provides incorrect input, display a warning message
        else:
            self.commandText.clear()
            self.commandText.insertPlainText("WARNING: Please use one of the following commands. \n")
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
