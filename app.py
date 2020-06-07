from time import strftime, gmtime

import users as users
from flask import Flask
from flask import request
import redis
import json
from flask import jsonify
import random
import string
from datetime import datetime, timedelta

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)
Users = {'id', 'username', 'password'}


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


# registration
@app.route('/registration', methods=['POST'])
def registration():
    if create_user(request.form['id'], request.form['username'], request.form['password']):
        print(r.hvals('Users'))
        return 'yeah haaahhh', 200

    else:
        return 'Ohh nooo', 400


def create_user(id, username, password):
    new_user = {'id': id, 'username': username, 'password': password}
    r.hmset('Users', new_user)
    return True


# list of all users
@app.route('/users', methods=['GET'])
def users():
    print(r.hgetall('Users'))
    return jsonify(str(r.hvals('Users')))

# login functionality
@app.route('/login', methods=['POST'])
def login():

    start_time = datetime.now()

    expire_time = datetime.now() + timedelta(minutes = +30)

    letters = 'abcdefghyjklmnopqrstuvwxyz1234567890'

    if check_user(request.form['username'], request.form['password']):
        print('Now is ' + str(start_time))
        print('Token expires at ' + str(expire_time))
        return ''.join(random.choice(letters) for i in range(32))
    else:
        return 400

def check_user(username, password):
    if username is not None and password is not None:
        return True, 200
    else:
        return False, 400


if __name__ == '__main__':
    app.run()
