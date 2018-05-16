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
from forms import *

# Init the application
app = Flask(__name__)
port = 5000

# DB Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = "random_large_int"
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(15))
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    password = db.Column(db.String(80))

# Routes
@app.route('/')
def index():

    name = 'Rob'

    return render_template('index.html', **locals())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                print("Logged {} {} in".format(current_user.first_name,
                                               current_user.last_name))
                return redirect(url_for('dashboard'))
            else:
              print("Something is wrong with this login info...")
              return redirect(url_for('login'))
        else:
            print("This isn't a user...")
            render_template('login.html', **locals())

    return render_template('login.html', **locals())

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', **locals())

@app.route('/articles')
def articles():

    # TODO: articles.html needs to be built
    return render_template('articles.html')

@app.route('/logout')
@login_required
def logout():
    return render_template('index.html')

# Run the server
app.run(port=port)
