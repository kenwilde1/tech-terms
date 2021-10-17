# Milestone Project 3 - Tech Terms

---

## Table of Contents:

---

<h1 style="text-align: center;">Tech Terms</h1>

---

## What is Tech Terms?

Tech Terms is a CRUD application that allows users to contribute term definitions to a repository. All terms can then be searched, edited or deleted. When a user comes across a tech term they don't understand, they can search the acronym on Tech Terms and get a definition. Tech Terms also provides other resources to learn more about the term.

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

##### 3. Logo

##### Wireframes

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

[Back to Top](#table-of-contents)

## Features

#### Future Features:

[Back to Top](#table-of-contents)

## Testing

Testing can be viewed at [TESTING.md]()

[Back to Top](#table-of-contents)

## Deployment

[Back to Top](#table-of-contents)

## Acknowledgements:

[Back to Top](#table-of-contents)
