import RPi.GPIO as GPIO
import time

buzzer = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

scale = [131, 147, 165, 175, 196, 220, 247, 262]
twinkle = [1,1,5,5,6,6,5,4,4,3,3,2,2,1,
					 5,5,4,4,3,3,2,5,5,4,4,3,3,2,
					 1,1,5,5,6,6,5,4,4,3,3,2,2,1]
buzz = GPIO.PWM(buzzer, 440)

try:
	while True:
		buzz.start(50)
		for i in range(0,42):
			buzz.ChangeFrequency(scale[twinkle[i]])
			if i==6 or i==13 or i==20 or i==27 or i==34 or i==41:
				time.sleep(1)
			else:
				time.sleep(0.5)
		buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
