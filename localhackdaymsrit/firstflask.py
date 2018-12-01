from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
	return 'hello flask!'
app.run(port=5000)
