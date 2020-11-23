from flask import Flask, redirect
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home_page(title="Home Page"):
    return render_template('home.html', title=title)


@app.route('/users', methods=['GET', 'POST'])
def login_page():
    error = ''
    title = 'Login Page'

    if request.method == 'GET':
        return render_template('login.html', error=error, title=title)

    if request.method == 'POST':
        title = 'User Authentication'

        if request.form['email'] == 'demo@example.com' and request.form['password'] == 'demo1234':
            return redirect('/users/welcome')

        else:
            error = 'Invalid username/password'
            return render_template('404.html', error=error, title=title)


@app.route('/users/logout')
def logout_page():
    error = ''
    title = 'Logout Page'

    return render_template('logout.html', error=error, title=title)


@app.route('/users/welcome')
def welcome_page():
    error = ''
    title = 'Welcome Page'

    return render_template('welcome.html', error=error, title=title)


if __name__ == '__main__':
    app.run()
