from flask import Flask

import util

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=util.achar_porta_livre(), debug=True)