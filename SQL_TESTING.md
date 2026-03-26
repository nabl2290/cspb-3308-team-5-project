Directions: 
# SQL_TESTING.md
## Project Milestone 5: SQL Design
**Project:** Team 5: BabySteps
**Purpose:** Database design and testing specification for developers

---

This document describes the **database schema**, **table relationships**, and
**data access methods** for the Baby Steps application. It is intended as a
**developer-facing design document** that clearly defines how data is stored,
accessed, and validated.
This document answers the following questions:
- What tables exist in the database?
- What fields and constraints do those tables contain?
- How are tables related?
- What data access methods are required?
- Which pages depend on which data?
- How do we test both the schema and the access routines?
The backend uses **SQLite** accessed through **SQLAlchemy**.

---

# Database Tables
At minimum, the system requires the following tables:
- `user`
- `child`
- `feeding_event`
- `user_child`

Each table is described below.
---

## 1) Table: User

### Table Description
Stores user account and profile information for all BabySteps users.

### Fields
| Field Name | Description | Constraints |
|------------|-------------|-------------|
| id | Unique user identifier | Primary key |
| first_name | User first name | NOT NULL, max 50 charcters |
| last_name | User last name | NOT NULL, max 50 charcters |
| email | User last name | UNIQUE NOT NULL, max 120 charcters |
| password_hash | Hashed password | NOT NULL, max 256 characters |

### Relationships

- Many-to-many with `Child` through `user_child` table
- One-to-many with `user_child` table

### Table Tests

**Use Case Name:** Create user record

**Description:** Verify a new user can be stored

**Pre-conditions:** Database running

**Test Steps:**
1. Insert valid user row
2. Query by email

**Expected Result:** User row exists

**Actual Result:** User returned by query

**Status:** Pass

**Post-conditions:** User persisted


## 2) Table: Child

### Table Description
TODO

### Fields
| Field Name | Description | Constraints |
|------------|-------------|-------------|
| TODO | TODO | TODO |

### Relationships

- Many-to-many with `User` through `user_child` table
- One-to-many with `user_child` table

### Table Tests

**Use Case Name:** TODO

**Description:** TODO

**Pre-conditions:** TODO

**Test Steps:**
1. TODO
2. TODO

**Expected Result:** TODO

**Actual Result:** TODO

**Status:** TODO (Pass)

**Post-conditions:** TODO

## 3) Table: FeedingEvent

### Table Description
TODO

### Fields
| Field Name | Description | Constraints |
|------------|-------------|-------------|
| TODO | TODO | TODO |

### Relationships
- TODO

### Table Tests

**Use Case Name:** TODO

**Description:** TODO

**Pre-conditions:** TODO

**Test Steps:**
1. TODO
2. TODO

**Expected Result:** TODO

**Actual Result:** TODO

**Status:** TODO (Pass)

**Post-conditions:** TODO

## 4) Table: user_child

### Table Description
TODO

### Fields
| Field Name | Description | Constraints |
|------------|-------------|-------------|
| TODO | TODO | TODO |

### Relationships
- TODO

### Table Tests

**Use Case Name:** TODO

**Description:** TODO

**Pre-conditions:** TODO

**Test Steps:**
1. TODO
2. TODO

**Expected Result:** TODO

**Actual Result:** TODO

**Status:** TODO (Pass)

**Post-conditions:** TODO


---
# Data Access Methods
---

## Access Method: get_user_by_id
### Description
Retrieves a user from the database
### Parameters
- user_id (int)
### Return Values
- User record (or None)
### Tests
1. User returned when user_id matches a user's id
2. None when no User has a matching id

TODO other table methods:
perhaps:
get_user_by_id (done)
get_user_by_email_password
update_user
get_child_by_id
update_child
get_feeding_event_by_id
update_feeding_event
get_feeding_events_by_child_id
get_children_of_user

--- 

# Page Data Access Tests

### Login
**Use Case Name:** Login form starts user session  
**Description:** Verify login page works properly  
**Pre-conditions:** None  
**Test Steps:**  
     1. Login with valid credentials and confirm dashboard opens.  
     2. Logging in with invalid credentials and notification informs user.

### Registration
**Use Case Name:** Alternative form of login to create user  
**Description:** Confirm that entering in data in form can successfully generate new user data.  
**Pre-conditions:** None  
**Test Steps:**  
    1. Test form by filling in required data and confirming.  
    - This should create a new user account and direct the user either back to login or dashboard.  
    2. Failing to enter all required information does not allow the user to proceed.

### Dashboard
**Use Case Name:** Dashboard loads user data  
**Description:** Verify dashboard queries correct tables  
**Pre-conditions:** User logged in  
**Test Steps:**  
    1. Load dashboard  
    2. Fetch user and children and most recent feeding event for display.

### User Profile Page
**Use Case Name:** View/edit User information  
**Description:** Verify current user can view their profile information  
**Pre-conditions:** User logged in  
**Test Steps:**  
    1. Load user profile with information from database  
    2. press edit button to be redirected to editing page. 

### Child Profile Page
**Use Case Name:** View/edit User information 
**Description:** Verify current user can view their child's information  
**Pre-conditions:** User logged in and is related to child  
**Test Steps:**  
    1. Load child's with information from database  
    2. press edit button to be redirected to editing page.

### Feeding Event Page
**Use Case Name:** view/edit feeding event information  
**Description:** Verify that feeding event information is valid.  
**Pre-conditions:** User logged in  
**Test Steps:**  
    1. Load feeding event information  
    2. press edit button to be redirected to editing page.


---

# Page-to-Database Mapping
| Page | Tables Accessed |
|----|----------------|
| Login | user |
| Registration | user |
| Dashboard | user, user_child, child, feeding_event |
| View User Profile Page | user |
| Edit User Profile Page | user |
| Add Child Profile Page | user, user_child, child |
| View Child Profile Page | user, user_child, child, feeding_event |
| Edit Child Profile Page | user, user_child, child |
| Add Feeding Event Page | user, user_child, child, feeding_event |
| Edit Feeding Event Page | user, user_child, child, feeding_event |

---

## Notes
- Constraints enforced at DB and ORM levels
- All data access will go through direct or wrapped SQLAlchemy methods
- Tests executable via unit test suite