from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt

import data

app = Flask(__name__)

app.secret_key = 'NOT_SO_SECRET'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        if has_authenticated():
            set_session_data()
            return redirect(url_for('index'))
        else:
            message = 'Wrong password'

    return render_template('login.html', message=message)


@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('question_count', None)
    session.pop('points', None)


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/test')
def test():
    return render_template('test.html')


def has_authenticated():
    return is_existing_user() and is_password_ok()


# helper methods
def is_existing_user():
    return request.form['email'] in data.users


def is_password_ok():
    actual_password = data.users[request.form['email']]
    received_password = request.form['password']

    return bcrypt.checkpw(received_password, actual_password)


def set_session_data():
    session['email'] = request.form['email']
    session['question_count'] = 0
    session['points'] = 0


if __name__ == '__main__':
    app.run()
