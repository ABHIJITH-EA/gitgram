import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QIcon, QBrush, QPainter, QWindow, QImage, QFontDatabase, QFont, QFontMetrics
from PyQt5.QtCore import Qt, QRect

class MainWindow(object):
    def __init__(self) -> None:
        self.title = "Git profile"
        self.window_min_width = 750
        self.window_min_height = 500
        
        resource_path = os.path.abspath(os.path.join(os.path.dirname(__package__), 'resource'))
        icon_path = os.path.join(resource_path, 'window-icon.png')
        css_path = os.path.join(resource_path, 'style.css')
        font_path = os.path.join(resource_path, 'Roboto-Regular.ttf')
        avatar_path = os.path.join(resource_path, 'torvolds.jpg')

        self.window_icon = QIcon(icon_path)

        with open(css_path, 'r') as f:
            self.style = f.read()
        
        QFontDatabase.addApplicationFont(font_path)

        self.font = QFont("Roboto")

        with open(avatar_path, 'rb') as f:
            self.imgeData = f.read()

        # Table data
        self.header = ["Repository", "Language", "Fork", "Star"]
        self.name = ["Linux", "uemacs", "test-tlb", "pesconvert", "subsurface-for-dirk", "libdc-for-dirk"]
        self.language = ["C", "C", "C", "C", "C++", "C"]
        self.fork = ["127k", "176", "155", "50", "53", "40"]
        self.star = ["41.1k", "823", "429", "216", "199", "199", "136"]

        self.tableItems = [self.name, self.language, self.fork, self.star]
        
    
    def setUpMainWindow(self, mainWindow):
        mainWindow.setWindowTitle(self.title)
        mainWindow.resize(self.window_min_width, self.window_min_height)
        mainWindow.setWindowIcon(self.window_icon)
        self.centralWidget = QWidget(mainWindow)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.mainFrame = QtWidgets.QFrame(self.centralWidget)
        self.centralLayout.setContentsMargins(0,0,0,0)
        self.centralLayout.addWidget(self.mainFrame)
        mainWindow.setCentralWidget(self.centralWidget)

        self.mainFrame.setObjectName(u'mainFrame')    
        self.mainFrame.setStyleSheet(self.style)
        
        self.mainLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.mainLayout.setContentsMargins( 15, 15, 15, 25)
        self.mainLayout.setSpacing(18)

        self.headFrame = QtWidgets.QFrame(self.mainFrame)
        self.bodyFrame = QtWidgets.QFrame(self.mainFrame)
        self.bodyFrameLayout = QtWidgets.QVBoxLayout(self.bodyFrame)
        self.bodyFrameLayout.setContentsMargins(40, 40, 40, 40)
        self.headFrame.setObjectName(u'headFrame')
        self.bodyFrame.setObjectName(u'bodyFrame')
        self.mainLayout.addWidget(self.headFrame, 40)
        self.mainLayout.addWidget(self.bodyFrame, 60)

        self.headFrameLayout = QtWidgets.QHBoxLayout(self.headFrame)
        self.headFrameLayout.setContentsMargins(40, 40, 40, 30)
        self.headFrameLayout.setSpacing(60)

        self.avatarFrame = QtWidgets.QFrame(self.headFrame)
        self.avatarFrame.setObjectName(u'avatarFrame')

        self.avatarFrameLayout = QtWidgets.QVBoxLayout(self.avatarFrame)
        self.avatar = QtWidgets.QLabel(self.avatarFrame)
        self.avatar.setPixmap(self.roundImage(self.imgeData))
        self.avatarFrameLayout.addWidget(self.avatar, 0, Qt.AlignHCenter)

        self.bioFrame = QtWidgets.QFrame(self.headFrame)
        self.bioFrame.setObjectName(u'bioFrame')
        
        self.headFrameLayout.addWidget(self.avatarFrame, 20, Qt.AlignLeft)
        self.headFrameLayout.addWidget(self.bioFrame, 80)

        # Setting up BIO Section
        self.bioFrameLayout = QtWidgets.QVBoxLayout(self.bioFrame)
        self.bioFrameLayout.setContentsMargins(60, 30, 60, 10)
        self.userName = QtWidgets.QLabel(self.bioFrame)
        self.userName.setText("Linus Torvalds")
        self.userName.setObjectName(u'userName')
        self.userName.setFont(self.font)
        self.userName.setStyleSheet(self.style)
        self.userBio = QtWidgets.QTextBrowser(self.bioFrame)
        self.userBio.setFont(self.font)
        self.userBio.setObjectName(u'userBio')
        self.userBio.setPlainText("Creator and, historically, the main developer of the Linux kernel")
        self.userBioResize()
        self.userBio.setStyleSheet(self.style)
        
        self.followerFrame = QtWidgets.QFrame(self.bioFrame)
        self.followerFrameLayout = QtWidgets.QHBoxLayout(self.followerFrame)
        self.followerLabel = QtWidgets.QLabel(self.followerFrame)
        self.followersCount = QtWidgets.QLabel(self.followerFrame)
        self.followingLabel = QtWidgets.QLabel(self.followerFrame)
        self.followingCount = QtWidgets.QLabel(self.followerFrame)
        self.followerLabel.setText("Followers:")
        self.followingLabel.setText("Following:")
        self.followersCount.setText("150k")
        self.followingCount.setText("0")
        self.followerLabel.setObjectName(u'followerStatus')
        self.followersCount.setObjectName(u'followerStatus')
        self.followingLabel.setObjectName(u'followerStatus')
        self.followingCount.setObjectName(u'followerStatus')
        self.followerFrameLayout.setSpacing(20)
        self.followerFrameLayout.addWidget(self.followerLabel)
        self.followerFrameLayout.addWidget(self.followersCount)
        self.followerFrameLayout.addWidget(self.followingLabel)
        self.followerFrameLayout.addWidget(self.followingCount)

        self.bioFrame.setStyleSheet(self.style)
        self.bioFrameLayout.addWidget(self.userName)
        self.bioFrameLayout.addWidget(self.userBio)
        self.bioFrameLayout.addWidget(self.followerFrame, 0, Qt.AlignLeft)

        self.setUpTable()
        self.repositoryTable.setStyleSheet(self.style)
    

    def setUpTable(self):
        self.repositoryTable = QtWidgets.QTableWidget(self.bodyFrame)
        self.repositoryTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.repositoryTable.setObjectName(u'repositoryTable')
        self.repositoryTable.setRowCount(6)
        self.repositoryTable.setColumnCount(4)

        for row in range(6):
            for col in range(4):
                self.repositoryTable.setItem(row, col, QtWidgets.QTableWidgetItem(self.tableItems[col][row]))

        self.repositoryTable.setHorizontalHeaderLabels(self.header)
        self.repositoryTable.horizontalHeader().setStyleSheet(self.style)
        self.repositoryTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.repositoryTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.repositoryTable.verticalHeader().setVisible(False)
        self.repositoryTable.horizontalHeader().setHighlightSections(False)

        self.bodyFrameLayout.addWidget(self.repositoryTable)


    # Will move this to a utility module
    def roundImage(self, imgdata, imgtype='jpg', size=200):
        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)
        imgsize = min(image.width(), image.height())
        rect = QRect(
            (image.width() - imgsize) // 2,
            (image.height() - imgsize) // 2,
            imgsize,
            imgsize,
        )
        image = image.copy(rect)
        output_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        output_img.fill(Qt.transparent)
        brush = QBrush(image)       
        painter = QPainter(output_img)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawEllipse(0, 0, imgsize, imgsize)
        painter.end()
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(output_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(int(size), int(size), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pm

    def userBioResize(self):
        bioFont = self.userBio.document().defaultFont()
        fontMetrics = QFontMetrics(bioFont)
        textSize = fontMetrics.size(0, self.userBio.toPlainText())
        height = textSize.height() + 25

        self.userBio.setMinimumHeight(height)
        self.userBio.setMaximumHeight(height)