from flask import Flask, redirect
from flask import request
from flask import render_template
import csv
import os

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
        if request.form['email'] == 'demo@example.com' and request.form['password'] == 'demo1234':
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
    root = os.path.dirname(os.path.realpath(__file__))
    directory = 'db'
    filename = 'user_db.csv'
    user_data = {}

    if request.method == 'GET':
        return render_template('signup.html', error=error, title=title)

    elif request.method == 'POST':
        if request.form['email'] != '' and request.form['username'] != '' and \
                request.form['password'] == request.form['password_confirm']:
            user_data = dict(request.form)

            with open(f'{root}/{directory}/{filename}', mode='w') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow([user_data['username'], user_data['email'], user_data['password']])

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