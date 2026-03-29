import sys
import os

# Allow importing from the parent directory (where models and queries are located)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from models import db, User, Child, FeedingEvent
from queries import (
    get_user_by_id,
    get_user_by_email_and_password,
    update_user,
    get_child_by_id,
    create_child,
    update_child,
    get_feeding_event_by_id,
    get_feeding_events_by_child_id,
    update_feeding_event,
)

# ---- User Query Tests ----
class TestGetUserById:
    def test_returns_user_when_exists(self):
        pass

    def test_returns_none_when_not_found(self):
        pass


class TestGetUserByEmailAndPassword:
    def test_returns_user_with_valid_credentials(self):
        pass

    def test_returns_none_with_invalid_credentials(self):
        pass


class TestUpdateUser:
    def test_updates_user_with_valid_fields(self):
        pass

    def test_raises_error_with_invalid_fields(self):
        pass

    def test_raises_error_when_user_does_not_exist(self):
        pass


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
    def test_updates_event_with_valid_fields(self):
        pass

    def test_raises_error_when_update_fails(self):
        pass


# ---- user.children Relationship Tests ----
class TestUserChildrenRelationship:
    def test_returns_children_when_associated(self):
        pass

    def test_returns_empty_list_when_no_children(self):
        pass
