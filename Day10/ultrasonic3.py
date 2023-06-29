import RPi.GPIO as GPIO
import time

buzzPin=13
TRIG = 21
ECHO = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(buzzPin,GPIO.OUT)
print("초음파 거리 측정기")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

buzz=GPIO.PWM(buzzPin,440)

GPIO.output(TRIG,False)
print("초음파 출력 초기화")
time.sleep(2)

try:
  while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    buzz.stop()
    a = 0.2
    while GPIO.input(ECHO)==0:
      start = time.time()

    while GPIO.input(ECHO)==1:
      stop = time.time()

    cheak_time = stop - start
    distance = cheak_time * 34300 / 2

    if distance < 7:
      buzz.start(50)
      buzz.ChangeFrequency(1000)
      print("Distance : %.1f cm " %distance)
      time.sleep(0.1)
      buzz.stop()
      time.sleep(0.1)
    elif distance < 30:
      buzz.start(50)
      buzz.ChangeFrequency(500)
      print("Distance : %.1f cm " %distance)
      time.sleep(0.3)
      buzz.stop()
      time.sleep(0.3)
    elif distance < 50:
      buzz.start(50)
      buzz.ChangeFrequency(300)
      print("Distance : %.1f cm " %distance)
      time.sleep(0.5)
      buzz.stop()
      time.sleep(0.5)
    else:
      print("Distance : %.1f cm " %distance)

except KeyboardInterrupt:
	print("거리 측정 완료")
	GPIO.cleanup()
