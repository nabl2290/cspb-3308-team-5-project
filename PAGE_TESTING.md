# PAGE_TESTING.md

This document defines the **pages** the Baby Steps app will implement and waht is required to (1) render them correctly and (2) test them consistently.

---
## Conventions Used in This Document

### Parameter Types
- **Route params**: values embedded in the URL path (e.g.,
`/child/:child_id`)
- **Query params**: values after `?` in the URL (e.g., `?
tab=tasks`)
- **State params**: values passed through navigation state
(optional; avoid for critical data)
### Data Types

- **Auth state**: current user identity + session token
- **Database data**: data fetched from the database
- **UI state**: transient values like form fields, selected
filters, toggles
### Mockups
- Each page includes a screenshot from our Figma document.

---

# 1) Welcome Page

## Page Title
TODO Page Title

## Page Description
TODO Page Description (include a mockup or hand drawn image of the page, Figma for us)

## Mockup
![Welcome page](mockups/welcome.png)

## Parameters needed for the page
TODO Parameters needed for the page

## Data needed to render the page
TODO Data needed to render the page

## Link destinations for the page
TODO Link destinations for the page

## Tests for Verifying Rendering of the Page
TODO List of tests for verifying the rendering of the page


# 2) Login

## Page Title
Login

## Page Description
This page allows users to log in to their account using their email and password. It includes form validation and error handling for incorrect credentials.

## Mockup
![Login](mockups/login.png)

## Parameters needed for the page
- URL query params :
  - `error` to display error messages for unauthorized access (e.g., `?/login?error=You+are+not+authorized+to+access+this+page`)

## Data needed to render the page
None, as the user is not authenticated yet and no data is need to render the form.

## Link destinations for the page
- "New User?" to take user to Registration page → `/register`
- Submit button to submit login form → `/login` (POST request)

## Tests for Verifying Rendering of the Page
- **Form fields render**: Email and password input fields are displayed
- **Submit button present**: Login button is visible and enabled
- **Link to registration**: "New User?" link is visible and navigates to `/register`
- **Submit button posts form**: Clicking submit sends a POST request to `/login` with email and password
- **Error handling**: Incorrect credentials show an error message
- **Successful login**: Correct credentials redirect to user dashboard. Session data should be set to keep user logged in.

# 3) Register User

## Page Title
Sign Up

## Page Description
Allows new users to create an account by providing their name, email, and password. Includes form validation and error handling for missing fields, existing email addresses, and failed password confirmation.

## Mockup
![registration.png](mockups/registration.png)

## Parameters needed for the page
None

## Data needed to render the page
None, as the user is not authenticated yet and no data is need to render the form.

## Link destinations for the page
- "Have an account?" to take user to Login page → `/login`
- Submit button to submit registration form → `/register` (POST request)

## Tests for Verifying Rendering of the Page
- **Form fields render**: First name, last name, email, password, and confirm password input fields are displayed.
- **Submit button present**: Sign Up button is visible and enabled.
- **Link to login**: "Have an account?" link is visible and navigates to `/login`.
- **Submit button posts form**: Clicking submit sends a POST request to `/register` with the form data.
- **Error handling**: Missing fields, existing email, and password confirmation errors show appropriate error messages.
- **Successful registration**: Correct form submission creates the user, logs them in, and redirects them to user dashboard. Session data should be set to keep user logged in.

# 4) User Landing Screen

## Page Title
User Dashboard

## Page Description
Purpose: View and click into children and/or add feeding events or more children.

## Mockup
![dashboard.png](mockups/dashboard.png)

## Parameters needed for the page
- Route params: 
  - `user_id` (required) from `/user/<int:user_id>/dashboard`
- Query params (optional): 
  - `user_id`

## Data needed to render the page
- Auth state: current user id
- Database data:
  - User data
  - Child data

## Link destinations for the page
- HOME click → `/user/:user_id/dashboard`
- Profile → `/user/:user_id`
- Logout → `/logout`
- Edit → `/child/:child_id/edit`
- Child card/section → `/child/<int:child_id>`
- Add another baby → `/child/new`
- Add Feeding Event → `/feeding-event`

## Tests for Verifying Rendering of the Page
1. **Route param required**
   - Visiting `/dashboard/` without `user_id` shows error or redirects
2. **User header renders**
   - User name and information is displayed

3. **child information renders**
   - If children related to parent/user exists, it is displayed
   - If no feeding info exists , "No children to show " is displayed
4. **Child info only available to this Child's parent**
   - Non-parents cannot access (redirect or “access denied”)
