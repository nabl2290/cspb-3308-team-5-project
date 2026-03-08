from datetime import date, datetime
from models import db, User, Child, FeedingEvent

def seed_db():
    if User.query.count() > 0:
        return  # already seeded

    # Users (parents)
    atsuko = User(first_name="Atsuko", last_name="Smith", email="atsuko@example.com")
    atsuko.set_password("test123")

    jon = User(first_name="Jon", last_name="Smith", email="jon@example.com")
    jon.set_password("test123")

    michelle = User(first_name="Michelle", last_name="Jones", email="michelle@example.com")
    michelle.set_password("test123")

    # Children
    emma = Child(
        first_name="Emma",
        last_name="Smith",
        dob=date(2026, 1, 15),
        gender="F",
        eye_color="brown",
        parents=[atsuko, jon],
    )

    sara = Child(
        first_name="Sara",
        last_name="Smith",
        dob=date(2024, 9, 3),
        gender="F",
        eye_color="brown",
        parents=[atsuko, jon],
    )

    noah = Child(
        first_name="Noah",
        last_name="Jones",
        dob=date(2023, 8, 22),
        gender="M",
        eye_color=None,
        parents=[michelle],
    )

    db.session.add_all([atsuko, jon, michelle, emma, sara, noah])
    db.session.flush()  # get IDs before creating feeding events

    # --- Feeding Events ---
    feeding_events = [
        FeedingEvent(child_id=emma.id, timestamp=datetime(2024, 6, 1, 8, 0),  description="Breastfed, 10 min"),
        FeedingEvent(child_id=emma.id, timestamp=datetime(2024, 6, 1, 12, 0), description="Formula, 4 oz"),
        FeedingEvent(child_id=emma.id, timestamp=datetime(2024, 6, 1, 17, 0), description=None),
        FeedingEvent(child_id=sara.id, timestamp=datetime(2024, 6, 1, 7, 30), description="Breastfed, 15 min"),
        FeedingEvent(child_id=sara.id, timestamp=datetime(2024, 6, 1, 11, 0), description="Formula, 3 oz"),
        FeedingEvent(child_id=noah.id, timestamp=datetime(2024, 6, 1, 9, 0),  description="Formula, 5 oz"),
    ]

    db.session.add_all(feeding_events)
    db.session.commit()
    print("Dev seeds loaded.")
