# Cheating
Wait for us to go through this together during our lesson. I'm posting in advance for the ease of having it done ahead of time. Essentially, consider this file the "walkthrough".

## Structure
First, we'll create the file structure. Your terminal tab/window should already be in the repo. From here, let's set up the sub-directories:

  ```Shell
  $ mkdir main && cd main
  $ mkdir static
  $ mkdir templates
  $ touch app.py
  ```
These commands have created a folder to hold all of our files for the application and the application file itself. In order to keep things organized, we'll create another file later on to house web-forms and a few other modules, but the majority of our code will live in `app.py`.

## Imports
At this point, we're ready to start building the application (server) itself. Start by bringing in the imports that we'll need:

  ```Python
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
  ```

I know this seems like a lot, but these libraries eliminate the need for us to write a lot of our own code that would just be boilerplate/reinventing the wheel. Like this [cartoon](https://plus.google.com/114528699166048052030/posts/QnTABxy8rrw) illustrates, these open source libraries make incredibly easy to develop our own applications.

## STOPPING Here
Before we actually start building the app during our code-along, I'm going to stop the guide. I'd like for us to work together before I put the rest of this walkthrough up for your reference later on. See you guys on Thursday.

-RD
