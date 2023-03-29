from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Titus Liu!'

@app.route('/hello')
def hello():

    fun_courses = ['BMGT402', 'BMGT382', 'BMGT407']

    return render_template('hello.html', courses=fun_courses)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favorite-course')
def about():
    return render_template('favorite-course.html.html')

if __name__ == '__main__':
    app.run()

