# Testing

## Automated Tests

Due to the time constraints of this project, partial automated testing was implemented as part of the release phase.

## Manual Tests

### Methodology

Manual testing occurred regularly throughout local development, making use of statements that would print information to the console and use of the Django debug pages.

Each function of the website had specific testing requirements which were documented as test cases. The aim of documenting these test cases was that they could be run before pull requests were committed to ensure no breaking changes were introduced. Tests were documented as the site evolved so new tests for new functionality could be easily added.

### Test Cases

&nbsp;

#### Registration Page

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Form Validation | 1 | Try to submit empty form | Form validation will prompt for user action | PASS |
| Form Validation | 2 | Try to submit invalid email address  | Form validation will prompt for user action | PASS |
| Form Validation | 3 | Try to submit username that is already taken | Form validation will prompt for user action | PASS |
| Form Validation | 4 | Try to submit non-complex, not matching passwords | Form validation will prompt for user action | PASS |
| Form Validation | 5 | Remove the required attribute using browser console tools and submit with no first or last name but other valid fields | Form validation will prompt for user action | PASS |
| Registration success | 6 | Enter unique, valid information for all fields | User is notified with a success message and redirected to the email verification page. Verification email is send to email address entered in registration form. Account can be seen in the Django admin panel | PASS |

&nbsp;

#### Create and Edit Posts

Tests for the creation and editing of posts were completed using an account with the role of Customer followed by an account with the role of Technician. The following tests are applicable for post creation and editing so are repeated for each activity.

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Text Field Validation | 1 | Try to submit empty form |  | PASS |
| Text Field Validation | 2 | Enter a description with leading white-space and submit the form | Form validation will prompt for user action | PASS |
| Text Field Validation | 3 | Enter a description and title with fewer characters than the required amount (10 for title and 20 fro description) and submit the form | Form validation will prompt for user action | PASS |
| Image Field Validation | 4 | Try to upload a GIF | Form validation will notify the user the image format is not permitted and remind them of the accepted formats | PASS |
| Image Field Validation | 5 | Try to upload a PDF | Form validation will notify the user the image format is not permitted and remind them of the accepted formats | PASS |
| Image Field Validation | 6 | Try to upload a JPEG larger than 3MB | Form validation will notify the user the image is too large (bytes) and remind them of the maximum accepted file size | PASS |
| Image Field Validation | 7 | Try to upload a Text file with the file extension changed to png | Form validation will notify the user the image format is not valid or corrupted | PASS |
| Image Field Validation | 8 | Try to upload a CSV file with the file extension changed to png | Form validation will notify the user the image format is not valid or corrupted  | PASS |
| Image Field Validation | 9 | Enter valid information for all fields | post created, user redirected to the newly created posts detail view and notified via message. Post matches all information as entered in the form (author, status, etc.) | PASS |

&nbsp;


&nbsp;

#### Navigation and Post View

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Customer can view their own profile | 4 | Navigate to a logged on customer profile page | Profile is visible | PASS |
| Customer cannot view the profiles of other users | 5 | Navigate to the profile of another valid user using a manually input URL | Redirected to a 403 page | PASS |
| Technician can view their own profile | 6 | Navigate to a logged on customer profile page | Profile is visible | PASS |
| Technician cannot view the profiles of other users | 7 | Navigate to the profile of another valid user using a manually input URL | Redirected to a 403 page | PASS |




&nbsp;

#### User Search

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Only administrator role can view User Search page | 1 | Login as customer and check if the navigation link to the user search is visible and try to navigate to the url manually | Link to user search not visible and will be redirected to 403 page | PASS |
| Only administrator role can view User Search page | 2 | Login as technician check if the navigation link to the user search is visible and try to navigate to the url manually | Link to user search not visible and will be redirected to 403 page | PASS |
| Profiles can be edited and only Role and Team can be changed | 5 | Logged in as Administrator, visiting the user profile of another user and selecting to edit.. the role and team can be successfully saved | User Role and Team can be changed. | PASS |

&nbsp;

#### Profile View and Edit (other than administrator)

| Testing | Test # | Steps | Expected Outcome | Results |
| - | - | - | - | - |
| Form Validation | 1 | Change first and last name and try to submit | From validation will prompt for user action | PASS |
| Form Validation | 2 | Enter username that is already taken | From validation will prompt for user action | PASS |
|

&nbsp;

## Code Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/nu/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) Services were used to validate the project's HTML and CSS files to ensure there were no syntax errors or warnings.

Tests passed with the exception of pages that made use of the *django-summernote* widget. The majority of these errors were fixed (as discussed in the [Changes as a result of testing](#changes-as-a-result-of-testing) and the [bugs](README.md#bugs) sections), but one error caused by *django-summernote* widget has been ignored.

![HTML validation error 3]()



Please click the page name to view a screenshot of the validation check.

| Page | Result |
| - | - |
| [Home Page - Not Authenticated]() | PASS |
| [Home Page - Authenticated]() | PASS |


\* Passed with known error ignored, caused by *django-summernote*.

### CSS

No validation errors reported.

- [Results for CSS]()



### Python

No validation error reported when using the [PEP8 Online Check Tool](http://pep8online.com/)

| App/Parent folder | File | Result |
| - | - | - |
| accounts | [admin.py]() | PASS |
| accounts | [forms.py]() | PASS |
| accounts | [models.py]() | PASS |
| accounts | [urls.py]() | PASS |
| accounts | [views.py]() | PASS |
| accounts/tests | [test_urls.py]() | PASS |
| common | [utils.py]() | PASS |


### JavaScript

No validation errors reported testing with [JSHint]().

![Results for JavaScript]()

## WAVE - Web Accessibility Evaluation Tool

All pages were tested using the [WAVE Firefox extension](). No errors were returned for any pages and the report for the homepage can be viewed below:

![Results for JavaScript]()

## Lighthouse Scores

Most pages of the site when tested with a desktop or mobile device view performed very well, with pages scoring above 90% for performance and accessibility, and 100% for Best Practices. 2 pages under mobile device testing dropped to 87% performance (with this number varying slightly under repeated testing).

Original post creation page score - Mobile

![Original post creation page score]()

Original post list page score - Mobile

![Original post list page score]()



## Devices used for manual testing

Site was tested using the following desktop and mobile browsers:

- Chrome (v.103), Firefox (v.103), Firefox Developer Edition (v.104), GNOME Web (v.41.3, using WebKitGTK 2.34.4), Safari (iOS 15 on iPhone 7 and iPad 6th Gen).

Return to [README.md]()