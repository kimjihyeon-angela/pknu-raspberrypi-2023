import sys
import RPi.GPIO as GPIO
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

ledPin = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

class qtApp(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('./pyQt1.ui')
		self.show()

		self.btnledOn.clicked.connect(self.btnledOnClicked)
		self.btnledOff.clicked.connect(self.btnledOffClicked)
		self.btnbuzzerOn.clicked.connect(self.btnbuzzerOnClicked)
		self.btnbuzzerOff.clicked.connect(self.btnbuzzerOffClicked)

	def btnledOnClicked(self):
		while True:
			GPIO.output(ledPin, True)
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = qtApp()
	ex.show()
	sys.exit(app.exec_())
