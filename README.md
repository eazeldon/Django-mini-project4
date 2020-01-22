# Django-milestone project 4
Student at Code Institue 
https://mini-project-design.herokuapp.com/

## Concept
This website aims to provide a designer with a platform to interact with existing and potential customers to showcase his/her ideas/designs, discuss the design with customers (existing and potential), sell designs as well as receive requests for contact from potential customers for custom designs to initiate a discussion on custom jobs. One key element is to register users to allow the designer to have contact details for customers and potential customers.
Website title: Design
Why Design? It is to avoid any confusion on the content of the site. The site is all about the designer’s designs and interaction with customers about his/her designs, to get requests for work, feedback on existing designs and sell designs. It is all about designs!

## Design / UX Design

### Summary
The typical visitor is using a mobile phone to visit the site. The main reason the visitor is using their mobile phone is for convenience. It is expected that the modern mobile phone is the best tool while on the go to have access to designs and the desktop/laptop while reviewing designs at the office/home. It is envisioned that the typical user will need to review designs or request customer designs while on the go, e.g. working on an interior design, and quickly need to see a design at a location and maybe hold it up against a wall or similar. That is not made easily with a laptop, why mobile phone screen viewing is given top priority.

## User stories
•	As the site owner, I want to display my designs so that a registered site visitor can buy them.
•	As the site owner, I want to display my designs so that a registered site visitor can give me comments/feedback on them.
•	As the site owner, I want the site visitors to know how to contact me regarding custom designs so that I can discuss and sell custom design work via a direct dialogue to ensure I have all needed information and fully understand the site visitors need.

•	As a site owner, I want the visitors to register so that I have contact details of existing and potential customers, e.g. to inform them when new designs are available, if I have a campaign, etc.
•	As a site visitor, I want to register so that I can buy available designs.
•	As a site visitor, I want to register so that I can leave comments/feedback on available designs.

•	As a site visitor, I want to register so that I can get news and updates from the site owner.
•	As a site visitor, I want to know how to contact the site owner so that I can initiate a discussion on custom designs.
•	As a site visitor, I want to be able to search for designs if I have the design name so that I can comment/give feedback on them.

•	As a site visitor, I want to be able to search for other designs if I have the design name so that I can place orders for them.
•	As a site visitor, I want to be able to search for other designs if I have the design name so that I can get the pricing for them.

## Design
The website is designed with the intent to give the best possible viewing experience on mobile phone screens, followed by laptop/desktop and the lowest priority being tablet viewing. The reason for this priority is that people to a growing extent use their mobile phones as the premiere viewing medium for sites especially to do quick research and also to have easy and usable access when they need to review available designs or request a custom design. The reason tablet is given lowest priority is that the expected customer would either work on e.g. interior designs on a desktop/laptop or use the phone on the go. The website design is intended to be straight forward, simple to navigate and understand, without any confusing elements that can distract the visitor from achieving his/her objective with visiting the site.

## Wireframe
I used Balsamiq to design my wireframe. I used iPhone 11, iPad, and MacBook pro views to give myself an idea of what I wanted to achieve in terms of what the site visitors will see and how it should be displayed. I’m aware of that when implementing it will not be perfect on all screens and operating systems but rather it will be a compromise. As I’m using Mac and don’t have a PC the main verification, as you will be able to read under testing, has been on iOS, Mac OS for desktop using both Safari and Google Chrome browsers. My priority is iPhone as top priority, followed by desktop/laptop and finally tablet experience. The reasoning for that priority is given in the design explanation above. 

## Header background Image and other images
All images on the site are my own designs. This is to support the fact that the site is all about the site owner’s own designs and the showcasing of them. Images are intended to be shown in a manner that they attract the visitors’ attention and review without any distraction. The intention is to ensure that whatever time the visitor spends on the site is spent on achieving the site owner’s main purpose of the site.

## Menu bar - top of page
Is in place to give easy access to the main pages of the site.
The logout option only emerges then the visitor is logged in to the site and is not a page.

## Comments page
The page is created to allow the visitor to quickly gain access to the interface for leaving comments. The visitor can give the comment a title separate from the actual comment content. The comment page also allows the visitor to upload an image, assign a tag and the date of the comments is entered. The fields are there to help the visitor to structure their comments.

## Home page
Intent is to immediately bring the visitors focus on the designs available for immediate purchase, be informed of the price and make it easy to add any desired quantity to the cart. In addition, the visitor should easily understand how to initiate contact if they would like to discuss ordering a custom design and the page should also enable the visitor to search for other designs should they have the name of that design from a previous visit. 

## Login page
Created to allow the visitor to easily find the log-in section and without any distractions enter the log-in credentials.
Register page
Designed to enable the visitor to quickly register on the site by providing the contact e-mail and assign a password. This will then enable to visitor to sign-in to buy designs, leave comments and get news as the site owner will have the contact e-mail of the visitor.

## Product page
The intent of the page is to give the visitor an immediate and clear view of what existing designs they can order online right 
now, and at what price. Moreover, it should give the visitor the ability to add what and the quantity they want to buy to the cart.

## Cart page
This page will show what items the visitor has added to the cart and the quantity added and the price. It further allows the visitor to finalize the order by checking out through entering the payment details and submitting the payment.

## Logout
This is not a page. The option only emerges in the menu bar once the visitor is logged in. Clicking it will sign the visitor out.

