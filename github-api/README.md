# Github API
# Write a RestAPI to Query GitHub

from flask import Flask
app = Flask(__name__)

@app.route('/v1/get)
def get():
	return 'test'

if __name == '__main__':
	app.run()
