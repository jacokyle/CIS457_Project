# Project 2 - GV-NAP File Sharing System
# CIS 457 - Data Communications
# Authors: Kevin Rufino, Kyle Jacobson, Logan Jaglowski, Kade O'Laughlin
# Date of Submission: December 14, 2020

# The peertopeer program creates the GUI for Project 2.

import sys
from PyQt5.QtWidgets import *

# Initializes the various inputs for the GUI.
isUserRegistered = False
username = ''
ipAddress = ''
portNumber = ''
hostName = ''
speed = ''


# Contains the components and layout of the GUI features.
class GUI(QWidget):
    def __init__(self, parent = None):
        layout = QVBoxLayout()
        super(GUI,self).__init__(parent)
        self.setWindowTitle("GV-NAP File Sharing System")

        # Creates layouts for each section of the GUI.
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        sublayout1 = QHBoxLayout()
        sublayout2 = QHBoxLayout()
        sublayout3 = QHBoxLayout()
        sublayout4 = QHBoxLayout()
        overallLayout = QVBoxLayout()

        # Creates components for the input section.
        self.Label1 = QLabel('Server Hostname:')
        self.IPAddressInput = QLineEdit()
        self.Label2 = QLabel('Port:')
        self.PortInput = QLineEdit()
        self.Label3 = QLabel('Username:')
        self.UsernameInput = QLineEdit()
        self.Label4 = QLabel('Hostname:')
        self.HostnameInput = QLineEdit()
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

        # Adds the individual widgets to subLayout 4.
        sublayout4.addWidget(self.Label4)
        sublayout4.addWidget(self.HostnameInput)
        sublayout4.addWidget(self.serverSpeed)
        sublayout4.addWidget(self.connectButton)

        # Create the layout section for the input section.
        layout.addLayout(sublayout3)
        layout.addLayout(sublayout4)

        # Create components for the search table section.
        self.Label5 = QLabel('Search:')
        self.SearchInput = QLineEdit()
        self.SearchButton = QPushButton("Search")
        self.SearchTable = QTableWidget()
        self.SearchTable.setRowCount(1)
        self.SearchTable.setColumnCount(3)
        self.SearchTable.setItem(0,0, QTableWidgetItem("Speed"))
        self.SearchTable.setItem(0, 1, QTableWidgetItem("Hostname"))
        self.SearchTable.setItem(0, 2, QTableWidgetItem("Filename"))

        # Adds the individual widgets to subLayout 1.
        sublayout1.addWidget(self.Label5)
        sublayout1.addWidget(self.SearchInput)
        sublayout1.addWidget(self.SearchButton)

        # Create the layout 2 section for the searchTable.
        layout2.addLayout(sublayout1)
        layout2.addWidget(self.SearchTable)

        # Create components for the command section.
        self.Label6 = QLabel('Enter Command:')
        self.commandInput = QLineEdit();
        self.commandButton = QPushButton("Go")
        self.commandText = QPlainTextEdit()

        # Adds the individual widgets to subLayout 2.
        sublayout2.addWidget(self.Label6)
        sublayout2.addWidget(self.commandInput)
        sublayout2.addWidget(self.commandButton)

        # Create the layout 2 section for the command section.
        layout3.addLayout(sublayout2)
        layout3.addWidget(self.commandText)

        # Add the 3 primary layouts to the main layout.
        overallLayout.addLayout(layout)
        overallLayout.addLayout(layout2)
        overallLayout.addLayout(layout3)

        # Set the main layout to appear.
        self.setLayout(overallLayout)


def main():
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
