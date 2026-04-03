from datetime import date
import os
import re

import prefix

import user_forms

from flask import Flask, request, render_template, redirect, url_for, session
from models import db, User, Child, FeedingEvent
from queries import create_user, get_user_by_email_and_password
from seeds import seed_db
from datetime import datetime

from flask_wtf import FlaskForm

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)   

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = os.getenv('APP_SECRET_KEY') or 'dev-secret-key'
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

    # Seed the database with test data if in development environment
    if os.getenv('FLASK_ENV') == 'development':
        seed_db()

"""
Helper function to get the currently logged-in user
"""
def get_current_user():
  user_id = session.get('user_id')

  if user_id is None:
      return None

  return db.get_or_404(User, user_id)

"""
Helper function to require user is authorized to access a page (e.g., their own dashboard or profile)
"""
def authorized_user(requested_user_id):
  current_user_id = session.get('user_id')

  if current_user_id is None:
        return False
  else:
    return current_user_id == requested_user_id


# Welcome page
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sample")
def sample():
    return render_template('sample.html')

# Registration page form
@app.get("/register")
def register():
    return render_template('registration.html')

# Post registration for new user
@app.post("/register")
def register_post():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    errors = {}

    if not email:
        errors['email'] = "Email is required."
    elif not re.match(EMAIL_REGEX, email):
        errors['email'] = "Please enter a valid email address."
    else:
        existing_user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()
        if existing_user is not None:
            errors['email'] = "An account with this email already exists."

    if not password:
        errors['password'] = "Password is required."
    elif len(password) < 8:
        errors['password'] = "Password must be at least 8 characters long."

    if not confirm_password:
        errors['confirm_password'] = "Please confirm your password."
    elif password != confirm_password:
        errors['confirm_password'] = "Passwords do not match."

    if not first_name:
        errors['first_name'] = "First name is required."

    if not last_name:
        errors['last_name'] = "Last name is required."

    if len(errors) > 0:
        return render_template('registration.html', errors=errors, form=request.form), 422
    else:
        new_user = create_user({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        })

        # Log in the new user by saving their ID in the session
        session['user_id'] = new_user.id
        return redirect(url_for('dashboard', user_id=new_user.id))

# Login page with form
@app.get("/login")
def login():
    # Get any error message from query parameters (e.g., after unauthorized access)
    error = request.args.get('error')
    return render_template('login.html', error=error)

# Post login for authentication
@app.post("/login")
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = get_user_by_email_and_password(email, password)

    if user is None:
        return render_template('login.html', error="Invalid email or password."), 422

    session['user_id'] = user.id
    return redirect(url_for('dashboard', user_id=user.id))

# Logout route
@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

# Show user profile page
@app.get("/user/<int:user_id>")
def get_user(user_id):
    user = db.get_or_404(User, user_id)

    # TODO: Add user profile template with user data
    return render_template('user.html', user=user)

# Edit user profile page with form
@app.get("/user/<int:user_id>/edit")
def edit_user(user_id):
    user = db.get_or_404(User, user_id)

    form=user_forms.EditUserForm(first_name=user.first_name,last_name=user.last_name,email=user.email)

    return render_template('edit_user.html', user=user, form=form)

# Update user profile
@app.post("/user/<int:user_id>/edit") # TODO update this in documentation, changed from PATCH
def update_user(user_id):
    user = db.get_or_404(User, user_id)

    if request.form["first_name"]:
        user.first_name = request.form["first_name"]
    if request.form["last_name"]:
        user.last_name = request.form["last_name"]
    if request.form["email"]:
        user.email = request.form["email"]

    # TODO update password too

    db.session.commit()

    return redirect(url_for('get_user', user_id=user.id))

# User dashboard page
@app.get("/user/<int:user_id>/dashboard")
def dashboard(user_id):
    if not authorized_user(user_id):
        return redirect(url_for('login', error="You are not authorized to access this page"))

    user = db.get_or_404(User, user_id)
    babies = user.children
    current_date = date.today()
    recent_feeding_evts = {}
    for baby in babies:
        latest = FeedingEvent.query.filter_by(child_id=baby.id).order_by(FeedingEvent.timestamp).first()
        recent_feeding_evts[baby.id] = latest
    # TODO: Add dashboard template with user-specific data
    #  (e.g., list of children, recent feeding events)
    return render_template('dashboard.html', user=user, babies=babies, current_date=current_date, recent_feedings=recent_feeding_evts)

# Show baby/child profile page
@app.get("/child/<int:child_id>")
def get_child(child_id):
    child = db.get_or_404(Child, child_id)

    user = db.get_or_404(User, session.get('user_id'))
    # TODO: Add child profile template with child data
    return render_template('child.html', child=child, user=user)

# New baby/child form
@app.get("/child/new")
def new_child():
    return render_template('new_child.html')

# Create new baby/child based on new form submission
@app.post("/child")
def create_child():
    # TODO: Add logic to create new child profile based on request data
    #
    # TODO: After creating the child, redirect to their profile page
    return '', 201

# Edit baby/child form
@app.get("/child/<int:child_id>/edit")
def edit_child(child_id):
    child = db.get_or_404(Child, child_id)

    # TODO: Add child profile template with child data
    return render_template('edit_child.html', child=child)

# Update baby/child profile based on edit form submission
@app.patch("/child/<int:child_id>")
def update_child(child_id):
    child = db.get_or_404(Child, child_id)

    # TODO: Add logic to update child profile based on request data

    return redirect(url_for('get_child', child_id=child_id))

# New feeding event form
@app.get("/feeding-event/new")
def new_feeding_event():
    current_user = get_current_user()
    if not current_user:
        return redirect(url_for("login"))
    children = current_user.children
    return render_template('new_feeding_event.html', children=children)

# Create new feeding event based on new form submission
@app.post("/feeding-event")
def create_feeding_event():
    child_id = int(request.form.get("child_id"))
    date = request.form.get("date")

    if not child_id or not date:
        return "Missing required fields", 400
        
    description = request.form.get("description") or None
    
    timestamp = datetime.fromisoformat(date)

    new_feed = FeedingEvent(
        child_id=int(child_id),
        timestamp=timestamp,
        description=description
    )

    db.session.add(new_feed)
    db.session.commit()
    
    return redirect(url_for("new_feeding_event"))

# Edit feeding event form
@app.get("/feeding-event/<int:event_id>/edit")
def edit_feeding_event(event_id):
    event = db.get_or_404(FeedingEvent, event_id)
    current_user = get_current_user()
    if not current_user:
        return redirect(url_for("login"))
    if event.child_id not in [child.id for child in current_user.children]:
        return "Unauthorized", 403
    children = current_user.children
    return render_template('edit_feeding_event.html', event=event, children=children)

# Update feeding event based on edit form submission
@app.post("/feeding-event/<int:event_id>/edit")
def update_feeding_event(event_id):
    event = db.get_or_404(FeedingEvent, event_id)
    child_id = request.form.get("child_id")
    date = request.form.get("date")
    description = request.form.get("description") or None

    if not child_id or not date:
        return "Missing required fields", 400

    event.child_id = int(child_id)
    event.timestamp = datetime.fromisoformat(date)
    event.description = description

    db.session.commit()
    return redirect(url_for("edit_feeding_event", event_id=event.id))

# @app.patch("/feeding-event/<int:event_id>")
# def update_feeding_event(event_id):
#     event = db.get_or_404(FeedingEvent, event_id)

#     # TODO: Add logic to update feeding event based on request data

#     return redirect(url_for('get_child', child_id=event.child_id))

# Route to display all users (for testing purposes)
@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

