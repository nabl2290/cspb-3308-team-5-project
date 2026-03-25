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
- `User`
- `Child`
- `FeedingEvent`
- `user_child` (TODO is this a "weak" table, or something else?)

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
TODO include children field here, or is that implicitly in the user_child table?

### Relationships

- One-to-many with `Child` through `user_child` table

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

TODO more tests?

## 2) Table: Child

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

## Notes
- Constraints enforced at DB and ORM levels (TODO confirm?)
- All access methods wrapped in service layer (TODO confirm?)
- Tests executable via integration test suite (TODO shall we plan to do this?)