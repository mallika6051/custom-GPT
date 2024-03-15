from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def name():
    return 'welcome'
@app.route('/index')
def index():
    courses = ["C", "C++", "Java", "Python", "HTML", "CSS"]
    is_logged_in = False
    # return render_template("index.html", courses=courses, is_logged_in=is_logged_in)
    return courses

@app.route('/about/hi/hello/')
def about():
    return '<h3>Hi! Welcome</h3>'


@app.route('/contact')
def contact():
    return '<h3>Contact Us</h3>'


@app.route('/users/<name>')
def users(name):
    # return  "<h3>Welcome {}</h3>".format(name.upper())
    fruits = ["Apple", "Orange", "Pineapple"]
    profile = {"name": "Mallika", "age": 25, "City": "Chennai"}
    return render_template("users.html", user_name=name, fruits=fruits, profile=profile)


if __name__ == '__main__':
    app.run(debug=True)
