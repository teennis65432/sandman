from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
import src.calendarHelper as calendarHelper
import src.tables as tables


LM = LoginManager()
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.database'

LM.init_app(app)
db.init_app(app)

@LM.user_loader
def load_user(user_id):
    return tables.getUser(user_id)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if not tables.checkLogin(request.form['username'], request.form['password']):
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template("index.html", error=error)

@app.route('/home')
def home():
    return render_template("Home.html", month=calendarHelper.getCurMonth())

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
