from flask import Flask, render_template, request, flash, redirect, url_for
import calendarHelper
import tables
import login

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if not login.checkUser(request.form['username'], request.form['password']):
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template("index.html", error=error)

@app.route('/home')
def home():
    return render_template("Home.html", month=calendarHelper.getCurMonth())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
