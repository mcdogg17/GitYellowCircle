import sys
from random import randint

from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.repaint()

    def paintEvent(self, e: QtGui.QPaintEvent):
        self.qp.begin(self)
        d = randint(3, 100)
        self.qp.setBrush(Qt.yellow)
        self.qp.drawEllipse(randint(0, self.label.width() - d),
                            randint(0, self.label.height() - d),
                            d, d)
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
