from flask import Flask, render_template, request, redirect, url_for, session

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


def has_authenticated():
    is_existing_user = True
    is_password_ok = True

    return is_existing_user and is_password_ok


def set_session_data():
    session['email'] = request.form['email']
    session['question_count'] = 0
    session['points'] = 0

@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()