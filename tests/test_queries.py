from datetime import datetime

import pytest
from models import db, User, Child, FeedingEvent
from queries import (
    create_user as create_user_query,
    get_user_by_id,
    get_user_by_email,
    get_user_by_email_and_password,
    update_user,
    get_child_by_id,
    create_child,
    update_child,
    get_feeding_event_by_id,
    get_feeding_events_by_child_id,
    update_feeding_event,
    create_feeding_event
)

# ---- User Query Tests ----
class TestCreateUser:
    def test_creates_user_with_valid_data(self, app):
        user = create_user_query({
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@example.com",
            "password": "Password123",
        })
        assert user.id is not None
        assert user.first_name == "Jane"
        assert user.last_name == "Doe"
        assert user.email == "jane@example.com"
        assert user.check_password("Password123")

    def test_raises_error_with_missing_fields(self, app):
        with pytest.raises(Exception):
            create_user_query({"first_name": "Jane"})

    def test_raises_error_with_duplicate_email(self, app, create_user):
        create_user(email="taken@example.com")
        with pytest.raises(Exception):
            create_user_query({
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "taken@example.com",
                "password": "Password123",
            })


class TestGetUserById:
    def test_returns_user_when_exists(self, create_user):
        user = create_user()
        retrieved_user = get_user_by_id(user.id)
        assert retrieved_user is not None
        assert retrieved_user.id == user.id

    def test_returns_none_when_not_found(self, app):
        retrieved_user = get_user_by_id(9999)  # Assuming this ID does not exist
        assert retrieved_user is None


class TestGetUserByEmail:
    def test_returns_user_when_email_exists(self, create_user):
        user = create_user(email="user@example.com")
        retrieved_user = get_user_by_email("user@example.com")
        assert retrieved_user is not None
        assert retrieved_user.id == user.id

    def test_returns_none_when_email_not_found(self, app):
        retrieved_user = get_user_by_email("nonexistent@example.com")
        assert retrieved_user is None


class TestGetUserByEmailAndPassword:
    def test_returns_user_with_valid_credentials(self, create_user):
        user = create_user(email="user@example.com", password="test123")
        retrieved_user = get_user_by_email_and_password("user@example.com", "test123")
        assert retrieved_user is not None
        assert retrieved_user.id == user.id

    def test_returns_none_with_invalid_credentials(self, create_user):
        user = create_user(email="user@example.com", password="test123")
        # With wrong password
        retrieved_user = get_user_by_email_and_password("user@example.com", "wrongpassword")
        assert retrieved_user is None

        # With wrong email
        retrieved_user = get_user_by_email_and_password("wrong@example.com", "test123")
        assert retrieved_user is None


class TestUpdateUser:
    def test_updates_user_with_valid_fields(self, create_user):
        user = create_user()
        fields_to_update = {"first_name": "Updated", "last_name": "Name", "email": "new-email@gmail.com", "password": "NewPassword123"}
        updated_user = update_user(user, fields_to_update)

        assert updated_user.first_name == "Updated"
        assert updated_user.last_name == "Name"
        assert updated_user.email == "new-email@gmail.com"
        assert updated_user.check_password("NewPassword123")

    def test_raises_error_with_invalid_fields(self, create_user):
        user = create_user()
        with pytest.raises(ValueError):
            update_user(user, {"invalid_field": "value"})

    def test_raises_error_with_invalid_field_values(self, create_user):
        user = create_user()
        with pytest.raises(Exception):
            update_user(user, {"first_name": ""})
        with pytest.raises(Exception):
            update_user(user, {"email": "not-an-email"})

    def test_raises_error_when_user_does_not_exist(self, app):
        with pytest.raises(ValueError):
            update_user(None, {"first_name": "Updated"})


# ---- Child Query Tests ----
class TestGetChildById:
    def test_returns_child_when_exists(self):
        pass

    def test_returns_none_when_not_found(self):
        pass

    def test_raises_error_with_invalid_id(self):
        pass


class TestCreateChild:
    def test_creates_child_linked_to_user(self):
        pass

    def test_raises_error_with_invalid_child_data(self):
        pass

    def test_raises_error_when_user_does_not_exist(self):
        pass


class TestUpdateChild:
    def test_updates_child_with_valid_fields(self):
        pass

    def test_raises_error_with_invalid_fields(self):
        pass

    def test_raises_error_when_child_does_not_exist(self):
        pass


# ---- Feeding Event Query Tests ----
class TestGetFeedingEventById:
    def test_returns_event_when_exists(self):
        pass

    def test_returns_none_when_not_found(self):
        pass

    def test_raises_error_with_invalid_id(self):
        pass


class TestGetFeedingEventsByChildId:
    def test_returns_events_for_child(self):
        pass

    def test_returns_empty_list_when_no_events(self):
        pass

    def test_raises_error_when_child_does_not_exist(self):
        pass


class TestUpdateFeedingEvent:
    def test_updates_event_with_valid_fields(self, create_feeding_event):
        #confirm that a child with id 1 exists
        feedEvt = create_feeding_event()  # Placeholder for actual event creation
        fields_to_update = {
            "child_id": 2,
            "timestamp": datetime(2024, 6, 1, 9, 0),
            "description": "Updated description"}
        updated_event = update_feeding_event(feedEvt, fields_to_update)
        assert updated_event.child_id == 2
        assert updated_event.timestamp == datetime(2024, 6, 1, 9, 0)
        assert updated_event.description == "Updated description"
        

    def test_raises_error_when_update_fails(self, create_feeding_event):
        FeedingEvt = create_feeding_event() 
        with pytest.raises(ValueError):
            update_feeding_event(FeedingEvt, {"invalid_field": "value"})
         # uncomment below if validation for FeedingEvent Table is implemented
        # with pytest.raises(Exception):
        #     update_feeding_event(FeedingEvt, {"child_id": "not-an-integer"})
        # with pytest.raises(Exception):
        #     update_feeding_event(FeedingEvt, {"timestamp": "not-a-datetime"})
        # with pytest.raises(Exception):
        #     update_feeding_event(FeedingEvt, {"description": 5.5})
        


# ---- user.children Relationship Tests ----
class TestUserChildrenRelationship:
    def test_returns_children_when_associated(self, create_user, create_child):
        user = create_user()
        child = create_child("Test", "Child", datetime(2026, 1, 1), "F", "blue", user.id)
        assert child in user.children 
        assert user in child.parents

    def test_returns_empty_list_when_no_children(self, create_user):
        user = create_user()
        assert user.children == []
