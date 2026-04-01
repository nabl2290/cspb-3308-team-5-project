from models import db, User, Child, FeedingEvent

# ---- User Queries ----
def get_user_by_id(user_id):
    """Retrieves a user by ID. Returns User or None."""
    return db.session.get(User, user_id)


def get_user_by_email_and_password(email, password):
    """Retrieves a user by email and password. Returns User or None."""
    user = db.session.query(User).filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None


def update_user(user, fields_to_update):
    """Updates a user's information. Returns updated User."""
    pass


# ---- Child Queries ----
def get_child_by_id(child_id):
    """Retrieves a child by ID. Returns Child or None."""
    pass


def create_child(user_id, child_data):
    """Creates a new child record linked to a user. Returns new Child."""
    pass


def update_child(child, fields_to_update):
    """Updates a child's information. Returns updated Child."""
    pass


# ---- Feeding Event Queries ----
def get_feeding_event_by_id(event_id):
    """Retrieves a feeding event by ID. Returns FeedingEvent or None."""
    pass


def get_feeding_events_by_child_id(child_id):
    """Retrieves all feeding events for a child. Returns list of FeedingEvents."""
    pass


def update_feeding_event(feeding_event, fields_to_update):
    """Updates a feeding event. Returns updated FeedingEvent."""
    pass
