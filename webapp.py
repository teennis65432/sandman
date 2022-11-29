from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import src.calendarHelper as calendarHelper
import src.tables as tables

LM = LoginManager()
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.database'
app.secret_key = 'a secret shhhh'

LM.init_app(app)
db.init_app(app)

@LM.user_loader
def load_user(id):
    return tables.getUserByID(id)

@app.route('/')
def start():
    if current_user == None:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = tables.checkLogin(request.form['username'], request.form['password'])
        if user == None:
            error = 'Invalid Credentials. Please try again.'
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", error=error)

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        if "next" in request.form:
            return render_template("Home.html", month=calendarHelper.getNextMonth(), user=current_user)
        else:
            return render_template("Home.html", month=calendarHelper.getCurMonth(), user=current_user)
    return render_template("Home.html", month=calendarHelper.getCurMonth(), user=current_user)

@app.route('/home/<int:errorcode>', methods=['GET', 'POST'])
@login_required
def homeError(errorcode):
    error = None
    if errorcode == 401:
        error = 'You are not authorized to access this page'
    if errorcode == 412:
        error = 'You are trying to clock in too early'
    if errorcode == 413:
        error = 'You are trying to clock out too late'
    if request.method == 'POST':
        if "next" in request.form:
            return render_template("Home.html", month=calendarHelper.getNextMonth(), user=current_user)
        else:
            return render_template("Home.html", month=calendarHelper.getCurMonth(), user=current_user)
    return render_template("Home.html", month=calendarHelper.getCurMonth(), user=current_user, error=error)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add-employee', methods=['GET', 'POST'])
@login_required
def addEmployee():
    if not current_user.manager:
        return redirect(url_for('homeError', errorcode=401))
    if request.method == 'POST':
        manager = False
        if request.form['manager'] == 'True':
            manager = True
        tables.addUser(request.form['username'], request.form['name'], request.form['password'], manager)
        return redirect(url_for('allEmployees'))
    return render_template('add-employee.html')
    
@app.route('/all-employees')
@login_required
def allEmployees():
    if not current_user.manager:
        return redirect(url_for('homeError', errorcode=401))
    return render_template('all-employees.html', users=tables.getAllUsers())


@app.route('/remove-employee')
@login_required
def removeEmployee():
    if not current_user.manager:
        return redirect(url_for('homeError', errorcode=401))
    return render_template('remove-employee.html', users=tables.getAllUsers())
    
@app.route('/remove/<id>')
@login_required
def remove(id):
    if not current_user.manager:
        return redirect(url_for('homeError', errorcode=401))

    tables.removeUser(id)
    return redirect(url_for('removeEmployee'))

if __name__ == "__main__":
    calendarHelper.getNextMonth()
    app.run(host="127.0.0.1", port=8080, debug=True)
