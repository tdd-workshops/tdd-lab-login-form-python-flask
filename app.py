from flask import Flask, redirect
from flask import request
from flask import render_template
import csv
import os

import db

app = Flask(__name__)

@app.route('/')
def home_page(title='Welcome to the Login Form Demo!'):
    return render_template('login.html', title=title)

@app.route('/signin', methods=['GET', 'POST'])
def login_page(title='Login Demo'):
    error = ''

    if request.method == 'GET':
        return render_template('login.html', error=error, title=title)

    elif request.method == 'POST':
        if any(request.form['email'] == email and request.form['password'] == password
                for _, email, password in db.get_all_employees()):
            return redirect('/users/welcome')

        else:
            error = 'Invalid username/password'
            return render_template('login.html', errorMsg=error, title=title)


@app.route('/users/logout')
def logout_page(title='Logout Page'):
    error = ''

    return redirect('/')


@app.route('/signup', methods=['GET', 'POST'])
def signup_page(title='Signup Page'):
    error = ''
    user_data = {}

    if request.method == 'GET':
        return render_template('signup.html', error=error, title=title)

    elif request.method == 'POST':
        if request.form['email'] != '' and request.form['username'] != '' and \
                request.form['password'] == request.form['password_confirm']:
            user_data = dict(request.form)

            db.insert_employee(user_data['username'], user_data['email'], user_data['password'])

            return redirect('/users/welcome')
        else:
            error = 'Invalid user registration'
            return render_template('signup.html', errorMsg=error, title=title)


@app.route('/users/welcome')
def welcome_page(title='Welcome back!'):
    error = ''

    return render_template('welcome.html', error=error, title=title)


if __name__ == '__main__':
    app.run()