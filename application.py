import os
import sqlite3
from flask_mail import Mail, Message

from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

from flask_session import Session

import datetime

# initialize the app
app = Flask(__name__)

# initialize the database
# conn = sqlite3.connect('database.db')

# create cursor object for database manipulation
# db = conn.cursor()

""" This section is for future development
# Configure the mail parameters
app.config['MAIL_SSERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
"""

# Homepage displaying hero image and other website sections
@app.route('/')
def index():
    return render_template("index.html")

# Page that displays Degrees, certificates, and other coursework
@app.route('/education')
def education():
    return render_template("education.html")

# A page displaying projects completed
@app.route('/projects')
def projects():
    return render_template("projects.html")

# A landing page with links to other, non-tech works
@app.route('/other')
def other():
    return render_template("other.html")

"""
@app.route('/contact, methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        first_name = request.form['first']
        last_name = request.form['last']
        email = request.form['email']
        message = request.form['message']

        if not first_name or not first_name.strip():
            error = 'First name is missing'
        if not last_name or not last_name.strip():
            error = 'Last name is missing'
        if not email or not email.strip() or '@' not in email:
            error = 'email is either missing or not valid'

        msg = Message(message, sender=email, recipients=['email@gmail.com'])

        mail.send(msg)

        return render_template("thanks.html")
    
    elif request.method == 'GET':
        return render_template("contact.html")
        """

"""
# A route for the personal blog.
@app.route('/blog')
def blog():
    pass
"""

if __name__ == '__main__':
    app.run()