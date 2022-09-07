import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from windows.mainWindow import MainWindow
from windows.findWindow import FindWindow

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.UI = MainWindow()
        self.UI.setUpMainWindow(self)


class Find(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.UI = FindWindow()
        self.UI.setUpFindWindow(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # main window
    mainWindow = Main()
    mainWindow.show()

    # find = Find()
    # find.show()

    sys.exit(app.exec_())