from flask import Flask, request, render_template
import RPi.GPIO as GPIO
ledPin = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def home():
	return "Hi~ This is Home"

@app.route('/led/on')
def led_on():
	try:
		GPIO.output(ledPin, GPIO.HIGH)
		return 'ok'
	except:
		return 'fail'

@app.route('/led/off')
def led_off():
    try:
        GPIO.output(ledPin, GPIO.LOW)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route('/led')
def led_onoff():
	return render_template('led2.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='1234', debug=True)
	
