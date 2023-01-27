# Balanced News



- 
This is the 4th portfolio project developed as part of the Code Institute Diploma in Full Stack Development. It was created to demonstrate skills acquired using Django to design and develop websites that offer full CRUD (create, read, update and delete) functionality.

![Multi Device Screenshot]()

## Demo

[View the live project here.]()

## TOC

- [User Experience (UX)](#user-experience-ux)
  - [Project Aims](#project-aims)
  - [User Stories](#user-stories)
  - [Agile Methodology](#agile-methodology)
  - [Design](#design)
    - [Wireframes](#wireframes)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Images and Iconography](#images-and-iconography)
    - [Database Schema](#database-schema)
    - [Design changes](#design-changes)
- [Features](#features)
  - [Features Not Implemented](#features-not-implemented)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Python Modules and Packages/Frameworks Used](#python-modules-and-packagesframeworks-used)
  - [Programs and Tools Used](#programs-and-tools-used)
- [Testing](#testing)
  - [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Remaining Bugs](#remaining-bugs)
- [Deployment](#deployment)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
  - [Deploying with Heroku](#deploying-with-heroku)
- [Credits](#credits)
  - [Online resources](#online-resources)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

## User Experience (UX)

### Project Aims

The initial aims of the project which formed the basis for user story creation were identified as the following:

- 

### User Stories

NOTE: The **Staff Member** role was renamed to **Customer** towards the end of development. This was based on feedback to bring the role further in line with the site purpose but user stories still refer to this role as **Staff Member**.

Acceptance criteria for each user story can be viewed within the linked GitHub issue.

#### Epic: News Posts
User Stories

1. As a Site User, I can view a paginated list of posts so that I can select a post I want to view. [Github Issue #1](https://github.com/qburn93/balanced-news-app/issues/1)

2. As a Site User, I can view a news feed table so that I can select one to read. [Github Issue #2](https://github.com/qburn93/balanced-news-app/issues/2)

3. As a Site User, I can click on a news post I want to read so that I can read the full text. [Github Issue #3](https://github.com/qburn93/balanced-news-app/issues/3)

4. As a Site User/Admin, I can view comments on an individual news post so that I can read the conversation. [Github Issue #4](https://github.com/qburn93/balanced-news-app/issues/4)

5. As a Site Admin, I can create, read, update and delete news posts so that I can manage my news site content. [Github Issue #8](https://github.com/qburn93/balanced-news-app/issues/8)

#### Epic: Comments and Interactions
User Stories

1. As a Site User, I can register an account so that I can comment and like. Github Issue #5[Github Issue #5](https://github.com/qburn93/balanced-news-app/issues/5)

2. As a Site User, I can leave comments on a post so that I can be involved in the conversation. [Github Issue #6](https://github.com/qburn93/balanced-news-app/issues/6)

3. As a Site User, I can like or unlike a news post so that I can interact with the content. [Github Issue #7](https://github.com/qburn93/balanced-news-app/issues/7)

4. As a Site Admin, I can approve or disapprove comments so that I can filter out unwarranted comments. [Github Issue #9](https://github.com/qburn93/balanced-news-app/issues/9)

#### Epic: Filtering and Viewing
User Stories

1. As a Site User, I can filter news stories by topic or category so that I can easily find the stories that interest me the most. [Github Issue #10](https://github.com/qburn93/balanced-news-app/issues/10)

1. As a Site Admin, I can create draft posts so that I can finish writing the content at any time. [Github Issue #11](https://github.com/qburn93/balanced-news-app/issues/11)

1. As a Site User, I can easily see what political view each news post belongs to so that I can get a better view of the political landscape of the site. [Github Issue #12](https://github.com/qburn93/balanced-news-app/issues/12)

1. As a Site User, I can view likes so that I have a clear view of popular opinions. [Github Issue #13](https://github.com/qburn93/balanced-news-app/issues/12)

### Agile Methodology

All user stories were entered as issues in a GitHub Kanban project and assigned labels using the MoSCoW prioritization technique. The live project board can be found on the repository's project tab (classic project section as of 07/22) or on the following link:

[Balanced News - Posting System User Stories - Kanban Board](https://github.com/users/qburn93/projects/9).

Pull requests where linked with a user story when they contributed to completion of the acceptance criteria.

### Design

#### Wireframes

I created Wireframes to visualize the site's design and act as a template to use when developing the templates. When designing the site I wanted to ensure the site looked and functioned just as well on mobile as larger viewports.

- [Wireframe Links Mobile]()
- [Wireframe Links Desktop]
  - (https://i.imgur.com/dWVFuWU.png)
  - (https://i.imgur.com/LqTkFtl.png)

#### Colour Scheme



![Background Colour]()


#### Typography

Google fonts was used in this project with both fonts selected for their legibility and simplicity.

[]() - Use in headings.
[]() - Use in paragraphs and labels.

#### Images and Iconography



#### Database Schema



![Image of Database Schema]()

### Libraries

#### Installed Libraries

| Package       | Version        |
| ------------- | ------------- |
| asgiref | 3.5.2 |
| cloudinary | 1.30.0 |
| coverage    |           7.0.3 |
| dj-database-url | 0.5.0 |
| dj3-cloudinary-storage | 0.0.6 |
| Django | 3.2.16 |
| django-crispy-forms | 1.14.0 |
| django-extensions | 3.2.1 |
| gunicorn | 20.1.0 |
| psycopg2 | 2.9.5 |
| 
| sqlparse | 0.4.3 |


## Features

1. Home Page

    - The functionality of the site is restricted to registered users in line with its purpose to assist individuals. The home page was therefore designed to welcome customers and provide an introduction to make the site purpose clear. There are clear links to encourage visitors to signup and allow existing users to login. The home page is fully responsive and is based on the site's base template, therefore includes the site wide navigation and footer elements.

        ![Home Page](docs/features/features-homepage-min.png)

1. Navigation

    -

    

    - 


    - Administrators see links to manage their profile and logout, but also the link to the user search page.

        ![NavBar - administrator]()

    - Navigation on smaller viewports

        ![NavBar - collapsible]()

1. Signup, Login and other account management pages

    - *django-alauth* was implemented to handle account creation and management of email verification, email address management, password change, etc.

    - The *django-allauth* signup page shown below was extended to request a user's name as part of the signup process. This also demonstrates how the styling of the *django-allauth* templates were altered to make them cohesive with the rest of the site. Forms were styled using the *crispy-bootstrap5* package.

        ![Account Signup]()



1. Filters

    - The post list has the potential to become very crowded as more news post are added and comments logged. To ease this issue the *django-filters* package was used to create a custom filterset that allows admins/users to filter news posts by Status and sort by creation date, or political views. 

        ![Filtering]()


1. User Management - Administrator Role

    - 

1. Messaging and Email

    - Bootstrap toasts were used in conjunction with Django messaging framework to report success and errors to customers as they used the site.

    - Entering an invalid url (integer) will direct users to a custom 404 Error page. If the user enters a string as the post slug, they will be directed to the home page and be informed of the error.

        ![Messaging - Toasts]()

   

### Features Not Implemented


### Future Features

- Given more time, I would add categories.
- Given more time and resources I would add, trending posts based on number of clicks for the post.
- Animated bar at the top of the page highlighting most recent important news posts. 

## Technologies Used

### Languages Used

- HTML5
- CSS3
- Python
- Javascript

### Python Modules and Packages/Frameworks Used

- Built-in Packages/Modules
  - [datetime](https://docs.python.org/3/library/datetime.html) - Used to get current time in a timezone aware format to use when updating posts.
  - [os](https://docs.python.org/3/library/os.html) - This module provides a portable way of using operating system dependent functionality.

- External Python Packages
  - [cloudinary](https://pypi.org/project/cloudinary/1.29.0/) - Used for the post Image Model field, Image upload and deletion.
  - [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/0.6/) - Used to style form using Bootstrap5
  - [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) - Allows the use of 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
  - [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/0.0.6/) - Facilitates integration with Cloudinary by implementing Django Storage API.
  - [Django](https://pypi.org/project/Django/3.2.14/) - High-level Python Web framework used to develop the project
  - [django-allauth](https://pypi.org/project/django-allauth/0.51.0/) - Set of Django application used for account registration, management and authentication.
  - [django-crispy-forms](https://pypi.org/project/django-crispy-forms/1.14.0/) - Used to format form elements and layout.
  - [django-filter](https://pypi.org/project/django-filter/22.1/) - Application that allows dynamic QuerySet filtering from URL parameters.
  - [django-model-utils](https://pypi.org/project/django-model-utils/) - Easily add choices to a django model field.
  - [django-summernote](https://pypi.org/project/django-summernote/0.8.20.0/) - Allows easy use of the Summernote WYSIWYG editor in Django projects.
  - [gunicorn](https://pypi.org/project/gunicorn/20.1.0/) - Python WSGI HTTP Server
  - [Pillow](https://pypi.org/project/Pillow/9.2.0/) - Fork of PIL, the Python Imaging Library which provides image processing capabilities.
  - [psycopg2](https://pypi.org/project/psycopg2/2.9.3/) - Python PostgreSQL database adapter

### Programs and Tools Used

- [Google Fonts:](https://fonts.google.com/)
  - Google fonts import statements were used as part of this project to make use
    of the Poppins and Cabin Round fonts which are used on all pages of the
    website.
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap was used through the project to style the project and create responsive elements/layouts.
- [Visual Studio Code:](https://code.visualstudio.com/)
  - Visual Studio Code was used as my code editor for this project.
- [Git](https://git-scm.com/)
  - Git was used for version control, using the terminal to commit to Git and
    Push to GitHub.
- [GitHub:](https://github.com/)
  - GitHub is used to store the projects code after being pushed from Git.
- [Balsamiq:](https://balsamiq.com/)
  - Balsamiq was used to create the [wireframes](#wireframes) during the design
    process.
- The following modules were installed or enabled in [Visual Studio
Code](https://code.visualstudio.com/) to assist with formatting and code
linting:
  - [flake8](https://github.com/pycqa/flake8) - Code Linter
  - [black](https://github.com/psf/black) - Code Formatter
- The following [Visual Studio Code](https://code.visualstudio.com/) extensions
  were utilized in the production of this project:
  - [Rewrap](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap) - Used to wrap comments.
  - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) - Used to spell check content and commits.
  - [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) - Makes indentation easier to read.
  - [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) - Generates python docstrings templates automatically

## Manuel Testing

<summary>See Testing User Stories</summary>

#### Testing User Stories - Users

To avoid unnecessary repetition of images, only the feature being referred to will have screenshots. Information on how to navigate to the feature referred to will be described within its relevant table reference. 

1. As a user, I want to use the navigation bar so that I can seamlessly navigate around the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Nav Bar  | Log in and scroll to the top of any page  | Nav Bar to be displayed along the top of the page or via a hamburger toggle if on a smaller screen    | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="">
</details>
<br>

2. As a user, I want to see visual indicators for example of having liked a post / followed a user so that I can tell if I have previously liked that post.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Like Button  | Log in and navigate to a post detail page via feed by clicking on the post. Below the post click on the heart icon to like or unlike the post  | Post heart indicator to visually reflect the current users status with regards to liking the post and the total like tally to plus or minus one like dependant on if the click is a like or unlike  | Works as expected |

<details>
<summary>Screenshots</summary>
<a href="https://imgur.com/qsB4itk"><img src="https://i.imgur.com/qsB4itk.png" title="source: imgur.com" /></a><br>
<a href="https://imgur.com/TbVW9ea"><img src="https://i.imgur.com/TbVW9ea.png" title="source: imgur.com" /></a>
</details>
<br>


4. As a user, I want to view post comments so that I can fulfil the aim of the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Comment on post  | Log in and navigate to a post detail page via feed by clicking on the post. Below the post image view the comments.  | User to be able to read all comments on the post or be made aware of no comments if there are none | Works as intended |

<details>
<summary>Screenshots</summary>
<a href="https://imgur.com/7B7o4NX"><img src="https://i.imgur.com/7B7o4NX.png" title="source: imgur.com" /></a>
</details>
<br>

5. As a user, I want to comment on other posts so that I can interact with other users.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Comment on post  | Log in and navigate to a post detail page via feed by clicking on the post. Below the post image fill in the comment form and click on the add comment button.  | User to fill in the comment form and when submitted will be added to the comments like for the post. | Works as expected |

<details>
<summary>Screenshots</summary>
<a href="https://imgur.com/QF04QKO"><img src="https://i.imgur.com/QF04QKO.png" title="source: imgur.com" /></a>
</details>
<br>

6. As a user, I want to log in so that I can access my account, view my profile, pictures and other user's pictures.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Log in  | Navigate to the Balanced News site and from the landing page navigate to log in, enter your username and password then click on the log in button.  | User to log in and be redirected to their profile page | Works as expected |

<details>
<summary>Screenshots</summary>
<a href="https://imgur.com/nf4lrin"><img src="https://i.imgur.com/nf4lrin.png" title="source: imgur.com" /></a>
</details>
<br>

7. As a user, I want to log out so that other users using the same device cannot access my account.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Log out  | From any page whilst logged in click on the log out button located in the right hand corner of the nav bar, or if using a small screen device from the last item in the list from the hamburger menu toggle.  | User to log out successfully and be presented with the logged out page | Works as intended |

<details>
<summary>Screenshots</summary>
<a href="https://imgur.com/FtrxbUu"><img src="https://i.imgur.com/FtrxbUu.png" title="source: imgur.com" /></a>
</details>
<br>

8. As a new user, I want to register an account with Pic Pals so that I can become a member and use the app as intended.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Register  | Navigate to the balanced News site and click on the Sign up button located below the log in section. Fill in the form with the required fields for registration and click on the create account button.  | User to create an account with the information provided in the form    | Works as intended |

<details>
<summary>Screenshots</summary>
<a href="https://imgur.com/WLDyGsg"><img src="https://i.imgur.com/WLDyGsg.png" title="source: imgur.com" /></a>
</details>
<br>

9. As a user, I want to view the Home Page so that I can understand what the website is about, create an account or log in.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Home Page  | Navigate to the Balanced News landing page  | Users will be presented with a small description of the sites purpose | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="">
</details>
<br>

10. As a user, I want to view how many likes a post has so that I can gauge how popular a post is.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Like count  | Log in and navigate to any post detail page via one of the methods to do so as explained above. Scroll down to below the post image and the like count will be displayed  | To view the total amount of likes a post has. | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="">
</details>
<br>
#### Testing User Stories - Site Owner

1. As a admin, I want to edit posts so that I can correct spelling mistakes.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Edit Post  | Log in to the admin panel and navigate to the post detail by clicking on the post in question. At the top of the post card click on the edit button, the edit post form will show, update the caption field to the desired caption and click update to save changes and redirect back to the post detail page.  | Caption for the post to be updated | Works as expected |

<details>
<summary>Screenshots</summary>
<img src=""><br>
<img src=""><br>
<img src=""><br>
<img src="">
</details>
<br>

2. As the site owner, I would want to have the ability to remove posts so that I can keep the app clean and friendly.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Delete Post  | Admin to log into the admin site of the app and from there go to the posts object and delete the required post database entry  | Admin to log into the admin site and have the ability to delete a post of any user as this profile is a super user | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="">
</details>
<br>

3. As the site owner, I would want the site to be fully responsive so that users can use it across multiple devices and create a good user experience.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Responsiveness  | Allow users to use the site on their own device regardless of the size  | The site is functional and works as intended on a range of device screen sizes  | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="">
</details>
<br>

### Bugs

#### Fixed Bugs

-

#### Remaining Bugs
- I have a migration warrning when i tried to add the categories panel, at one point during the project i had categories in the nav bar and in the class modal of Post, but later decided i will leave it for future implementations, so i removed everything related to category from the code, but when running the server online command im getting a red warning that 1 migration is behind, I will try to fix this before submission.


## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on
our GitHub account to view and/or make changes without affecting the original
repository by using the following steps...

1. Log in to GitHub and locate the [GitHub
   Repository](https://github.com/ianmeigh/support-hub)
1. At the top of the Repository (not top of page) just above the "Settings"
   Button on the menu, locate the "Fork" Button.
1. Click the button (not the number to the right) and you should now have a copy
   of the original repository in your GitHub account.

### Making a Local Clone

**NOTE**: It is a requirement of the is project that you have Python version 3.8 or higher installed locally.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/qburn93/support-hub).
1. Under the repository name, click "Code".
1. To clone the repository using HTTPS, under "HTTPS", copy the link.
1. Open your local terminal with git installed
1. Change the current working directory to the location where you want the cloned directory to be created.
1. Type `git clone`, and then paste the URL you copied in Step 3.

    ```console
    ~$ git clone https://github.com/qburn93/project-1.git
    ```

1. Press Enter. Your local clone will be created.

    ```console
    $ git clone https://github.com/qburn93/project-1.git
    > Cloning into `test-dir`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```

    [Click here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explanation of the process above with pictures.

1. Change the current working directory to the cloned project folder (this will be a child directory in the location you cloned the project).

1. It is recommended to use a virtual environment during development ([learn more about virtual environments](https://realpython.com/python-virtual-environments-a-primer/)). If you would prefer not to use on please skip the following steps:
    1. Create a virtual environment in the projects working directory by entering the following command in the same terminal window used for the steps above `python3 -m venv .venv`.
    1. Before use, the virtual environment will need to be activated using the command `source .venv/bin/activate` in the same terminal window used previously.
1. Packages required by the project can now using the command `pip install -r requirements.txt`
1. In the cloned directory, rename the file `.env-example` to `.env` and populate it with the information required.
1. Make django migrations using the command `./manage.py migrate`.

### Deploying with Heroku

**NOTE**: It is a prerequisite of deployment to Heroku that you already have access to the following:

- A Cloudinary account, create one for free at [https://cloudinary.com](https://cloudinary.com).
- An account with an email service that can be used to send confirmations and notification to users.
  - Gmail can be used for small demonstration or test projects. An 'app' password will be required for use in this project. Refer to the following Google support article to set one up):
    - [https://support.google.com/accounts/answer/185833](https://support.google.com/accounts/answer/185833)
  - Visit the following Google support article to learn more about GMail sending limits:
    - [https://support.google.com/a/answer/166852](https://support.google.com/a/answer/166852)
  - A service like [SendGrid](https://sendgrid.com) or [mailgun](https://www.mailgun.com) should be used in production environments.

**NOTE**: It is assumed you have followed all deployment instructions listed in this readme starting with the section titled 'Forking the GitHub Repository'.

1. Log in to [Heroku](https://www.heroku.com/) and if not taken there automatically, navigate to your personal app dashboard.
1. At the top of the page locate the 'New' drop down, click it and then select 'Create new app'.
1. Give your application a unique name, select a region appropriate to your location and click the 'Create app' button.
1. Your app should now be created, so from the menu towards the top of the page select the 'Resources' section.
1. Search for 'Heroku Postgres' under the Add-ons section and add it.
1. From the menu towards the top of the page select the 'Settings' section and lick 'Reveal Config Vars' in the Config vars section. Enter the following key / value pairings:
    1. Key as `ALLOWED_HOSTS` and the value as the name of you project with '.herokuapp.com' appended to the end e.g.  `example-app.herokuapp.com`. Click the Add button.
    1. Key as `CLOUDINARY_URL` and the value as your cloudinary API Environment variable e.g. `cloudinary://**************:**************@*********`. Click the Add button.
    1. Key as `EMAIL_HOST_PASSWORD` and the value as the password or value provided by your email service of choice. Click the Add button.
    1. Key as `EMAIL_HOST_USER` and the value as the the email address or value provided by your email service of choice. Click the Add button.
    1. Key as `SECRET_KEY` and the value as a complex string which will be used to provide cryptographic signing. The use of a secret key generator is recommended such as [https://djecrety.ir](https://djecrety.ir/). Click the Add button.
    1. Ensure the key `DATABASE_URL` is already populated. This should have been created automatically by Heroku.
    1. The `DATABASE_URL` should be copied into your local `.env`, created during the cloning process.
1. Open the `.env` file in the project directory and delete the key / value pair `DEV_ENVIRONMENT_DATABASE = True` before saving the file. This can be added back after the next step to ensure local development changes will not alter the remote database.
1. Running migrations on the remote database
    1. Open your local terminal and change the current working directory to that of the project folder.
    1. Make django migrations using the command `./manage.py migrate`.
1. Navigate to the 'Deploy' page using the menu towards the top of the page.
1. Select 'GitHub' from the 'Deployment method' section and you will be prompted to 'Connect to GitHub'.
1. Once connected to your GitHub account you will be able to search for your repository which contains the forked 'Support-Hub' repository.
1. Once the repository is found click 'Connect'.
1. At the bottom of the page find the section named 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.
1. Once deployment is complete, click the 'View' button to load the URL of the deployed application.

## Credits

### Online resources

- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.1) and [Examples](https://getbootstrap.com/docs/5.1/examples/)
- [Django-Summernote Documentation](https://github.com/summernote/django-summernote)

### Code

The following credits represent cases where code was adapted or used from external resources. Some credits in the code would have broken the PEP8 character limit and as such have links to this section in the the source code:
- **#1** - 
  - CREDIT:From Code institute's django-blog module i used the comment class and post, but added and updated it with Political leaning.  
  - URL: [Code institute credit](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/04_building_the_models/blog/models.py)

- **#2** - 
  - 
  


### Media

- 

### Acknowledgments

