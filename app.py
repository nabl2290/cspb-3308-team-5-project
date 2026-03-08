import os

from flask import Flask, request, render_template, redirect, url_for
from models import db, User, Child, FeedingEvent
from seeds import seed_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

    # Seed the database with test data if in development environment
    if os.getenv('FLASK_ENV') == 'development':
        seed_db()

# Welcome page
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/sample")
def sample():
    return render_template('sample.html')

# Registration page
@app.get("/register")
def register():
    # TODO: Add registration template
    return render_template('register.html')

# Post registration for new user
@app.post("/register")
def register_post():
    # TODO: Add logic to create new user based on form data
    return redirect(url_for('dashboard'))

# Login page
@app.get("/login")
def login():
    # TODO: Add login template
    return render_template('login.html')

# Post login for authentication
@app.post("/login")
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    # TODO: Add logic to authenticate user based on form data

    return redirect(url_for('dashboard'))

# Show user profile page
@app.get("/user/<int:user_id>")
def get_user(user_id):
    user = db.get_or_404(User, user_id)

    # TODO: Add user profile template with user data
    return render_template('user.html', user=user)

# Update user profile
@app.patch("/user/<int:user_id>")
def update_user(user_id):
    user = db.get_or_404(User, user_id)

    # TODO: Add logic to update user profile based on request data

    return redirect(url_for('get_user', user_id=user_id))

# User dashboard page
@app.get("/user/<int:user_id>/dashboard")
def dashboard(user_id):
    user = db.get_or_404(User, user_id)
    # TODO: Add dashboard template with user-specific data
    #  (e.g., list of children, recent feeding events)
    return render_template('dashboard.html', user=user)

# Show baby/child profile page
@app.get("/child/<int:child_id>")
def get_child(child_id):
    child = db.get_or_404(Child, child_id)

    # TODO: Add child profile template with child data
    return render_template('child.html', child=child)

# Create new baby/child profile
@app.post("/child")
def create_child():
    # TODO: Add logic to create new child profile based on request data
    #
    # TODO: After creating the child, redirect to their profile page
    return '', 201

# Update baby/child profile
@app.patch("/child/<int:child_id>")
def update_child(child_id):
    child = db.get_or_404(Child, child_id)

    # TODO: Add logic to update child profile based on request data

    return redirect(url_for('get_child', child_id=child_id))

# Create new feeding event
@app.post("/feeding-event")
def create_feeding_event():
    # TODO: Add logic to create new feeding event based on request data
    return '', 201

# Edit feeding event
@app.patch("/feeding-event/<int:event_id>")
def update_feeding_event(event_id):
    event = db.get_or_404(FeedingEvent, event_id)

    # TODO: Add logic to update feeding event based on request data

    return redirect(url_for('get_child', child_id=event.child_id))

# Route to display all users (for testing purposes)
@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

