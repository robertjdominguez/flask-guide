from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from wtforms import *
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import *
from random import *
import time
from functools import wraps

# Init the application
app = Flask(__name__)
port = 5000

# Routes


@app.route('/')
def index():

    name = 'Rob'

    return render_template('index.html', **locals())


@app.route('/articles')
def articles():

    # TODO: articles.html needs to be built
    return render_template('articles.html')


# Run the server
app.run(port=port)
