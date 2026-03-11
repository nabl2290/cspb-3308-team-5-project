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