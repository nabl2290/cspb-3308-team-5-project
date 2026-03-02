import os
from flask import Flask, render_template
from models import db, User
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

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/users")
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)
