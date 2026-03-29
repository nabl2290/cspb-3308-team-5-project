import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from flask import Flask
from models import db, User

@pytest.fixture
def app():
    """Create a Flask app with an in-memory test database."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


# Factory fixture for creating test users.
# Uses default values, but any field can be overridden.
#
# Examples:
#   user = create_user()                              # all defaults
#   user = create_user(first_name="Jane")             # override first name
#   user = create_user(email="jane@example.com",      # override multiple fields
#                      password="Secret456")
@pytest.fixture
def create_user(app):
    def _create_user(first_name="Test", last_name="User", email="test@example.com", password="Password123"):
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    return _create_user
