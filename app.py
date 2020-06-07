from flask import Flask
from flask import request
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/')
def hello_world():
    return "Hello"


# registration
@app.route('/registration', methods=['POST'])
def registration():
    if createUser(request.form['username'], request.form['password']):
        return r.get(1)

#        if r.get(1) == 'username':
#            return 'yeah haaahhh', 200
#        else:
#            return 'Something went wrong', 400
#    else:
#        return 'Ohh nooo', 400


def createUser(username, password):
    r.set(1, username)
    return True


if __name__ == '__main__':
    app.run()
