# LED RGB 중 Red 깜빡이기 확인하기 위함
# True/False가 반대로 돼야함을 확인함

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

GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True)

try:
    while(True):
        GPIO.output(red,False) # Red 켜짐
        time.sleep(1)
        GPIO.output(red, True)
        time.sleep(1)
        
except KeyboardInterrupt :
    GPIO.cleanup()