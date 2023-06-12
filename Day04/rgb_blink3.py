# LED RGB 깜빡이기
# 전압이 5v가 들어가진 경우 True, False가 반대로 되어야 함
import RPi.GPIO as GPIO
import time

# is_run = True
red = 17
green = 27
blue = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

# 초기화
GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True)

# 불 들어오는 부분
try:
    while(True):
        # Red + Green = Yellow
        # Red + Blue = Pink
        # Green + Blue = SkyBlue
        # Red + Green + Blue = White

        # Yellow
        GPIO.output(red, False)
        GPIO.output(blue, True)
        GPIO.output(green,False)
        time.sleep(1)

        # Pink
        GPIO.output(green, True)
        GPIO.output(red, False)
        GPIO.output(blue, False)
        time.sleep(1)

        # SkyBlue
        GPIO.output(blue, False)
        GPIO.output(green, False)
        GPIO.output(red, True)
        time.sleep(1)

        # White
        GPIO.output(blue, False)
        GPIO.output(green, False)
        GPIO.output(red, False)
        time.sleep(1)
        
except KeyboardInterrupt :
    GPIO.cleanup()