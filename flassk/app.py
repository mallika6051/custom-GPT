from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/register')
def index():
    return render_template("register.html")

@app.route('/confim', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        n=request.form.get('name')
        a=request.form.get('age')
        d=request.form.get('domain')
        return render_template("confirm.html", name=n, age=a, domain=d)

if __name__ == '__main__':
    app.run(debug=True)

