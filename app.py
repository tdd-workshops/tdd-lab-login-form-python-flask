from flask import Flask, redirect
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home_page(title='Login Demo'):
    return render_template('login.html', title=title)

@app.route('/users', methods=['GET', 'POST'])
def login_page(title='Login Demo'):
    error = ''

    if request.method == 'POST':
        if request.form['email'] == 'demo@example.com' and request.form['password'] == 'demo1234':
            return redirect('/users/welcome')

        else:
            error = 'Invalid username/password'
            return render_template('404.html', error=error, title=title)


@app.route('/users/logout')
def logout_page(title='Logout Page'):
    error = ''

    return redirect('/')


@app.route('/users/welcome')
def welcome_page(title='Welcome Page'):
    error = ''

    return render_template('welcome.html', error=error, title=title)


if __name__ == '__main__':
    app.run()
