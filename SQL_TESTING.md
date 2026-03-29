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
| Field Name | Description | Type | Constraints |
|------------|-------------|------|-------|
| id | Unique user identifier | INT | Primary key |
| first_name | User first name | STRING | NOT NULL, max 50 characters |
| last_name | User last name | STRING | NOT NULL, max 50 characters |
| email | User last name | STRING | UNIQUE NOT NULL, max 120 characters |
| password_hash | Hashed password | STRING | NOT NULL, max 256 characters |

### Relationships

- Many-to-many with `child` through `user_child` table (many users have many children)
- One-to-many with `user_child` table (one user has many children)

### Table Tests

#### **Use Case Name:** Create user record

**Description:** Verify a new user can be stored

**Pre-conditions:** Database running

**Test Steps:**
1. Insert valid user row
2. Query by email

**Expected Result:** User row exists

**Expected Post-conditions:** User persisted


## 2) Table: Child

### Table Description
Stores child profile information.

### Fields
| Field Name | Description | TYPE | Constraints |
|------------|-------------|------|-------|
| id | Unique child identifier | INT | Primary key |
| first_name | Child first name | STRING | NOT NULL, max 50 characters |
| last_name  | Child last name | STRING | NOT NULL, max 50 characters |
| dob        | Date of birth | DATE | NOT NULL |
| gender     | Gender [M/F/X] | CHAR | NOT NULL, exactly 1 character |
| eye_color  | Color of their eyes | STRING | max 20 characters |

### Relationships

- Many-to-many with `user` through `user_child` table (many children have many users)
- One-to-many with `user_child` table (one child has many users)
- One-to-many with `feeding_event` (one child has many feeding events)

### Table Tests

#### **Use Case Name:** Create child record associated with User

**Description:** Verify a new child can be stored

**Pre-conditions:** Database running

**Test Steps:**
1. Insert valid user row
2. Insert valid child row
3. Insert valid user_child row
4. Query for child by id
5. Query for child of user using user_child relationship
6. Query for user (parent) of child using user_child relationship

**Expected Result:** Child row exists, and assocation between child and user is made

**Expected Post-conditions:** Child is persisted, and relationship between user and child is persisted

## 3) Table: FeedingEvent

### Table Description
Stores a child's feed desctiprion, date/time, and relationship to child.

### Fields
| Field Name | Description | TYPE | Constraints |
|------------|-------------|------|-------|
| event_id | Unique event identifier | INT | Primary Key |
| child_id | id of corresponding child | INT | Foreign Key |
| timestamp | date/time of event | DATETIME | NOT NULL |
| description | event description | STRING | max 512 characters |

### Relationships
- Many-to-one with `child` (many feeding_events have one child)

### Table Tests

#### **Use Case Name:** Create new event

**Description:** Verify a new event has been stored

**Pre-conditions:** Database running, child exists

**Test Steps:**
1. Insert event with an existing child id
2. Query the event by id

**Expected Result:** Event exists in database

**Expected Post-conditions:** Event continues to exist is database

## 4) Table: user_child

### Table Description

Join table to represent many-to-many relationship between users and children.

### Fields
| Field Name | Description      | TYPE | Constraints |
|------------|------------------|------|-------------|
| user_id    | user identifier  | INT  | NOT NULL    |
| child_id   | child identifier | INT  | NOT NULL    |

Note: Composite primary key on (user_id, child_id) to prevent duplicate associations.

### Relationships
- Many-to-one with `user` (user_id foreign key) (many user_child entries have one user)
- Many-to-one with `child` (child_id foreign key) (many user_child entries have one child)

### Table Tests

#### **Use Case Name:** Inserting a valid user-child association

**Description:** Verify that a valid association can be created by inserting a row with existing user_id and child_id values, confirming the many-to-many relationship works correctly.

**Pre-conditions:** Database running, user record exists, child record exists

**Test Steps:**
1. Insert a row into user_child linking the user to the child
2. Query user_child with the `user_id` and `child_id` to confirm the association exists
3. Query user_child with the `user_id` to confirm the child is linked to the user
4. Query user_child with the `child_id` to confirm the user is linked to the child

**Expected Result:** Query returns the inserted row, confirming the association exists.

**Expected Post-conditions:** user_child row is persisted

#### **Use Case Name:** Inserting a user-child association with NULL values

