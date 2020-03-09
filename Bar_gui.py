from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys


class Stacked(QWidget):
    def __init__(self):
        super(Stacked, self).__init__()
        self.initUI()
        self.mainLayout()

    def initUI(self):
        self.setGeometry(400, 400, 850, 550)
        self.setWindowTitle("词频区间")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def mainLayout(self):
        self.mainhboxLayout = QHBoxLayout(self)
        self.frame = QFrame(self)
        self.mainhboxLayout.addWidget(self.frame)
        self.hboxLayout = QHBoxLayout(self.frame)
        self.myHtml = QWebEngineView()
        # 打开本地html文件
        # 词频区间柱状图
        self.myHtml.load(QUrl("file:///C:/Users/sy/Desktop/Python课设/EnglishKiller/0.html"))
        # CVPR
        # self.myHtml.load(QUrl("file:///C:/Users/sy/Desktop/Python课设/EnglishKiller/3.html"))
        self.hboxLayout.addWidget(self.myHtml)
        self.setLayout(self.mainhboxLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Stacked()
    ex.show()
    sys.exit(app.exec_())