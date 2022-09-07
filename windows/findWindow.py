import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

class FindWindow(object):
    def __init__(self) -> None:
        self.title = "Git profile"
        self.window_min_width = 750
        self.window_min_height = 500
        
        resource_path = os.path.abspath(os.path.join(os.path.dirname(__package__), 'resource'))
        icon_path = os.path.join(resource_path, 'window-icon.png')
        
        self.window_icon = QIcon(icon_path)

    def setUpFindWindow(self, findWindow):
        findWindow.setWindowTitle(self.title)
        findWindow.resize(self.window_min_width, self.window_min_height)
        findWindow.setWindowIcon(self.window_icon)
        self.centralWidget = QWidget(findWindow)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.mainFrame = QtWidgets.QFrame(self.centralWidget)
        self.centralLayout.setContentsMargins(0,0,0,0)
        self.centralLayout.addWidget(self.mainFrame)
        findWindow.setCentralWidget(self.centralWidget)