## Colours
Colours were selected with the intent of not distracting from the display of the designs on display.


## Testing
Testing has been made in Cloud 9, Inspect mode. In addition, it has been live tested on MacBook Pro 15” screen, with MacOS ver. 10.14.6 and browsers Google Chrome and Safari, iPad mini4 with iOS ver. 12.4 using the Safari browser, iPhone 7 plus with iOS 13.3, iPhone 11 with iOS 13.3. The live testing was done by visiting the deployed site on the devices mentioned but also using the following online validators: 

•	http://browsershots.org/ 
o	To get multiple browser view tests

•	https://jigsaw.w3.org/
o	For CSS validation

•	https://www.freeformatter.com/
o	For html validation

Testing result revealed that the site is not perfect on all screens but that was expected. The site layout was designed with the intent to be as good as possible on iPhone as top priority, followed by desktop viewing and tablet screens as the lowest priority. The reasoning for the priority is given in the design section.

### Errors left unaddressed
When using an html validator the following issues were identified, but since I could not identify any errors on my site as a result of them, they were left unaddressed

•	The character encoding was not declared. Proceeding using “windows-1252”.

•	Non-space characters found without seeing a doctype first. Expected e.g. “<!DOCTYPE html>”.

•	Element “head” is missing a required instance of child element “title”.

When using a CSS validator two errors were found. The description was identical why it is only listed once in this document. The errors were left unaddressed since I could not identify and issues on the site as a result of them.

•	.navbar-default .navbar-brand:hover, .navbar-default .navbar-brand:focus  //  Value Error : background-color none is not a background-color value : none

## Acknowledgements
The code was inspired by instructions and examples provided by Code Institute in the module named “Full Stack Frameworks with Django!”. Examples used as inspiration are taking from the module subsections named “Blog all about it” and “Putting It All Together | ECommerce Mini Project”. 

## Technologies used
The technologies used to build this project were: html, CSS, JavaScript, Python, jQuery, Ginger.

## Deployment

### These are the steps taken to deploy the site:

1.	Sign-in to GitHub
2.	Click the green button stating “New” to create a new project
3.	Go to repository name
4.	Enter the website name you want for your project
5.	Select go to description
6.	Enter a description of the project, e.g. a short name describing the project
7.	Click public menu
8.	Click the green button stating “create repository”
9.	Select “Quick set-up” once it is visible
10.	Go to the ”… or push an existing repository” section
11.	Copy the keys displayed
a.	You will need them when you are ready to push your code to GitHub from cloud9
12.	Sign in to Heroku
13.	Create your project name

   a.	Select your name for the app

   b.	Select the region

   c.	Click create app

14.	Select “Resources” menu
15.	In add-ons type “postgres”
16.	Choose the free option
17.	Go to settings
18.	Click “reveal config Vars”
19.	Copy the key as you need it in your code
20.	Return to Cloud9
21.	Install your database in Cloud9
22.	You also need to install “psycopg2” for your database to work
23.	Go to settings py
24.	Import database dj url
25.	Enter the database code needed
26.	Go to env.py to set the key you got from Heroku
27.	Do the migration and create a super user
28.	Rebuild all your products through admin
29.	You need to create an AWS s3 bucket which you need for your e-commerce media file hosting
30.	Sign in to AWS
31.	Go to dashboard
32.	Select s3
33.	Create bucket to host your cloud server
34.	Give you bucket a unique name
35.	Choose the region you’re in
36.	Click next and next on the page afterwards
37.	Then unselect all the “block” ticks and click create bucket
38.	Open the bucket you created
39.	Go to properties
40.	Select static website hosting
41.	Enter needed index and error information and save
42.	Go to permissions
43.	Do the CORS configuration
44.	Go to bucket policy and enter the needed code
45.	Go to IAM and create your app name, group, user and policy
46.	The username is important because it will give you the key to access the bucket through cloud9, Heroku and GitHub. Download the .csv file
47.	Test your bucket
48.	Set-up you Travis CI & connect it to GitHub (I was instructed by my mentor that this step is optional)
49.	Go to your account
50.	Select your project – click to the switch next to your project name
51.	On build, click unknown and select markdown in the pop-up
52.	Create the travis.yml file in your Cloud9
53.	Enter the needed information in the travis file
54.	After you’ve completed everything in Cloud9 push to GitHub to host your code

   a.	Step 1: I use the command: git init 

   b.	Step 2: I used the command: git status

   c.	Step 3: I used the command: git add . 

   d.	Step 4: I used the command: git commit -m”added changes”

   e.	I had some errors and used Sometimes the push didn’t work in GitHub so I used:

   •	Git merge –-abort

   •	Git push --force
   and thereafter it worked.

55.	Use the key you got from ”… or push an existing repository” in GitHub
56.	Sign-in to GitHub and check that your code is there
57.	Sign-in to Heroku
58.	Go to settings
59.	Go to “config Vars” and set all your needed keys
60.	Once you’re done, connect your GitHub to Heroku inside your Heroku
61.	Go to “deploy” in Heroku
62.	Click the view log
63.	Check for errors

   a.	In deploying to Heroku I had an error in my view log. It stated I’m missing some code in the requirement.txt. I have edited and replaced the file to successfully address the issue.

64.	Once there are no errors there is a green “view” button meaning you have successfully completed the deployment to Heroku
65.	Deployment completed.

Please note that to deploy to Heroku I used a Procfile and a requirements.txt file.













  


















