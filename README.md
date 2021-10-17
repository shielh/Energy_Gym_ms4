# Energy Gym

The live version of the site is available [here]()

This project was created for my fourth and final Milestone Project with Code Institute in order to display my knowledge and understanding 
of HTML, CSS, JavaScript, Python+Django, MySQL and Stripe payments.

I remember I really wanted to create a website for a gym for my first project but I held out until now to complete it so I could add the features I wanted to add and have it looking as professional as possible. As someone who is equally passionate about fitness and technology, I know the huge effect a good website can have on the perception of your business. Down the line, I would love to be able to open my own fitness studio so this project is going to be the first step in acheiving that goal. I want this site to be simple and sleek with strong images and minimal text. This site will be the place users come to sign up easily and be able to purchase their membership option as well as book in for classes. The members will also be able to leave reviews on the classes to create a community feel where feedback is always appreciated.

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
Energy Gym is a site that myself and a friend want built for potential business idea. Both of us are keen gym goers and really appreciate the power of a good website. Down the line, we plan to open a gym in Dublin city and we will use this project as the beginning of our new, exciting adventure.

We both have similar opinions on how our site shoud look and function. We want a clean , classy site with sharp images and minimal text. We want users to be able to be create an account and have the choice of three membership options - 1 month, 3 months or annual memberships. Users will be able to book into classes and read blog pieces on healthy lifestyles.

### User stories
- As a first time user, I want to be able to easily navigate across the site so I can find the content quickly
- As a first time user, I want to know the purpose of the site immediately upon arrival
- As a first time user, I want to be able to find information about the membership options available at the gym
- As a user I want the site to be responsive across all devices
- As I user I want to be able to easily create an account
- As a user I want to be able to select a membership appropriate for my life
- As a user I want to be able to pay for the membership option securely
- 

### The Scope Plane
#### Features
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