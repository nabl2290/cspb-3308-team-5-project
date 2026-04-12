# Baby Steps Final Report
by Team 5 - FAAWN

## Project Title and Description
**Title**: Baby Steps

**Description**: Baby Steps helps parents track and manage their baby's schedule,
health, and milestones.

## Team Members
- Felice Forby
- Antonio Duran
- Alana Powell
- Will Hansen
- Nate Bliton

## Project Tracker
Trello Board: https://trello.com/b/XiGBDKNQ/team-fawn

## Demo Video
TODO

## Github Repository
https://github.com/nabl2290/cspb-3308-team-5-project

## Final Status Report
### What was completed
- An MVP version of the Baby Steps web application with the following features:
  - User registration and login
  - Dashboard with overview of each baby's data
  - Ability to add and edit baby profiles
  - Ability to add, view, and edit baby data. For MVP, we only implemented feeding event tracking.
  - User profile management
- Form validation and error handling
- Basic authorization to ensure users can only access their own data
- Unit tests for the database access methods

### What was in progress
- Better consistency of UI styling and design across the application
- More testing

### Future planned work
- Add more data tracking for babies, such as diaper events, sleep tracking, and weight tracking
- Implement calendar with ability to add appointments and reminders
- Add more detailed analytics and insights based on the tracked data
- Better data visualization
- Data export functionality for users to download their baby's data in CSV format

### Known issues and bugs
- Not mobile friendly yet
- Some style inconsistencies across pages
- User profile photo cannot be uploaded yet

## Other Documents
Source code is available in the Github repository linked above.

Additional documentation is also available in the repository:
- [Project Proposal](README.md)
- [How to set up and run the project](SETUP.md)
- [Weekly Progress Reports](WEEKLY_REPORTS.md)
- [Page Testing Documentation](PAGE_TESTING.md)
- [SQL Database Testing Documentation](SQL_TESTING.md)
- TODO - [Demo Video]()

## System Overview
We build both our backend and frontend using the Flask framework. The Flask backend handles the endpoint routing, database interactions, and business logic. The frontend is built using Flask's templating engine (Jinja) to render dynamic HTML pages with data pull from a SQLite database. Page styles were implemented using vanilla CSS. Our page templates allow for page-specific CSS to be included on a per-page basis to prevent styling conflicts.

### Architecture Summary
- **Backend**: Flask
- **Frontend**: Flask templates with HTML and CSS
- **Database**: SQLite

### Libraries and Plugins Used
- **Flask SQL Alchemy ORM**: database-to-model mapping and query
helpers
- **WTForms extension**: form helpers and validations
- **Pytest**: unit testing

## Testing
We implemented unit tests for our database access methods using the Pytest framework. These tests cover the basic CRUD operations for our database models, ensuring that data can be created, read, updated, and deleted correctly. We also performed manual testing of the application to validate expected behavior.
