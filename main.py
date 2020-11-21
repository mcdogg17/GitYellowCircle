import sys
from random import randint


from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget
from UI import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.repaint()

    def paintEvent(self, e: QtGui.QPaintEvent):
        self.qp.begin(self)
        d = randint(3, 100)
        self.qp.setBrush(QtGui.QColor(randint(0, 0xffffff)))
        self.qp.drawEllipse(randint(0, self.label.width() - d),
                            randint(0, self.label.height() - d),
                            d, d)
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
