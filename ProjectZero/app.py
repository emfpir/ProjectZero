from flask import Flask
from controllers import front_controller as fc

app = Flask(__name__)

fc.route(app)

if __name__ == '__main__':
    app.run(debug=True)
