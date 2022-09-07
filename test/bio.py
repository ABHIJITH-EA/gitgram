import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets

class Bio(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Bio")

        self.centralLayout = QtWidgets.QVBoxLayout(self)

        self.setLayout(self.centralLayout)

        self.mainFrame = QtWidgets.QFrame(self)

        self.centralLayout.addWidget(self.mainFrame)

        self.setUpUI()
    
    def setUpUI(self):
        self.mainFrameLayout = QtWidgets.QVBoxLayout(self.mainFrame)

        self.name = QtWidgets.QLabel(self.mainFrame)
        self.name.setText("Linus torvolds")
        self.mainFrameLayout.addWidget(self.name)

        self.bio = QtWidgets.QTextBrowser(self.mainFrame)
        self.bio.setText("Creator and, historically, the main developer of the Linux kernel")
        self.mainFrameLayout.addWidget(self.bio)

        self.followerFrame = QtWidgets.QFrame(self.mainFrame)
        self.followerFrameLayout = QtWidgets.QHBoxLayout(self.followerFrame)
        self.mainFrameLayout.addWidget(self.followerFrame)

        self.follower = QtWidgets.QLabel(self.followerFrame)
        self.follower.setText("Followers")
        self.followersCount = QtWidgets.QLabel(self.followerFrame)
        self.followersCount.setText("158k")
        self.following = QtWidgets.QLabel(self.followerFrame)
        self.following.setText("Following")
        self.followingCount = QtWidgets.QLabel(self.followerFrame)
        self.followingCount.setText("0")

        self.followerFrameLayout.addWidget(self.follower)
        self.followerFrameLayout.addWidget(self.followersCount)
        self.followerFrameLayout.addWidget(self.following)
        self.followerFrameLayout.addWidget(self.followingCount)
        self.followerFrameLayout.addStretch(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    bio = Bio()

    bio.show()

    sys.exit(app.exec_())