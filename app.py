from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return "Hello your_name_roll_no!"

if __name__ == '__main__':
    app.run('localhost', 4449)