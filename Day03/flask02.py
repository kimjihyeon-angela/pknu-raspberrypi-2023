# Flask 웹 서버
from flask import Flask, render_template
# Flask => Class, render_template => 함수

app = Flask(__name__)

@app.route('/hello') #http://localhost:5000/hello
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True) # port번호가 8000으로 바뀜