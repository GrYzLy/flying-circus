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

    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if not is_logged_in():
        return redirect(url_for('index'))

    question = list(data.questions.items())[session['question_count']]
    return render_template('test.html', question=question)


@app.route('/submit_question', methods=['POST'])
def submit_question():
    if not is_logged_in():
        return redirect(url_for('index'))
    question = list(data.questions.items())[session['question_count']]
    answers = list(question[1].items())

    if 'answer' in request.form:
        try:
            converted_answer = int(request.form['answer'])
        except ValueError:
            pass
        else:
            if answers[converted_answer][1]:
                session['points'] += 1

    session['question_count'] += 1

    if session['question_count'] > 4:
        return redirect(url_for('result'))

    return redirect(url_for('test'))

@app.route('/result')
def result():
    if not is_logged_in():
        return redirect(url_for('index'))

    return render_template('result.html')


# helper methods
def has_authenticated():
    return is_existing_user() and is_password_ok()


def is_existing_user():
    return request.form['email'] in data.users


def is_password_ok():
    actual_password = data.users[request.form['email']]
    received_password = request.form['password'].encode('utf-8')

    return bcrypt.checkpw(received_password, actual_password)


def is_logged_in():
    return 'email' in session

def set_session_data():
    session['email'] = request.form['email']
    session['question_count'] = 0
    session['points'] = 0


if __name__ == '__main__':
    app.run()
