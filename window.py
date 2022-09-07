# import sys
# from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QVBoxLayout
# from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
# from PyQt5.QtCore import Qt

# class MainWindow(object):
#     def setUpMainWindow(self, mainWindow):
#         mainWindow.setWindowTitle("Git profile")
#         mainWindow.resize(650, 420)

#         self.centralWidget = QWidget(mainWindow)

#         self.layout = QVBoxLayout(self.centralWidget)

#         self.radius = 25
        
#         label = QLabel(self.centralWidget)
#         label.setMaximumSize(50, 50)
#         label.setMinimumSize(50, 50)
#         label.setText("Abhijith")
#         self.layout.addWidget(label)

#         avatar = QPixmap(label.size())
#         avatar.fill(Qt.transparent)
#         image = QPixmap('E:/git-profile/data/avatar.png').scaled(50, 50, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
#         # paiter = QPainter(avatar)
#         # path = QPainterPath()
#         # path.addRoundedRect(0, 0, label.width(), label.height(), self.radius, self.radius)

#         mainWindow.setCentralWidget(self.centralWidget)



# class Start(QMainWindow):
#     def __init__(self) -> None:
#         super().__init__()

#         self.UI = MainWindow()
#         self.UI.setUpMainWindow(self)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     start = Start()
#     start.show()

#     sys.exit(app.exec_())

import sys
from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPixmap, QPainter, QPainterPath
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QApplication

class Label(QLabel):
    def __init__(self, *args, antialiasing=True, **kwargs):
        super(Label, self).__init__(*args, **kwargs)
        self.Antialiasing = antialiasing
        self.setMaximumSize(50, 50)
        self.setMinimumSize(50, 50)
        self.radius = 25 

        self.target = QPixmap(self.size())  
        self.target.fill(Qt.transparent)   

        p = QPixmap('E:/git-profile/data/avatar.png').scaled(  
            50, 50, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        painter = QPainter(self.target)
        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.setPixmap(self.target)

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.addWidget(Label(self))
        layout.addWidget(Label(self, antialiasing=False))  
        self.setStyleSheet("background: blue;")           

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())