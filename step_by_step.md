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



## STOP Here
Before we actually start building the app during our code-along, I'm going to stop the guide. I'd like for us to work together before I put the rest of this walkthrough up for your reference later on. See you guys on Thursday.

-RD


## Organizing our application -- TODO TOGETHER
I like to map out what my app will look like by using comments. We've got a block under a comment called "`Routes`" already. Let's use that to organize the rest of our application's structure. The `flask-snippets` package that we installed helps speed up our development and keeps our syntax clean and consistent. To build an endpoint with this package, start typing `froute` and then hit enter. When you do, the endpoint found below `/` will be in your code:

![flask-snippets](https://github.com/robertjdominguez/flask-guide/blob/master/main/static/approute.gif)

Let's have our next endpoint be a page where users can find all the articles that have been written. Change the templated endpoint from `froute` to the following:

  ```Python
  @app.route('/articles')
  def articles():
    # TODO: build articles.html
    return render_template('articles.html')
  ```

Notice, I included a `TODO` comment; I did this to remind myself to come back and build this page - and others - after I've mapped out my routes. In Atom, comments are easy: just start typing `todo` and then hit enter. If your file already has an extension (i.e., .py, .js, etc.) then Atom knows what type of syntax is necessary for a comment (e.g., `#` or `//`). The `todo-show` package that we installed earlier allows us to see all of a project's `TODO` tags. Depending on your OS, you can bring this up different ways. This is a great tool to help keep us organized.

Now, go ahead and create the rest of your endpoints (articles/headlines, article, login, logout, profile, create_article) and I'll help you.

## Endpoints
Flask makes it easy to build a consistent appearance for our application. We're going to use [Bootstrap](https://getbootstrap.com/) for our site's appearance. The first thing we need to create is a file called `base.html`. This file will serve as our foundation and will contain our CSS link, jQuery, and other "every page" elements that each page on our site will need. The syntax is going to look a little weird - especially when we start utilizing loops inside of HTML - but this is a templating engine called [Jinja2](http://jinja.pocoo.org/).

Navigate to the `templates` directory and `$ touch base.html` to create the file. From there, when using Atom - and since you included the `emmet` package, doctypes like HTML are a snap to create. Just open the file in the editor and start typing `html`. When you hit enter, the skeleton of an HTML file will be generated. Even better, because of the Bootstrap 4 package we're utilizing, there's an option that will pop up titled `htmlb4` that will go ahead and take care of needed information. It should look like the code below:

```HTML
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title></title>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
  </body>
</html>
```

From here, let's delete the line with the `h1` tag and put the following in its place:

```HTML
<br>
{% block content %} <!-- This will be dynamic content depending on the page --> {% endblock %}
<br>
```

### Creating a Page
For every page that we want to feed off of the `base.html` file, we need to include the following lines in the HTML file:

```HTML
{% extends "base.html" %} {% block title %} <!-- Title can be typed here --> {% endblock %} {% block content %}

<!-- body goes here -->

{% endblock %}
```

As you can see, we can dynamically include information like the page's title, and - for each page - the body without having to rewrite everything that would be boilerplate on each page. Let's set up a title page that looks like this:

```HTML
{% extends "base.html" %} {% block title %} Home Page {% endblock %} {% block content %}

<h1>What's up, dude?</h1>

{% endblock %}
```

Go head and build the pages you need based on the endpoints you've written.

### Dynamic Content
Using Jinja, we can start to feed in dynamic information to a page's view utilizing the `app.py` file we've created. Let's "personalize" our `index.html` file; in `app.py` declare a variable `name` and assign your name to its value:

```Python
@app.route('/')
def index():

    name = 'Rob'

    return render_template('index.html')
```

Now, let's edit the `index.html` page and replace "dude" with your name:

```HTML
{% extends "base.html" %} {% block title %} Home Page {% endblock %} {% block content %}

<h1>What's up, {{ name }}?</h1>

{% endblock %}
```

If you try to run this as it's written, you're not going to get any dynamic content. When we return the `index.html` file, we need to be sure to pass local variables through as an argument. At times, this can be a lot of content; luckily, we can just use the following to catch all local variables and pass them through as arguments:

```Python
@app.route('/')
def index():

    name = 'Rob'

    return render_template('index.html', **locals())
```

## Building the DB
We're going to use SQLite3 to create this database. There's a great library that we'll be using called `flask_sqlalchemy` that will make interacting with this db really simple. Before the db is actually created, we're going to create the different tables which will act as different classes. First, we need to configure the location of the db and then define our db variable by creating a SQLAlchemy object of our application:

```Python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = "random_large_int"
Bootstrap(app)
```

We've also utilized a secret key so we can use CSRF (Cross-site Request Forgery) tokens and we've passed in our app as an argument to the Bootstrap function. Now, let's create the users table:

```Python
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(15))
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    password = db.Column(db.String(80))
```
You'll notice a couple of arguments that have been included when defining the class of `Users`. First, we've included `UserMixin` which comes from the `flask_login` library - this will allow us some extended functionality when dealing with a user. Second, there's `db.Model` - this just let's our application know that this class is a table in our db.

### Create the DB
We're going to create the db using Python. In your `app.py` file, comment-out the last line that runs the application:

```Python
# app.run(port=port)
```

This will prevent the server from launching when we import the db object into the Python CLI. Next, open Terminal and type in the following:

```Shell
$ python
>>> from app import db
>>> db.create_all()
>>> exit()
```

You should now see a new .db file named `database.db` inside your `main` folder. Congrats! Don't forget to go back and uncomment the last line of `app.py`.

## Creating a Form
For the most part, users will use a form to enter data into your application. The first form we need is a login form so authenticated users can access certain portions of your site.

Start by creating a new file in the `main` folder called `forms.py`. This file will house the logic for all our forms. There's a few necessary imports, so copy and paste the following:

```Python
from wtforms import *
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.file import FileField
from forms import *
```

Each form is set up as a class that inherits from `FlaskForm`. Our form stored in `forms.py` for logging in should look like this:

```Python
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=5, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
```

Now that the form has been created, let's include it in a new page called `login.html` inside our `templates` folder. Remember, the top of the file should "extend" from the `base.html` file, so it should look something like this as we start:

```HTML
{% extends "base.html" %} {% block title %} Login {% endblock %} {% block content %} {% import "bootstrap/wtf.html" as wtf %}

<div class="container">
  <div class="jumbotron">
    <h1>Login</h1>
  </div>
</div>
{% endblock %}

```

Notice, there's an additional line for an HTML file that has a form included; this allows the Jinja2 engine to read the forms we're going to include. After the jumbotron (which is a Bootstrap element) we should place our login form; however, it will look different from a typical HTML form:

```HTML
<div class="container" id="login">
<!-- This is where we create the form for the login -->
  <form class="form sign-in" , method="POST" action="/login">
    {{ form.hidden_tag() }} {{ wtf.form_field(form.email) }}
    <!-- Password field -->
    {{ wtf.form_field(form.password) }}
    <!-- Submit and forgot buttons -->
    <input class="btn btn-primary" type="submit" value="Login">
  </form>
</div>
```

Finally, we need to include the form in our `app.py` because the templating engine will be expecting a form, but it doesn't know which one. So, make our `/login` endpoint look like this:

```Python
@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', **locals())
```

If we try to run our server, we'll be able to see a login page. However, if we try to submit the form, we're going to get thrown an error of the server not being able to handle the request because we haven't defined the methods for this page. What we need to do is manipulate our `/login` route a bit to handle a `POST` request when the form is submitted. This takes two steps:

```Python
@app.route('/login', methods=['GET', 'POST']) # Step 1 = Methods
def login():
    form = LoginForm()

    if request.method == 'POST': # Step 2 = If POST is the type of request
        print('Success signing in {}'.format(form.email.data))
        return redirect(url_for('index'))

    return render_template('login.html', **locals())
```

Now, if we run our server and "sign in" using any email address, we should get a response back in the terminal while we're redirected to the index:

```Shell
127.0.0.1 - - [22/Apr/2018 17:35:30] "GET /login HTTP/1.1" 200 -
Success signing in user@email.com
127.0.0.1 - - [22/Apr/2018 17:35:39] "POST /login HTTP/1.1" 302 -
127.0.0.1 - - [22/Apr/2018 17:35:39] "GET / HTTP/1.1" 200 -
```

This is great for "logging in" users, but doesn't actually authenticate anything. We need to create a way for users to log in only if they have valid credentials. This could be hard-coded into our application, but this wouldn't be scalable or secure. Earlier, we created the `Users` class in the db...let's actually do something with it now.

I've given you a file called `conn_test.py` that will allow you programmatically add users to your db. Edit the variables in the file to your liking, then run:

```Shell
$ python conn_test.py
```

You should get output that alerts you to the addition of your new user. However, let's check it out ourselves:

```Shell
$ sqlite3 database.db
```
Then:

```sql
sqlite> .headers on
sqlite> .mode columns
sqlite> select * from users;
```

The first two commands make it easier to read what the hell is going on; the last will show us all records in the table `Users`. You should get a response to your query with all the information for the user you created earlier.

Now, we need to authenticate the user. In `app.py`, we need to replace the logic under the login table. This will require a couple of steps: first, we'll have to include some more imports from `flask_login` underneath our db configs:

```Python
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
```

Then, with our `login` route, we'll need to swap out our dummy logic that read the form's email address for an actual authentication process using our db:

```Python
if request.method == 'POST':
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                print("Logged {} {} in".format(current_user.first_name,
                                               current_user.last_name))
                return redirect(url_for('index'))
            else:
              print("Something is wrong with this login info...")
              return redirect(url_for('login'))
        else:
            print("This isn't a user...")
            render_template('login.html', **locals())

return render_template('login.html', **locals())
```

Let's have our authenticated users directed to a page that can only be accessed if they are indeed authenticated. First, we'll create the html file in our `templates` folder. Let's call it `dashboard.html`. Let's build the page like this:

```HTML
{% extends "base.html" %} {% block title %} Login {% endblock %} {% block content %}
<div class="container">
  <div class="jumbotron">
    <h1>Hello, {{ current_user.first_name }} {{ current_user.last_name }}!</h1>
  </div>
</div>

{% endblock %}
```

Now, we need to create a new route for this endpoint:

```Python
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', **locals())
```

Now, let's change the redirect from our earlier login function to navigate to the correct page once authenticated:

```Python
if request.method == 'POST':
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                print("Logged {} {} in".format(current_user.first_name,
                                               current_user.last_name))
                return redirect(url_for('index')) # TODO: Change this argument to 'dashboard'
            else:
              print("Something is wrong with this login info...")
              return redirect(url_for('login'))
        else:
            print("This isn't a user...")
            render_template('login.html', **locals())

return render_template('login.html', **locals())
```
