import os
import sqlite3

from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

from flask_session import Session

import datetime

# initialize the app
app = Flask(__name__)

# initialize the database
conn = sqlite3.connect('database.db')

# create cursor object for database manipulation
db = conn.cursor()

# Homepage displaying hero image and other website sections
@app.route("/")
def index():
    return render_template("index_2.html")

# Page that displays Degrees, certificates, and other coursework
@app.route("/education")
def education():
    return render_template("education.html")

# A page displaying projects completed
@app.route("/projects")
def projects():
    return render_template("projects.html")

# A landing page with links to other, non-tech works
@app.route("/other")
def other():
    return render_template("other.html")


# A route for the personal blog.
@app.route("/blog")
def blog():
    pass