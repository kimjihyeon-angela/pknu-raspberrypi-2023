import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
buzzerPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)

melody = [262, 294, 330, 349, 392, 440, 494]

def buzz_Freq(Piano):
	# print("숫자 : %d 입력" , Piano)
	buzz.ChangeFrequency(Piano)
	time.sleep(0.3)
	buzz.stop()

try:
	while True:
		key = int(input())
		buzz.start(50)
		if (key == 1):
			buzz_Freq(melody[0])

		elif (key == 2):
			buzz_Freq(melody[1])

		elif (key == 3):
			buzz_Freq(melody[2])

		elif (key == 4):
			buzz_Freq(melody[3])

except KeyboardInterrupt:
	GPIO.cleanup()
