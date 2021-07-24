import sys, os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        # Установить заголовок
        self.setWindowTitle("Примеры рисования")
        # Создание класса QPixmap
        self.pix = QPixmap()
        self.path = r'C:\Users\Konstantin\PycharmProjects\pythonProject\SPGUI\art'

    def convertFiles(self):
        exe = r'C:\Users\Konstantin\PycharmProjects\pythonProject\SPGUI\art\pngcrush_1_8_11_w32.exe'  # pngcrush file

        for file in os.listdir(self.path):
            if file.endswith(".png"):
                # self.pix.load(self.path + "\\" + file)
                # self.pix.save(self.path + "\\new_" + file)
                print(self.path + "\\" + file)
                cmd = r'{} -ow -rem allb -reduce {}'.format(exe, self.path + "\\" + file)
                os.system(cmd)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    form.convertFiles()
    sys.exit(app.exec_())