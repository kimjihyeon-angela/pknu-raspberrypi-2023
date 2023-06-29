from flask import Flask

app = Flask(__name__) # 객체생성

@app.route('/')

def hello_World():
	return "Hello World"

@app.route('/name')
def namefunc():
	return "Kim Ji Hyeon"

if __name__=="__main__":
	app.run(host="0.0.0.0", port="9000")
