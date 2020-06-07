import users as users
from flask import Flask
from flask import request
import redis
import json
from flask import jsonify

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)
hashUsers = 'Users'

@app.route('/')
def hello_world():
    return "Hello"


# registration
@app.route('/registration', methods=['POST'])
def registration():
    if create_user(request.form['id'], request.form['username'], request.form['password']):
        print (r.hgetall('Users'))
        return 'yeah haaahhh', 200

#        if r.get(1) == 'username':
#            return 'yeah haaahhh', 200
#        else:
#            return 'Something went wrong', 400
    else:
        return 'Ohh nooo', 400


def create_user(id, username, password):
    new_user = {'id': id, 'username': username, 'password': password}
    r.hmset('Users', new_user)
    return True


# list of all users
#@app.route('/users', methods=['GET'])
#def get_users(self):
#    print (r.hgetall('Users'))
#    return r.hgetall(self, 'Users')


if __name__ == '__main__':
    app.run()
