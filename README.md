# **Everyday Legends**
 
Everyday legends is a platform in which players of the game 'League of Legends' can post, like and comment about certain matchups or guides on a specific champion.
 
![Image from amiresponsive](/assets/images/amiresponsive.png)
 
Image from [Am I Responsive?](https://ui.dev/amiresponsive)
 
[Everyday Legends live on Heroku](https://everyday-legends.herokuapp.com)
 
## **CONTENTS**
 
* [User Experience (UX)](#user-experience-ux)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment)
* [Testing](#testing) - [External document here](/docs/testing.md)
* [Credits](#credits)
 
***
## **User Experience (UX)**
 
### Initial Discussion
 
League of Legends is a hugely popular online PC game developed by Riot Games, with millions of players playing every week. There are many different online reasources for the game. However most of these reasources use statistics pulled from the Riot Games API so there isn't a lot of room for player opinion.

The purpose of this website it to provide a place where people can post their own tips and guides for specific champions, either in specific matchups or generally for a specified role. These posts will also be able to be liked by users to show that they found it particulary useful for themselves.

### **User Stories**
 
#### Client Goals
 
* As a user I should be able to register for an account and login.
* As a user I should be able to view created posts.
* As an admin I should be able to create an entry for a new champion that a user than then select when creating a new post.
* As a registered user I should be able to create a post containing my guide/tips for a specific champion in a role.
* As a registered user I should be able to like posts.
* As a user I can contact the site owners to provide feedback or suggestions
 
#### First Time Visitor Goals
 
* I should be allowed to view posts that have been created by registered users.
* I should be able to register for an account on the site.
* I should be able to contact the site owners to provide feedback or suggestions
 
#### Returning Visitor Goals
 
* I should be allowed to view posts created by registered users.
* I should be able to login (Or register if I have not done so at this point) to my account.
* I should be able to create a post (if logged in).
* I should be able to like a post (if logged in).
 
***
## **Design**
 
### **Colour Scheme**
 
![My original chosen colour scheme](/assets/images/colour_scheme.png)

The colour scheme I have chosen is based off of the league of legends logo's gold and a very dark blue to provide a suitable contrast. This scheme is commonly used within various league of legends media so it will match the feel provided by Riot games.
 

 
### **Typography**
 
[Google fonts](https://fonts.google.com) was used for the following fonts:
* Cinzel - Used for the site logo and in the headings.
* Rubik - Used as the default font across all content within the site.
 
[Font Awesome](https://fontawesome.com) was used for the Github and Linkedin logos in the footer.
 
### **Imagery**
 
[Cloudinary]() was used as an external image hosting site, which is required due to the ephemeral system used with Heroku apps, which would cause all images to be lost if the app has to be rebuilt for any reason.
 
### **Wireframes**
 
Wireframes created using Balsamiq.
 
 #### **Home page**
![Wireframe for Home page](/assets/images/home.png)
![Wireframe for Desktop Home page](/assets/images/home-alt.png)

 #### **Champion List page**
![Wireframe for Champion List page](/assets/images/champion-list.png)
![Wireframe for Desktop Champion List page](/assets/images/champion-alt.png)

 #### **Login/registration page**
![Wireframe for Login page](/assets/images/login.png)
![Wireframe for Register page](/assets/images/register.png)

 #### **Contacts Us page**
![Wireframe for Contact Us page](/assets/images/contact-us.png)

 #### **Champion Details page**
![Wireframe for Champion Details page](/assets/images/details.png)
![Wireframe for Desktop Champion Details page](/assets/images/details-alt.png)

### **Database Design**

As the project features will require the use of databases, I have provided a diagram, and an example of the database that will be setup, for the site below.

#### **Champion database**
![Champion database diagram](/assets/images/champion_diag.png)
![Champion database example](/assets/images/champion_example.png)

#### **Post database**
![Post database diagram](/assets/images/post_diag.png)
![Post database example](/assets/images/post_example.png)
 
### **Features**
 
### **Future Implementations**
 
* Password reset and email confirmation for account registration.
 
### **Accessibility**
 
While coding this site I have been mindful to ensure that the website is accessible and friendly. I have achieved this by:
  * Using descriptive alt attributes on all images used.
  * Making sure that there is sufficient colour contrast throughout the entire site.
  * Use semantic HTML where possible.
***
## **Technologies Used**
 
### **Languages used**
HTML, CSS, Javascript, Python, Markdown
 
### **Frameworks, Libraries & Programs Used**
 
* [Balsamiq](https://balsamiq.com) - Used to create wireframes.
* [Bootstrap V5.2](https://getbootstrap.com/docs/5.2/getting-started/download/) - Used to help style the website
* [Django v3.2](https://www.djangoproject.com) - Used to help take a lot of the work out of a lot of things such as creating functions required for making my database models.
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Used for making an authentication system on the website.
* [POSTGRESQL](https://www.postgresql.org) - An open sourced database management system used in this project.
* [Git](https://git-scm.com) - For version control.
* [Github](https://github.com) - To save and store all the files of the site.
* [CodeAnywhere](https://codeanywhere.com/?ref=marcomartins11) - The IDE used for all of the coding. Also used to write the README.
* [EmailJS](https://www.emailjs.com) - Used to help send the Contact Us form data to the site admin
* [Google Fonts](https://fonts.google.com) - To import the fonts used on the site.
* [Font Awesome](https://fontawesome.com) - For the down arrows used.
* [OperaGX](https://www.opera.com/gx) - Dev Tools to troubleshoot and test features, solve issues with responsiveness and styling.
* [Am I Responsive?](https://ui.dev/amiresponsive) - To show the website image on a variety of devices.
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) - Chrome DevTool extension that I use on my OperaGX browser.
* [Ico Converter](https://www.icoconverter.com) - Used to create my favicon from an image.
***
## **Deployment & Local Development**
 
### **Deployment**
The site is deployed using Heroku. Visit the deployed site [here.](https://everyday-legends.herokuapp.com)
 
To do this I:
1. Logged into [Heroku](https://www.heroku.com)
2. This leads to the dashboard. I then clicked on "New" on the right hand side and clicked "Create New App".
3. I set my app name to 'wow-ah-averages' and the region to Europe. Then I clicked "Create App"
4. On the app page. I clicked onto the "Settings" tab, then "reveal config vars".
5. I added 2 config Vars. First was called "CREDS" with the value being copied directly from my entire CREDS.json file. Second was called "PORT" with the value of "8000" to ensure deployment would work correctly.
6. I then clicked "Add Buildpack" and added Python, saving the changes after. I then clicked it again and added nodejs, saving changes again.
7. I then clicked onto the "Deploy" tab.
8. On the "Deployment Method" section, I clicked to connect to github and searched for the "wow-ah-averages" repository and connected it.
9. Further down the page, I enabled automatic deployments so that Heroku would rebuild and deploy the app whenever changes are pushed to the github repository. There is an option below to manually build the app if that is preferred.
 
### **Local Development**
 
#### How to Fork the repository
 
1. Log in (or sign up) to Github.
2. Go to the repository for this project, [everyday-legends](https://github.com/Welshy92/everday-legends).
3. Click the Fork button in the top right corner.
 
#### How to Clone the repository
 
1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [everyday-legends](https://github.com/Welshy92/everday-legends).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
***
## **Testing**
Click [here](/docs/testing.md) to view details on testing and bugs
***
## **Credits**
***
This website is a solo project created by [myself.](https://github.com/Welshy92)
 
### **Learning Resources**
 
There are a few different sites that I used to learn the required skills to develop this website.
* [Code Institute](https://codeinstitute.net) - Used the LMS to learn about Agile development, Bootstrap, Testing, Django and more.
* Code Institute Slack - Used to get answers for specific queries.
* [w3Schools](https://www.w3schools.com) - Used to double check some syntax for both CSS and Javascript.
* [Stack Overflow](https://stackoverflow.com) - Used as my main search point after Slack to get the answers I needed.
 
### **Code Used**
 
I have not copied any code from any source during this project.
 
### **Media**
 
Footer icons modified using icons from:
 
* [LinkedIn](https://www.linkedin.com)
 
* [GitHub](https://github.com)
 
 
### **Acknowledgments**
 
