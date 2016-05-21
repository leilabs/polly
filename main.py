from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h2>polly wants a cracker</h2>'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')