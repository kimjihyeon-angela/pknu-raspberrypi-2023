import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
buzzerPin = 13
melody = [131, 147, 165, 175, 196, 220, 247, 262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440) 			# 440Hz를 갖는 객체 생성

try:
	while True:
		buzz.start(50)										# duty cycle 50으로 pwm 출력 시작
		for i in range(0, len(melody)):
			buzz.ChangeFrequency(melody[i]) # 주파수 변경
			time.sleep(0.3)
		buzz.stop()											  # pwm 종료 
		time.sleep(1)
except KeyboardInterrupt:							# 키보드인터럽트
	GPIO.cleanup()
