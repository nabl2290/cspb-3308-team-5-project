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

Join table to represent many-to-many relationship between users and children.

### Fields
| Field Name | Description      | Constraints   |
|------------|------------------|---------------|
| user_id    | user identifier  | int, NOT NULL |
| child_id   | child identifier | int, NOT NULL |

Note: Composite primary key on (user_id, child_id) to prevent duplicate associations.

### Relationships
- Many-to-one with `User` (user_id foreign key)
- Many-to-one with `Child` (child_id foreign key)

### Table Tests

#### **Use Case Name:** Inserting a valid user-child association

**Description:** Verify that a valid association can be created by inserting a row with existing user_id and child_id values, confirming the many-to-many relationship works correctly.

**Pre-conditions:** Database running, user record exists, child record exists

**Test Steps:**
1. Create a user record
2. Create a child record
3. Insert a row into user_child linking the user to the child
4. Query user_child with the `user_id` and `child_id` to confirm the association exists
5. Query user_child with the `user_id` to confirm the child is linked to the user
6. Query user_child with the `child_id` to confirm the user is linked to the child

**Expected Result:** Query returns the inserted row, confirming the association exists.

**Post-conditions:** User, child, and association persisted

#### **Use Case Name:** Inserting a user-child association with NULL values

**Description:** Verify that inserting a row with a NULL user_id or child_id fails due to NOT NULL constraints.

**Pre-conditions:** Database running

**Test Steps:**
1. Attempt to insert a row into user_child with a NULL user_id
2. Attempt to insert a row into user_child with a NULL child_id

**Expected Result:** Both insertions are rejected with a NOT NULL constraint error

**Post-conditions:** No rows are added to user_child

**Use Case Name:** One user linked to multiple children

**Description:** Verify that a single user can be associated with multiple children by inserting multiple rows with the same       
  user_id and different child_id values, confirming the many-to-many relationship works correctly.

**Pre-conditions:** Database running, user record exists, children records exist

**Test Steps:**
1. Create a user record
2. Create two child records
3. Insert two rows into user_child, linking the user to each child
4. Query user_child with the `user_id` to confirm all associations exist

**Expected Result:** Query returns two rows, each linking the user to a different child

**Post-conditions:** User, child, and associations persisted

#### **Use Case Name:** One child linked to multiple users

**Description:** Verify that a single child can be associated with multiple users by inserting multiple rows with the same child_id and different user_id values, confirming the many-to-many relationship works correctly.

**Pre-conditions:** Database running, users records exist, child record exists

**Test Steps:**
1. Create two user records
2. Create a child record
3. Insert two rows into user_child, linking each user to the child
4. Query user_child with the `child_id` to confirm all associations exist

**Expected Result:** Query returns two rows, each linking a different user to the child

**Post-conditions:** User, child, and associations persisted

---
# Data Access Methods
---

## Access Method: `get_user_by_id`
### Description
Retrieves a user from the database
### Parameters
- user_id (int)
### Return Values
- User record (or None)
### Tests
1. User returned when user_id matches a user's id
2. None when no User has a matching id

## Access Method: `get_user_by_email_and_password`
### Description
Retrieves a user from the database by email and password
### Parameters
- email (str)
- password (str)
- Note: Password should be hashed and compared to stored password_hash
### Return Values
- User record (or None)
### Tests
1. User returned when email and password match a user's credentials
2. None returned when no User has matching email and password

## Access Method: `update_user`
### Description
Updates a user's information in the database
### Parameters
- User record
- fields_to_update (dict of field names and new values)
### Return Values
- Updated User record when update is successful
- Note: error is raised if fields_to_update contains invalid field names or values, or if the user does not exist
### Tests
1. User record is updated when User is present and fields are valid
3. Validation errors raised when fields_to_update contains invalid fields or values
4. Error raised when User does not exist

## Access Method: `create_child`
### Description
Creates a new child record for a user in the database
### Parameters
- user_id (int)
- child_data (dict of child field names and values)
- Note: child_data must contain all required fields for the Child table
### Return Values
- Newly created Child record when creation is successful
- Note: error is raised if child_data is missing required fields or contains invalid values, or if the user_id does not exist
### Tests
1. Child record is created and linked to user when user_id exists and child_data is valid. A new user_child association is also created.
2. Validation errors raised when child_data is missing required fields or contains invalid values
3. Error raised when user_id does not exist

## Access Method: `user.children`
### Description
We will use the existing SQLAlchemy relationship to access a user's children, which will return a list of Child records associated with the user through the user_child table.
### Parameters
- none (accessed via User object)
### Return Values
- List of Child records associated with the user
### Tests
1. Returns a list of Child records when the user has associated children
2. Returns an empty list when the user has no associated children


TODO other table methods:
perhaps:
get_child_by_id
update_child
get_feeding_event_by_id
update_feeding_event
get_feeding_events_by_child_id

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