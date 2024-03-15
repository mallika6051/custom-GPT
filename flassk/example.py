# from flask import Flask
# fllask = Flask(__name__)
# @fllask.route('/hi/<name>')
# def hello_world(name):
#     return '<h2> Hi I am {} <h2>' . format(name)
#
# @fllask.route('/python')
# def domain():
#     return 'my domain is python'
# fllask.run()









from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hi! Welcome'

@app.route('/admin')
def admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def guest(guest):
    return 'hello %s guest' % guest
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))
if __name__ == '__main__':
    app.run(debug=True)
