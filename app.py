from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

#registration
@app.route('/registration', methods=['POST'])
def registration():
    return 'You are registered!', 200


if __name__ == '__main__':
    app.run()
