import RPi.GPIO as GPIO
import time

buzzerPin = 13
melody = [262, 294, 330, 349, 392, 440, 494, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)
try:
  while True:
    cmd = input('숫자입력 (1 ~ 7)')
    cmd = int(cmd)
    print(cmd)
    if cmd == 0:
      buzz.stop()
    else:
      if cmd > 8:
        buzz.stop()
        print('범위를 벗어났습니다.')
      else:
        buzz.start(50)
        buzz.ChangeFrequency(melody[cmd-1])
        time.sleep(0.3)
        print(melody[cmd-1])

except KeyboardInterrupt:
  GPIO.cleanup()

