# LED 깜빡이기
import RPi.GPIO as GPIO
import time

signal_pin = 18 # 시그널을 받아야 하는 핀 번호

# GPIO.setmode(GPIO.BOARD) # 1 - 40
GPIO.setmode(GPIO.BCM) # GPIO 18, GROUND
GPIO.setup(signal_pin, GPIO.OUT) # GPIO 18번 핀에 출력 설정

while (True):
    GPIO.output(signal_pin, True) # GPIO 18번 핀에 전압 시그널 ON
    time.sleep(2)
    GPIO.output(signal_pin, False) # GPIO 18번 핀에 전압 시그널 OFF
    time.sleep(1)