"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Rating, Movie


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route('/users')
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/register")
def register_form():
    """Add a registration form that asks for an email address, pw, route that 
    shows registration form."""


    return render_template("register_form.html")

@app.route("/register", methods=["POST"])
def register_process():

    Email = request.form.get("email")
    Password = request.form.get("password")

    print(Email)
    print(Password)

    users = User.query.filter(User.email == Email).all()

    print(users)

    if len(users) < 1:
        db.session.add(User(email=Email, password=Password))
        db.session.commit()
    else:
        flash("User with email {} already exists".format(Email))


@app.route("/login")
def login_form():
    """User login form"""

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def submit_login():
    """Check to see if login and password exist. Then, allow user to log in."""

    Email = request.form.get("email")
    Password = request.form.get("password")

    users = User.query.filter(User.email == Email, User.password == password).one()
    

    if users and usersTwo:






if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
