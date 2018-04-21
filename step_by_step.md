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

I know this seems like a lot, but these libraries eliminate the need for us to write a lot of our own code that would just be boilerplate/reinventing the wheel. Like this [cartoon](https://plus.google.com/114528699166048052030/posts/QnTABxy8rrw) illustrates, these open source libraries make it incredibly easy to develop our own applications.

## Initialize the Application
The first thing we need to do is actually create the application as a flask object:

  ```Python
  # Init the application
  app = Flask(__name__)
  port = 5000
  ```

## First Endpoint
An endpoint is essentially a URL, or a web service endpoint. There are different protocols (HTTP requests) we can call such as `GET` and `POST` in order to have different functions triggered. The simplest is our index's endpoint which we'll just assign `(/)`:

  ```Python
  @app.route('/')
  def index():
      return render_template('index.html')
  ```
What we're saying here is when a user navigates to the url ending with `/`, regardless of the request method, our server will just return `index.html`. Each endpoint gets its own function - in the example above, it's `index()` that is called whenever the request is made. Later on, we'll look at triggering different blocks of code depending on the type of request that's made.

## Run the Server
Couldn't be easier with flask. All we do is utilize the `.run` method for the application object, feed it the port (which is an optional argument, btw), and we'll have an up-running-server:

  ```Python
  app.run(port=port)
  ```

At this point, our whole `app.py` would look like this:

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

  # Init the application
  app = Flask(__name__)
  port = 5000

  # Routes
  @app.route('/')
  def index():
      return render_template('index.html')

  # Run the server
  app.run(port=port)
  ```

If we went to our terminal and tried to run the server, we'd have an issue when trying to navigate to `localhost:5000` because we haven't actually built the html page that's trying to be served to us; we'd get a `500` response code. If you haven't made yourself familiar with HTTP response codes, [this](https://pbs.twimg.com/media/B50dCAKIEAAP0NQ.jpg) is helpful and from the perspective of the server/developer.

Before running the server for the first time, create an `index.html` file in your `templates` folder. Now, if you run the following command, you should get some output that let's you know your server is up and listening on port `5000`:

  ```Shell
  $ python app.py

  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

  If you open a web-browser and navigate to `http://127.0.0.1:5000/` you should get a response that reads something like the following, but with the current date/time:

  ```Shell
  127.0.0.1 - - [21/Apr/2018 12:49:54] "GET / HTTP/1.1" 200 -
  ```



## STOPPING Here
Before we actually start building the app during our code-along, I'm going to stop the guide. I'd like for us to work together before I put the rest of this walkthrough up for your reference later on. See you guys on Thursday.

-RD
