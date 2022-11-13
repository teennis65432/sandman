from flask import Flask, render_template, request, flash, redirect
import calendarHelper
import tables

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("Home.html", month=calendarHelper.getCurMonth())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
