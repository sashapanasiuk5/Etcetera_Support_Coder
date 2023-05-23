from flask import Flask
from main import Task

app = Flask(__name__)

@app.route("/")
def hello_world():
    Task()
    return 'Task Done!'

if __name__ == '__main__':
	app.run(port=8000,debug=True)