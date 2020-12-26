import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/courses_and_certificates")
def courses_and_certificates():
    return render_template("coursework.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

if __name__=='__main__':
    app.run(debug=True)
