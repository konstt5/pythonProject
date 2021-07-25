import sys, random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from threading import Timer

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = QtGui.QColor(r, g, b)
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)

class Window(QMainWindow):
    resized = QtCore.pyqtSignal()  # 1

    def __init__(self):
        super(Window, self).__init__()
        self.Balls = []
        self.r = 20
        self.setupUi(self)
        self.timerEvent()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(500, 300)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PaintBox = QtWidgets.QLabel(self.centralwidget)
        self.PaintBox.setGeometry(QtCore.QRect(10, 40, 780, 550))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PaintBox.sizePolicy().hasHeightForWidth())
        self.PaintBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        self.PaintBox.setFont(font)
        self.PaintBox.setFrameShape(QtWidgets.QFrame.Box)
        self.PaintBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PaintBox.setText("")
        self.PaintBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PaintBox.setObjectName("PaintBox")
        # self.pixmap = QtGui.QPixmap()
        # self.PaintBox.setPixmap(self.pixmap)
        self.NumLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumLabel.setGeometry(QtCore.QRect(10, 10, 131, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.NumLabel.setFont(font)
        self.NumLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.NumLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NumLabel.setTextFormat(QtCore.Qt.RichText)
        self.NumLabel.setObjectName("NumLabel")
        self.SpeedSlider = QtWidgets.QSlider(self.centralwidget)
        self.SpeedSlider.setGeometry(QtCore.QRect(210, 10, 160, 22))
        self.SpeedSlider.setMinimum(1)
        self.SpeedSlider.setMaximum(100)
        self.SpeedSlider.setSliderPosition(1)
        self.SpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SpeedSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.SpeedSlider.setTickInterval(0)
        self.SpeedSlider.setObjectName("SpeedSlider")
        self.SpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpeedLabel.setGeometry(QtCore.QRect(150, 10, 61, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.SpeedLabel.setFont(font)
        self.SpeedLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SpeedLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SpeedLabel.setTextFormat(QtCore.Qt.RichText)
        self.SpeedLabel.setObjectName("SpeedLabel")
        self.GravBox = QtWidgets.QSpinBox(self.centralwidget)
        self.GravBox.setGeometry(QtCore.QRect(450, 10, 42, 22))
        self.GravBox.setWrapping(False)
        self.GravBox.setFrame(True)
        self.GravBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.GravBox.setMaximum(300)
        self.GravBox.setSingleStep(10)
        self.GravBox.setDisplayIntegerBase(10)
        self.GravBox.setObjectName("GravBox")
        self.GravLabel = QtWidgets.QLabel(self.centralwidget)
        self.GravLabel.setGeometry(QtCore.QRect(380, 10, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.GravLabel.setFont(font)
        self.GravLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GravLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GravLabel.setTextFormat(QtCore.Qt.RichText)
        self.GravLabel.setObjectName("GravLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        self.setWindowTitle("Прыгающие мячики")
        self.NumLabel.setText(f"Количество шаров: {len(self.Balls)}")
        self.SpeedLabel.setText("Скорость:")
        self.GravLabel.setText("Гравитация:")

    def resizeForm(self):
        g = self.geometry()
        self.PaintBox.setGeometry(QtCore.QRect(10, 40, g.width() - 20, g.height() - 50))

    def paintEvent(self, event):
        self.drawBalls()

    def resizeEvent(self, event):
        self.resizeForm()
        self.resized.emit()
        return super(Window, self).resizeEvent(event)

    def closeEvent(self, event):
        self.timer.cancel()

    def timerEvent(self):
        self.moveBalls()
        self.update()
        self.timer = Timer(0.05, self.timerEvent)
        self.timer.start()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x = event.x() - (self.r // 2)
            y = event.y() - (self.r // 2)
            g = self.PaintBox.geometry()
            if (x < g.x()) or (x + (self.r // 2) + 2 > g.width()) \
                    or (y < g.y()) or (y + (self.r // 2) + 2 > (g.height() + 30)):
                return

            self.addBall(x, y)
            self.retranslateUi()
            self.update()

    def addBall(self, x, y):
        self.Balls.append(Ball(x, y))

    def moveBalls(self):
        for Ball in self.Balls:
            Ball.vy = Ball.vy - self.GravBox.value() / 100

            dx = Ball.vx * self.SpeedSlider.value() // 10
            dy = int(Ball.vy * self.SpeedSlider.value() // 10)

            if abs(dx) <= 1 and Ball.vx >= 0:
                dx = 1
            elif abs(dx) <= 1 and Ball.vx < 0:
                dx = -1
            if abs(dy) <= 1 and Ball.vy >= 0:
                dy = 1
            elif abs(dy) <= 1 and Ball.vy < 0:
                dy = -1

            Ball.x = Ball.x + dx
            Ball.y = Ball.y - dy

            g = self.PaintBox.geometry()

            if (Ball.x < g.x()):
                Ball.x = 2 * g.x() - Ball.x
                Ball.vx = -Ball.vx
            elif (Ball.x + (self.r // 2) + 2 > g.width()):
                Ball.x = 2 * (g.width() - self.r // 2 - 2) - Ball.x
                Ball.vx = -Ball.vx

            if (Ball.y < g.y()):
                Ball.y = 2 * g.y() - Ball.y
                Ball.vy = -Ball.vy
            elif (Ball.y + (self.r // 2) + 2 > (g.height() + 30)):
                Ball.y = 2 * (g.height() + 30 - self.r // 2 - 2) - Ball.y
                Ball.vy = -Ball.vy

    def drawBalls(self):
        qp = QtGui.QPainter(self)
        for Ball in self.Balls:
            # qp.setPen(QtGui.QPen(Ball.color, 1))
            qp.setBrush(Ball.color)
            qp.drawEllipse(Ball.x, Ball.y, self.r, self.r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())