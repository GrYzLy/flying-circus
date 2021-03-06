from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
# sprawdź rodzaj komunikatu, i zwróć message z rodzajem metody HTTP
    message = ''
    if request.method == 'POST':
        message = 'POST'
    else:
        message = 'GET'

    return render_template('login.html', message=message)


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()