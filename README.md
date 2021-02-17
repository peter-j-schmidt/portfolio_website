# Portfolio Website
## Video Demo:  <URL HERE>
### Description:

### For my final project for CS50, I have created a personal portfolio website to display my education, programming abilities, and other work. The website was built using HTML, CSS/SCSS, Flask, and Bootstrap. The web app is deployed to Heroku and connected to Github Pages.

#### I used Flask to create a simple, one-page backend framework. This framework is based on the distribution code from CS50's Finance problem. The app has a route for each page on the site - the Homepage, Education, Projects, and Other Works pages.
#### Bootstrap 5 was used for the contruction of the front end, as well as basic HTML and CSS. I created the Hero Image on the Homepage based on code tutorials from Geeks for Geeks and W3Schools tutorials.
#### The website is fully responsive. Bootstrap has responsive design built in to its components and utilities, and only a simple media query was needed to make the Hero Image responsive.

#### The Homepage has the aforementioned Hero Image, with my name and my title positioned evenly across the page. The Hero Image is created using CSS's background element, and has a slight linear gradient applied to it. When the viewport shrinks (for resizing or loading onto a mobile device), a different background image is displayed.
#### The Hero Image is centered and stretches the entire height and width of the viewport. The name and title are made with Bootstrap's responsive grid layout and text sizing classes.
#### Below the hero image is a small About section with short biography of myself and what I am currently doing. Included in the section are links to a few social media sites (Github, LinkedIn, Youtube), as well as my personal email, should a visitor wish to contact me.
#### After the About section are a series of sections with links to other pages. Each section is made using Bootstrap's grid system, culminating in a row for the link to each page, separated by an "hr" tag. The row containes a themed image related to the page it links to, as well as a short description of that said page.

#### All of the other pages after the homepage are rendered with their own Flask route. Each page is rendered from a template that uses Jinja to extend a "layout.html" file. The layout file contains the basic HTML structure for each page, the links to Bootstrap's CSS, Javascript, and JQuery files, and a link to a Google Fonts file.
#### The layout file also contains a responsive Bootstrap navbar. The navbar contains links to each page rendered by the Flask app, as well as my personal email and links to the social media sites listed in the About section.

#### The Education page contains a series of cards for all of the computer science courses that I am taking or have completed. Each card has a link to a certificate earned and a Final Project, if available. Since I am not a traditional student (not currently pursuing a degree in Computer Science), this is meant to show initiative and dedication to the discipline, as well as a list of accomplishments.

#### The Projects page is a curation of completed projects, with links to relavent URLs and repositories. It is formated in a similar manner to the links presented on the Homepage.

#### The Other Works page is a collection of non-tech related work that I've done. Specifically, this contains a link to an aviation-related YouTube channel that I've started (Aviation is a great passion of mine).

#### I chose to use a Flask app for the backend of this website so that it can be scaled up in the future to include things such as a blog, a database that collects visitor information, and other similar features.
#### With a simple Flask web app, small changes can be developed quickly.



#### This is my first complete project, made independently and without much guidance. In order to implement my vision for the site, I had to learn new things that were not taught in CS50, such as how to implement different Bootstrap components, how to create a Hero Image, and how to import and utilize different fonts.
#### I thoroughly enjoyed this course and completing this project, and I am excited to continue my journey as a software developer and computer scientist.
