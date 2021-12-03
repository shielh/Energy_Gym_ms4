# Energy Gym

The live version of the site is available [here]()

This project was created for my fourth and final Milestone Project with Code Institute in order to display my knowledge and understanding 
of HTML, CSS, JavaScript, Python+Django, MySQL and Stripe payments.

I remember I really wanted to create a website for a gym for my first project but I held out until now to complete it so I could add the features I wanted to add and have it looking as professional as possible. As someone who is equally passionate about fitness and technology, I know the huge effect a good website can have on the perception of your business. Down the line, I would love to be able to open my own fitness studio so this project is going to be the first step in acheiving that goal. I want this site to be simple and sleek with strong images and minimal text. This site will be the place users come to sign up easily and be able to purchase their membership option. The members will also be able to leave reviews on the gym and the products to create a community feel where feedback is always appreciated.

---

## Table of Contents
* [User Experience](#User-Experience)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [User stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Font](#Font)
            * [Images](#Images)
            * [Colour Scheme](#colour-scheme)
* [Features](#Features)
    - [Future Features to Implement](#future-features-to-implement)
* [Technologies Used](#Technologies-Used)
    - [Languages](#languages)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Tools](#tools)
* [Testing](#testing)
* [Security](#security)
* [Deployment](#deployment)
    * [Initial Creation](#initial-creation)
    * [Deployment to Heroku](#deployment-to-heroku)
        - [Create the app on Heroku](#create-the-app-on-heroku)
        - [Connect Heroku to Github](#connect-heroku-to-github)
        - [Set environment variables](#set-environment-variables)
        - [Automatic Deployment](#automatic-deployment)
* [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

--- 

## User Experience
### The Strategy Plane
Energy Gym is a site that myself and a friend want built for a potential business idea. Both of us are keen gym goers and really appreciate the power of a good website. Down the line, we plan to open a gym in Dublin city and we will use this project as the beginning of our new, exciting adventure.

We both have similar opinions on how our site shoud look and function. We want a clean , classy site with sharp images and minimal text. We want users to be able to be create an account and have the choice of four membership options - 1, 3, 6 months or annual memberships. Users will be able to purchase membership options, class bundles and gym merchandise on the site and down the line many more features will be added which I will expand onmore in the future features section.

### User stories
- As a first time user, I want to be able to easily navigate across the site so I can find the content quickly
- As a first time user, I want to know the purpose of the site immediately upon arrival
- As a first time user, I want to be able to find information about the membership options available at the gym
- As a user I want the site to be responsive across all devices
- As I user I want to be able to easily create an account
- As a user I want to be able to select a membership appropriate for my life
- As a user, I want to be able to view my order in the cart before paying to review
- As a user I want to be able to pay securely
- As a logged in user I want to be able to leave a review on the review section
- As a user, I want to be able to view other users reviews
- 
- 

### User stories - Admin
- As an admin user, I want to be able to add, edit and delete products on the site
- As an admin user, I want to be able to delete reviews that might contain harmful or inappropriate content
- 

### The Scope Plane
#### Features
##### Site Wide Features
- Navbar with site logo  "Energy", directing users back to the home page
- Navbar containing links to Home, About, Products, Account and Cart
- Navbar containing search bar
- Responsive navbar on mobile device, collapsing into burger icon

##### Home page
- Hero-video on landing page
- Button in middle of video prompting user to sign up 
- Description of type of products available
- Button linking to products page

##### About page
-

##### Products page
- Contains headers corresponding to category type of products
- Contains product images, price, name and description
- Each product image contains a link to product description page
- 

##### F


### Tools
- [GitHub](https://github.com/) 
    - This is the hosting site where I first created the repository for this webpage and also where the live site is deployed from 
- [Git](https://git-scm.com/) 
    - This is the version control software used where can I commit and push the updated information to the hosting website GitHub
- [MongoDB](https://www.mongodb.com/)
    - This was used for the database
- [BootsWatch](https://bootswatch.com/)
    - This was used as a theme for Bootstrap
- [PyMongo](https://pymongo.readthedocs.io/)
    - This was used as a tool to allow interaction between Python and MongoDB
- [Heroku](https://id.heroku.com)
    - This was used to deploy the live website
- [Balsamiq](https://balsamiq.com/) 
    - This was used to create my rough wireframes
- [Favicon](https://favicon.io/)
    - This was used to create the sites Favicon of an olive branch
- [Font Pair](https://fontpair.co/) 
    - This was used to choose complementary fonts
- [Tiny JPG](https://tinyjpg.com/) 
    - This was used this to compress my images
- [ClipArtKey](https://www.clipartkey.com/)
    - This was used to download the olive branch image used above the footer of the site
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
    - This was used to inspect elements on the page and help debug issues involving the 
    site layout
- [PEP8 Online](http://pep8online.com/)
    - This was used to check for PEP8 compliance
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    - This was used to test the CSS code for any errors
- [W3C Markup validator](https://validator.w3.org/)
    - This was used to test the HTML code for any errors
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - This was used as a web template engine for the Python language 
- [Web Accessibility](https://www.webaccessibility.com/)
    - This was used to test the accessibility of this site for users with disabilities


[Back to top](#Table-of-Contents)

---

## Testing
The testing documentation can be found [here](TESTING.md)

---

## Security 
I have stored all sensitive information in my env.py file which is ignored. Any user that registers an account will have their password undergo password hashing as an extra security measure. 


## Deployment 
### Initial Creation
Wedding App was first created by completing the following steps on GitHub:
1. Open [Github](https://github.com/) page up in browser
2. Log in using your username and password
3. Click the "New" green button to the left-hand side repository section
4. Click template dropdown menu and select the "Code Institute Full Template"
5. Enter name of project "Energy_Gym_MS4"
6. Click "Create repository"
7. Click the green "Gitpod" button ONCE to redirect to the Gitpod workspace
8. Open via [Gitpod Workspaces](https://gitpod.io/workspaces/) only, from then on

Throughout development, three primary commands were used with the CLI [Git](https://git-scm.com/) and were as follows :

- "git add" followed by the file name you wish to stage or "git add ." stages all unstaged files
- "git commit -m" followed by a detailed comprehensive comment pertaining to the changes made since the previous commit
- "git push" makes all changes visible on the GitHub Repo

In order to deploy the site to Heroku, the four following steps must be followed:
1. Create a requirements.txt file that contains the names of packages being used in Python. It is critical to update this file if other packages or modules are installed during project development to reflect the current requirements by using the following command:
- pip freeze --local > requirements.txt
2. Create a Procfile that contains the name of the application file so that Heroku knows what to run. Ensure to remove the blank line at the beginning of the Procfile as this may cause problems.
3. Push these files to GitHub.
4. Install `psycopg2` and `dj_datatbase_url` in your workspace cli.

When the above steps are complete, the app is ready to deploy to Heroku:

### Deployment Steps

1. Log into Heroku .
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.

### Connect Heroku app to Github repository

1. In heroku select the deploy tab.
2. Click github button.
3. Enter the repository name and click search.
4. Select the relevant repository and click connect. 

### Add Heroku Postgres Database
1. Click the resources tab in heroku.
2. Under Add-ons search for heroku postgres.
3. Click on heroku postgres when it appears. 
4. Select the Hobby Dev-Free option in plans. 
5. Click submit order form.

### Setting up environment variables
1. In the heroku settings click the reveal config vars button and set the following variables:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - DATABASE_URL
    - EMAIL_HOST_PASS
    - EMAIL_HOST_USER
    - SECRET_KEY
    - STRIPE_PRICE_ID
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - STRIPE_WH_SECRET
    - USE_AWS

## Code
Code institutes Boutique Ado project
https://www.youtube.com/watch?v=lSX8nzu9ozg
https://www.youtube.com/watch?v=fEoQsPvcZGs
https://getbootstrap.com/docs/5.0/components/collapse/