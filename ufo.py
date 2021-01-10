import sys
import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.f = 0
        self.setGeometry(300, 300, 300, 300)
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 64, 53)
        pixmap = QPixmap('нло.png')
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            if self.label.x() + 5 + self.label.width() > self.width():
                self.label.setGeometry(0, self.label.y(), self.label.width(), self.label.height())
            else:
                self.label.setGeometry(self.label.x() + 5, self.label.y(), self.label.width(), self.label.height())
        if event.key() == Qt.Key_Down:
            if self.label.y() + 5 + self.label.height() > self.height():
                self.label.setGeometry(self.label.x(), 0, self.label.width(), self.label.height())
            else:
                self.label.setGeometry(self.label.x(), self.label.y() + 5, self.label.width(), self.label.height())
        if event.key() == Qt.Key_Left:
            if self.label.x() - 5 < 0:
                self.label.setGeometry(self.width() - self.label.width(), self.label.y(), self.label.width(), self.label.height())
            else:
                self.label.setGeometry(self.label.x() - 5, self.label.y(), self.label.width(), self.label.height())
        if event.key() == Qt.Key_Up:
            if self.label.y() - 5 < 0:
                self.label.setGeometry(self.label.x(), self.height() - self.label.height(), self.label.width(), self.label.height())
            else:
                self.label.setGeometry(self.label.x(), self.label.y() - 5, self.label.width(), self.label.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