6. **Links**
   - Clicking onto a child card directs the user to `/child/<int:child_id>`
   - “Add Feeding Event” navigates to `/feeding-event/new`

# 5) Add/Edit baby form

## Page Title
TODO Page Title

## Page Description
TODO Page Description (include a mockup or hand drawn image of the page, Figma for us)

## Mockup
TODO

## Parameters needed for the page
TODO Parameters needed for the page

## Data needed to render the page
TODO Data needed to render the page

## Link destinations for the page
TODO Link destinations for the page

## Tests for Verifying Rendering of the Page
TODO List of tests for verifying the rendering of the page

# 6) Profile

## Page Title
TODO Page Title

## Page Description
TODO Page Description (include a mockup or hand drawn image of the page, Figma for us)

## Mockup
TODO

## Parameters needed for the page
TODO Parameters needed for the page

## Data needed to render the page
TODO Data needed to render the page

## Link destinations for the page
TODO Link destinations for the page

## Tests for Verifying Rendering of the Page
TODO List of tests for verifying the rendering of the page

# 7) Child Profile

## Page Title
Child Profile

## Page Description
Purpose: view Child info, and view feeding events.

## Mockup
TODO update screenshot

## Parameters needed for the page
- Route params: 
  - `child_id` (required) from `/child/:child_id`
- Query params (optional): none

## Data needed to render the page
- Auth state: current user id
- Database data:
  - Child data
  - Child event data
- UI state:
  - Selected Child user info and data
  - Visualization - Table or Chart

## Link destinations for the page
- HOME click → `/user/:user_id/dashboard`
- Profile → `/user/:user_id`
- Logout → `/logout`
- Edit → `/child/:child_id/edit`
- Add Feeding Event → `/feeding-event`

## Tests for Verifying Rendering of the Page
1. **Route param required**
   - Visiting `/child/` without `child_id` shows error or redirects
2. **Child header renders**
   - Child name + child information is displayed
3. **Feeding information renders**
   - If feeding info for this child exists, it is displayed
   - If no feeding info exists for this child, "No Feeding Data" is displayed
4. **Child info only available to this Child's parent**
   - Non-parents cannot access (redirect or “access denied”)
6. **Links**
   - “Edit” navigates to correct route or opens modal
   - “Add Feeding Event” navigates to correct route or opens modal

# 8) Feeding Events

## Page Title
Feeding Event

## Page Description
Purpose: Be able to log the time, date, amount, and description of a child's feed/meal.

## Mockup
![feedevent.png](mockups/feedevent.png)

## Parameters needed for the page
- Route params: 
  - `/feeding-event/new` for new event
 
## Data needed to render the page
- Auth state: only available to logged in user
- Database data:
  - Child data
- UI state:
  - Selected Child info

## Link destinations for the page
- HOME click → `/user/:user_id/dashboard`
- Profile → `/user/:user_id`
- Logout → `/logout`
- Add Feeding Event → `/feeding-event`

## Tests for Verifying Rendering of the Page
1. **Child name renders**
   - Child name is displayed
2. **Only available if logged in**
   - Non-parents and logged out users cannot access (redirect or “access denied”)
  
# 9) Edit/Delete Feeding Event

## Page Title
Edit Feeding Event

## Page Description
Purpose: Be able to edit the time, date, amount, and description of a child's feed/meal or delete the event entirely.

## Mockup
![editfeedevent.png](mockups/editfeedevent.png)

## Parameters needed for the page
- Route params: 
  - `/feeding-event/<int:event_id>/edit` for editing an existing event
- Query params (optional): none

## Data needed to render the page
- Auth state: only available to logged in user
- Database data:
  - Child data
  - Feed data if updating/deleting previous input
- UI state:
  - Selected Child info
  - Selected event info

## Link destinations for the page
- HOME click → `/user/:user_id/dashboard`
- Profile → `/user/:user_id`
- Logout → `/logout`
- Edit Feeding Event → `/feeding-event/<int:event_id>`
- Delete Feeding Event → `/feeding-event/<int:event_id>` (DELETE request)
  
## Tests for Verifying Rendering of the Page
1. **Route param required**
   - Editing: Visiting `/feeding-event` without `event_id` shows error or redirects
2. **Child name renders**
   - Child name is displayed
3. **Previous event renders**
   - Editing an existing event, the respective information for that event is displayed and able to be changed
4. **Only available if logged in**
   - Non-parents and logged out users cannot access (redirect or “access denied”)
5. **Save event**
   - Selecting to update an event, updates the information for that event in the database.
6. **Deletion removes event**
   - Deleting an event removes it permanently from the database