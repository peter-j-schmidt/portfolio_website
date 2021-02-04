import os

from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

from flask_session import Session

import datetime


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_2.html")

@app.route("/education", methods=["GET", "POST"])
def courses():

    if request.method == "GET":

        return render_template("courses.html")

    else:

        return render_template("courses.html")