from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#registration
@app.route('/registration', methods=['POST'])
def registration():
#    return 'You are ' + request.form['username'] + ' ' + request.form['password']

    if createUser(request.form['username'], request.form['password']):
        return 'yeah haaahhh', 200
    else:
        return 'Ohh nooo', 400

def createUser(username, password):
    if (username == 'xxx'):
        return False
    else:
        return True


if __name__ == '__main__':
    app.run()
