import RPi.GPIO as GPIO
import time

swPin = 24
ledPin = 7
flag = False
buzzerPin = 13
melody = 523

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)

def callbackfunc(channel):
	global flag
	print("Interrupt!!")
	if flag == False:
		flag = True
	elif flag == True:
		flag = False

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)

try:
	while True:
		buzz. start(50)
		if flag == True:
			GPIO.output(ledPin, True)
			time.sleep(0.3)
			GPIO.output(ledPin, False)
			time.sleep(0.3)
			buzz.ChangeFrequency(melody)
			time.sleep(0.3)
		elif flag == False:
			GPIO.output(ledPin, False)
			buzz.stop()
	buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
