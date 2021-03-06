from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()