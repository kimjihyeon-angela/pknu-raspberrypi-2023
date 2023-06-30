import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import RPi.GPIO as GPIO
import time

count = 0
ledPin = 7
buzzerPin = 13
melody = [131, 147, 165, 175, 196, 220, 147, 262]
twinkle = [1,1,5,5,6,6,5,4,4,3,3,2,2,1,
		   5,5,4,4,3,3,2,5,5,4,4,3,3,2,
		   1,1,5,5,6,6,5,4,4,3,3,2,2,1]
OnPin = [[22,27,14,15,18,10],
         [27,14],
         [22,27,9,18,15],
         [22,27,9,14,15],
         [10,9,27,14],
         [22,10,9,14,15],
         [22,10,9,14,15,18],
         [22,27,14],
         [9,10,22,27,18,15,14],
         [22,10,27,9,14]]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)  # G
GPIO.setup(10, GPIO.OUT) # F
GPIO.setup(22, GPIO.OUT) # A
GPIO.setup(27, GPIO.OUT) # B
GPIO.setup(18, GPIO.OUT) # E
GPIO.setup(15, GPIO.OUT) # D
GPIO.setup(14, GPIO.OUT) # C
buzz = GPIO.PWM(buzzerPin, 440)

class qtApp(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('/home/pi/sources/pknu_raspberrypi_2023/Day12/pyQt2.ui', self)
		self.setWindowTitle('스마트홈 케어 v0.5')

		# 버튼 시그널/슬롯 함수 지정
		self.BtnLedOn.clicked.connect(self.BtnLedOnClicked)
		self.BtnLedOff.clicked.connect(self.BtnLedOffClicked)
		self.BtnBuzzerScale.clicked.connect(self.BtnBuzzerScaleClicked)
		self.BtnBuzzerTwinkle.clicked.connect(self.BtnBuzzerTwinkleClicked)
		self.BtnCount0.clicked.connect(self.BtnCount0Clicked)
		self.BtnCount1.clicked.connect(self.BtnCount1Clicked)
		self.BtnCount2.clicked.connect(self.BtnCount2Clicked)
		self.BtnCount3.clicked.connect(self.BtnCount3Clicked)
		self.BtnCount4.clicked.connect(self.BtnCount4Clicked)
		self.BtnCount5.clicked.connect(self.BtnCount5Clicked)
		self.BtnCount6.clicked.connect(self.BtnCount6Clicked)
		self.BtnCount7.clicked.connect(self.BtnCount7Clicked)
		self.BtnCount8.clicked.connect(self.BtnCount8Clicked)
		self.BtnCount9.clicked.connect(self.BtnCount9Clicked)
		self.BtnCountAuto.clicked.connect(self.BtnCountAutoClicked)
		self.BtnCountOff.clicked.connect(self.BtnCountOffClicked)

	def BtnLedOnClicked(self):
		GPIO.output(ledPin,True)
		print("불이 켜졌습니다.")

	def BtnLedOffClicked(self):
		GPIO.output(ledPin,False)
		print("불이 꺼졌습니다.")

	def BtnBuzzerScaleClicked(self):
		print("음계를 노래합니다")
		buzz.start(50)										# duty cycle 50으로 pwm 출력 시작
		for i in range(0, len(melody)):
			buzz.ChangeFrequency(melody[i]) # 주파수 변경
			time.sleep(0.3)
		buzz.stop()											  # pwm 종료 
		time.sleep(1)

	def BtnBuzzerTwinkleClicked(self):
		print("작은별을 노래합니다")
		try:
			while True:
				buzz.start(50)
				for i in range(0,42):
					buzz.ChangeFrequency(melody[twinkle[i]])
					if i==6 or i==13 or i==20 or i==27 or i==34 or i==41:
						time.sleep(1)
					else:
						time.sleep(0.5)
				buzz.stop()

		except KeyboardInterrupt:
			GPIO.cleanup()

	def BtnCount0Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[0], True)

	def BtnCount1Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[1], True)

	def BtnCount2Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[2], True)

	def BtnCount3Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[3], True)

	def BtnCount4Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[4], True)

	def BtnCount5Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[5], True)

	def BtnCount6Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[6], True)

	def BtnCount7Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[7], True)

	def BtnCount8Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[8], True)

	def BtnCount9Clicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		GPIO.output(OnPin[9], True)

	def BtnCountAutoClicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)
		global count
		if count == 10:
			count = 0
		else:
			for i in range(len(OnPin[count])):
				GPIO.output(OnPin[count][i], True)
			count = count + 1
			
		time.sleep(0.1)

	def BtnCountOffClicked(self):
		GPIO.output([9, 10, 22, 27, 18, 15, 14], False)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = qtApp()
	ex.show()
	sys.exit(app.exec_())
