# Milestone Project 3 - Tech Terms

---

## Table of Contents:

- [What is Tech Terms?](#what-is-tech-terms?)
- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Objective](#objective)
    - [Font](#font)
    - [Colour Scheme](#colour-scheme)
    - [Favicon](#favicon)
    - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Tools Used](#tools-used)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

---

<h1 style="text-align: center;">Tech Terms</h1>

---

## What is Tech Terms?

Tech Terms is a CRUD application that allows users to contribute term definitions to a repository. All terms can then be searched, edited or deleted. When a user comes across a tech term they don't understand, they can search the acronym on Tech Terms and get a definition. Tech Terms also provides other resources to learn more about the term.

Live Deployment - [Tech Terms](https://tech-terms-1.herokuapp.com/)

(My take a couple seconds to load due to heroku saving server resources if site is idle)

[Back to top](#table-of-contents)

## User Experience:

#### User Stories:

- _As a User_, I want to be register an account and for that data to persist.
  <br>
- _As a User_, I want to be login with details I used to register.
  <br>
- _As a User_, I want to be search for tech terms and retreive their definitions.
  <br>
- _As a User_, I want to be able to create a definition for term.
  <br>
- _As a User_, I want to be able to view all my created term definitions.
  <br>
- _As a User_, I want to be able to edit my term's definition.
  <br>
- _As a User_, I want to be able to delete my term's definition.
  <br>
- _As a User_, I want to be able to logout and clear my session.

#### Design

##### Objective

The design objective was to follow a familiar and rigid UX experience. A User of any level of experience should be able to navigate the various pages with confidence. It follows a common navbar with explicit options. The options clearly explain where the User is about to navigate to / what action they are to perform. Due to the nature of it being a CRUD application, there are no complicated components or designs.

The design is also mobile-friendly. The navbar will shrink to a burger-style menu and the other components will take up more space, using Bulma's responsive properties.

##### Font

The chosen font was Arial, with its fallbacks being: Helvetica and sans-serif. These are tried and tested fonts that are supported by all browsers. They should also be installed on all User's Operating Systems. This keeps it simple and dependeble. It also eliminates the need to import any fonts which can take up small amounts of network resources when the User loads the page.

There is also an interesting [Stack Overflow Post](https://stackoverflow.com/questions/30630563/why-use-arial-helvetica-sans-serif-as-font-family-instead-of-just-sans-serif) that explains the ordering and priority of the above mentioned fonts.

##### Colour Scheme

Bulma was used as the CSS framework. Due to this, the main colour scheme followed Bulma's. The colours used:

- Primary: hsl(171, 100%, 41%)
- Secondary: hsl(0, 0%, 100%)
- Controls: hsl(141, 53%, 53%)
- Important: hsl(348, 100%, 61%)

##### Favicon

The following favicon was made using [formito](https://formito.com/tools/favicon).

<img src="./static/favicon/favicon.ico" alt="favicon">

##### Wireframes

The Wireframes were created for the following resolutions:

- Desktop (1920 x 1080)
- Tablet (768 x 1024)
- Mobile (360 x 720)

They were created using Figma. They can be viewed here [Wireframes.pdf](https://github.com/kenwilde1/tech-terms/blob/main/assets/wireframes/wireframes.pdf).

<a href="https://github.com/kenwilde1/tech-terms/tree/main/assets/wireframes/wireframes.pdf">

[Back to Top](#table-of-contents)

---

## Technologies Used

#### Languages

- HTML5
- Bulma & CSS3
- Flask & Python
- JavaScript

#### Tools Used

- [Youtube](https://youtube.com)
  - Youtube was the main resource for learning how to accomplish certain tasks in Flask e.g creating a secure Register / Login system.
- [Stack Overflow](https://stackoverflow.com/)
  - Used to help debug during development.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
  - Used for all debugging and testing. Ensured the page was responsive on all relevant devices.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
  - As per project specifications, MongoDB was used to store data for the application.
- [VSCode](https://code.visualstudio.com/)
  - VSCode was used as the development editor. I used some extensions to help:
    - Prettier - format the code on every save.
    - Markdown Preview Enhancement - write README.md and TESTING.md whilst having a preview tab that had live updates of my changes.
- [Github](https://github.com/)
  - Github was used for version control and issue management. I used a Kanban style board to effectively manage the features I was implementing.
- [Figma](https://www.figma.com/)
  - Used to create UI mockups for Tech Terms.

[Back to Top](#table-of-contents)

## Features

#### Register

The User can register an account with Tech Terms. They will provide a name, email and password. These details are stored on MongoDB.

#### Login

The User can use their registered details in order to login to their account. The flask models will check their details against a document in MongoDB. If the details are correct, a new session is created. An appropriate error is provided if any details are wrong.

#### Search Term

An input bar allows the user to search a term acronym e.g OS. A query will then be made to MongoDB, see if the term exists. If the term exists, the definition will be returned. Additionally, a hyperlink will be generated for this term that autofills a google search so the User can learn more about the term.

#### Browse Terms

There is a term table on the dashboard, with pagination. The user can browser through the table, viewing the terms that exist in the database. They don't have to search for a term. A query is made to MongoDB to return all term definitions.

#### Create Term

The User can click Create a Term in the nav bar. A modal will popup where they can create a new definition in the database. A query is made to MongoDB to see if this term already exists, if so, this error is returned. If the term does not exist, we create one.

#### View Terms

A User can view the terms they have created on a dedicated page. It will send a query to MongoDB and grab all documents that have the 'created_by' matching with the User's ID.

#### Edit Term

If the User would like to change the definition they provided for a term, they can edit it on the My Terms list.

#### Delete Term

If the User no longer wants to keep that term definition, they can delete it. We ensure that they are the correct owner of that term before sending the deletion query to MongoDB.

#### Logout

The User can log out and clear their session. This will bring them back to the Login page.

[Back to Top](#table-of-contents)

## Testing

Testing can be viewed at [TESTING.md](https://github.com/kenwilde1/tech-terms/blob/main/TESTING.md)

[Back to Top](#table-of-contents)

## Deployment

The site was deployed to Heroku. The following tutorial was used to deploy to Heroku - [RealPython](https://realpython.com/flask-by-example-part-1-project-setup/)

The taken steps to deployed were:

1. Create a requirements.txt

```
python3 -m pip3 freeze > requirements.txt
```

This tells Heroku which packages need to be installed.

2. Log CLI into Heroku

```
heroku login
```

3. Add Procfile

Create a Procfile that gives Heroku a command to execute in order to start the app.

```
web: gunicorn app:app
```

4. Create app on heroku

```
heroku create tech-terms-1
```

5. Push repo to heroku branch

```
git push heroku main
```

After pushing the local repository to heroku, it will build and use the Procfile to execute the flask app.

[Back to Top](#table-of-contents)

## Acknowledgements:

- Code Institute learning resources, especially setting up a MongoDB cluster on MongoDB Atlas.
- Youtube channels such as [Luke Peters](https://www.youtube.com/user/lukepetersphoto) and [Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg)
- Stack Overflow helped enormously when encountering Flask bugs. Tutorials often use a certain version of flask and python, so what may work on tutorials, may not work when developing yourself.

[Back to Top](#table-of-contents)
