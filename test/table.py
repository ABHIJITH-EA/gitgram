import sys
from turtle import color

from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor

class RepositoryTable(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Respository table")


        self.centralLayout = QtWidgets.QVBoxLayout(self)

        self.setLayout(self.centralLayout)

        self.mainFrame = QtWidgets.QFrame(self)
        
        self.centralLayout.addWidget(self.mainFrame)

        self.header = ["Repository", "Language", "Fork", "Star"]
        self.name = ["Linux", "uemacs", "test-tlb", "pesconvert", " subsurface-for-dirk", "libdc-for-dirk"]
        self.language = ["C", "C", "C", "C", "C++", "C"]
        self.fork = ["127k", "176", "155", "50", "53", "40"]
        self.star = ["41.1k", "823", "429", "216", "199", "199", "136"]

        self.tableItems = [self.name, self.language, self.fork, self.star]

        self.setUpUI()

    def setUpUI(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.repositoryTable = QtWidgets.QTableWidget(self.mainFrame)
        self.repositoryTable.setRowCount(6)
        self.repositoryTable.setColumnCount(4)

        for row in range(6):
            for col in range(4):
                self.repositoryTable.setItem(row, col, QtWidgets.QTableWidgetItem(self.tableItems[col][row]))

        self.repositoryTable.setHorizontalHeaderLabels(self.header)
        self.repositoryTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.repositoryTable.setStyleSheet("QTableWidget { selection-color: palette(text); selection-background-color: palette(base); }")

        self.mainLayout.addWidget(self.repositoryTable)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    bio = RepositoryTable()

    bio.show()

    sys.exit(app.exec_())