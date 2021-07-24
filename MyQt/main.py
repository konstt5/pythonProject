from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Первая программа")
        self.setGeometry(100, 200, 640, 480)

        self.main_label = QtWidgets.QLabel(self)
        self.main_label.setText("12345678        mkjgmjh kjh h")
        self.main_label.move(100, 100)
        self.main_label.adjustSize()

        self.main_btn = QtWidgets.QPushButton(self)
        self.main_btn.setText("Push Me")
        self.main_btn.move(50, 50)
        self.main_btn.setFixedWidth(150)

        self.main_btn.clicked.connect(self.btn_push)

    def btn_push(self):
        print("pushed")

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()