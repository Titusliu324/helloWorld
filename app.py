from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Titus Liu!'

@app.route('/hello')
def hello():  # put application's code here
    return render_template("hello.html")

@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")

if __name__ == '__main__':
    app.run()

