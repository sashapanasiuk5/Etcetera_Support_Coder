from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<h1>Hello World</h1>"
    subprocess.call("test.py", shell=True)

if __name__ == '__main__':
	app.run(port=8000,debug=True)