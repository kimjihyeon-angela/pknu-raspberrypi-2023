import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 21
ECHO=20
buzzPin = 13
melody = 1000

GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("초음파 출력 초기화")
time.sleep(2)

buzz = GPIO.PWM(buzzPin, 440)

try:
	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO)==0:
		 	start = time.time()
		while GPIO.input(ECHO)==1:
			stop = time.time()
		check_time = stop-start

		distance = check_time * 34000 / 2
		print("Distance : %.2f cm", distance)
		time.sleep(0.4)

		if (distance <=40 and distance > 25):
			buzz.start(50)
			buzz.ChangeFrequency(melody)
			time.sleep(0.3)
			buzz.stop()
			time.sleep(0.3)
		elif(distance <= 25 and distance >10):
			buzz.start(50)
			buzz.ChangeFrequency(melody)
			time.sleep(0.15)
			buzz.stop()
			time.sleep(0.1)
		elif(distance <=10):
			buzz.start(99)
			buzz.ChangeFrequency(melody)
			time.sleep(1)
			buzz.stop()
			time.sleep(0.05)
		else:
			buzz.stop()
			time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
