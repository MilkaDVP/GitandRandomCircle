import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QColor
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 464)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("генерировать окружность")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = MainWindow.menuBar()
        self.menubar.setGeometry(QRect(0, 0, 481, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = MainWindow.statusBar()
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


class CircleLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QColor(0, 0, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.color)
        painter.drawEllipse(self.rect())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.circle_label = CircleLabel(self.centralwidget)
        self.circle_label.setGeometry(0, 0, 0, 0)

    def draw_circle(self):
        self.circle_label.clear()

        diameter = random.randint(50, 150)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circle_label.color = color
        x = int((self.centralwidget.width() - diameter) / 2)
        y = int((self.centralwidget.height() - diameter) / 2)
        self.circle_label.setGeometry(x, y, diameter, diameter)
        self.circle_label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