**Description:** Verify that inserting a row with a NULL user_id or child_id fails due to NOT NULL constraints.

**Pre-conditions:** Database running

**Test Steps:**
1. Attempt to insert a row into user_child with a NULL user_id
2. Attempt to insert a row into user_child with a NULL child_id

**Expected Result:** Both insertions are rejected with a NOT NULL constraint error

**Expected Post-conditions:** No rows are added to user_child

#### **Use Case Name:** One user linked to multiple children

**Description:** Verify that a single user can be associated with multiple children by inserting multiple rows with the same       
  user_id and different child_id values, confirming the many-to-many relationship works correctly.

**Pre-conditions:** Database running, user record exists, 2 child records exist

**Test Steps:**
1. Insert two rows into user_child, linking the user to each child
2. Query user_child with the `user_id` to confirm all associations exist

**Expected Result:** Query returns two rows, each linking the user to a different child

**Expected Post-conditions:** 2 user_child associations persisted

#### **Use Case Name:** One child linked to multiple users

**Description:** Verify that a single child can be associated with multiple users by inserting multiple rows with the same child_id and different user_id values, confirming the many-to-many relationship works correctly.

**Pre-conditions:** Database running, 2 user records exist, child record exists

**Test Steps:**
1. Insert two rows into user_child, linking each user to the child
2. Query user_child with the `child_id` to confirm all associations exist

**Expected Result:** Query returns two rows, each linking a different user to the child

**Post-conditions:** 2 user_child associations persisted

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

## Access Method: `get_feeding_event_by_id`
### Description
Retrieves a feeding event from the database
### Parameters
- event_id
### Return Values
- Feeding event record
- None if no record is found
- Error if invalid id like "s"
### Tests
1. Return a specific event by id with valid child id
2. Return None for a valid id that doesn't exist
3. Raise error when invalid event id is entered

## Access Method: `update_feeding_event`
### Description
Updates an existing feeding event
### Parameters
- feeding_event record
- fields_to_update (dict of field names and new values)
### Return Values
- Updated feeding event record
- Note: error is raised if fields_to_update contains invalid field names or values, or if the user does not exist
### Tests
1. Updating any field in a feed event updates that event in the database (new event is not created)
2. Raises error if an event is unable to be updated & the record remains but is unchanged

## Access Method: `get_feeding_events_by_child_id`
### Description
Retrieves all feeding events of one child
### Parameters
- child_id
### Return Values
- List of all feeding events (which could be empty)
- Error (if child does not exist)
### Tests
1. Valid child_id with feeding events returns list of all feed events
2. Valid child_id with no feeding events returns empty list
3. If invalid child_id error is raised

## Access Method: `get_child_by_id`
### Description
Retrieves one child by its id
### Parameters
- child_id
### Return Values
- Child 
- None (if child does not exist for valid child_id)
- Error (if invalid child_id like "s")
### Tests
1. Valid child_id returns the child row
2. If invalid child_id, error is raised
3. If child_id does not match a child, then None is returned.

## Access Method: `update_child`
### Description
Updates a child's information in the database
### Parameters
- Child record
- fields_to_update (dict of field names and new values)
### Return Values
- Updated Child record when update is successful
- Note: error is raised if fields_to_update contains invalid field names or values, or if the user does not exist
### Tests
1. Child record is updated when Child is present and fields are valid
2. Validation errors raised when fields_to_update contains invalid fields or values
3. Error raised when Child does not exist
--- 

# Page Data Access Tests

### Login
**Use Case Name:** Login form starts user session  
**Description:** Verify login page works properly  
**Pre-conditions:** BabySteps server is running  
**Test Steps:**  
1. Login with valid credentials and confirm dashboard opens.  
2. Logging in with invalid credentials and notification informs user.

### Registration
**Use Case Name:** Alternative form of login to create user  
**Description:** Confirm that entering in data in form can successfully generate new user data.  
**Pre-conditions:** BabySteps server is running  
**Test Steps:**  
1. Test form by filling in required data and confirming.  
    - This should create a new user account and direct the user to their dashboard.
2. Failing to enter all required information does not allow the user to proceed and displays errors for any invalid entries in fields.

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
2. Press edit button to be redirected to editing page. 

### Child Profile Page
**Use Case Name:** View/edit Child information  
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