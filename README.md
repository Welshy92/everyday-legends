# **Everyday Legends**
 
Everyday legends is a platform in which players of the game 'League of Legends' can post, like and comment about certain matchups or guides on a specific champion within the game.
 
![Responsive View of home page](/assets/images/responsive.png)
 
 
[Everyday Legends live on render](https://everyday-legends.onrender.com)
 
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
 
League of Legends is a hugely popular online PC game developed by Riot Games, with millions of players playing every week. There are many different online resources for the game. However most of these resources use statistics pulled from the Riot Games API so there isn't a lot of room for player opinion.


The purpose of this website is to provide a place where people can post their own tips and guides for specific champions, either in specific matchups or generally for a specified role. These posts will also be able to get liked by users to show that they found it particularly useful for themselves, or give their comments to the posts.

I used some agile methodology while working on the project as seen on my github projects page [HERE](https://github.com/users/Welshy92/projects/5/).


### **User Stories**
 
#### Client Goals
 
* As a user I should be able to register for an account and login.
* As a user I should be able to view created posts.
* As an admin I should be able to create an entry for a new champion that a user can then select when creating a new post.
* As a registered user I should be able to create a post containing my guide/tips for a specific champion in a role.
* As a registered user I should be able to like posts.
* As a registered user I can comment on user posts.
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
* I should be able to comment on a possed (if logged in)
 
***
## **Design**
 
### **Colour Scheme**
 
![My original chosen colour scheme](/assets/images/colour_scheme.png)


The colour scheme I have chosen is based off of the league of legends logo's gold and a very dark blue to provide a suitable contrast. I have brightened the gold a bit to provide a better contrast for the visually impaired. This scheme is commonly used within various league of legends media so it will match the feel provided by Riot games.
 


 
### **Typography**
 
[Google fonts](https://fonts.google.com) was used for the following fonts:
* Cinzel - Used for the site logo and in the headings.
* Rubik - Used as the default font across all content within the site.
 
[Font Awesome](https://fontawesome.com) was used for the Github and Linkedin logos in the footer.
 
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
 I had originally had a much bigger scope for the site but felt this was not required for the MVP. However this may be implemented in the future.


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
 
As I originally had a much larger scope for this project, there are a bunch of features that I deemed not required for the project to be functional to users;


* Password reset and email confirmation for account registration.
* A champion list page that displays basic information about the champion such as ability rundown and basic lore.
* Use the Riot API to add champion win rate on the current page to the above mentioned champion page.
* Add full CRUD functionality to the champion list page instead of getting them to do it through the admin panel.
* Ability for users to edit and delete their comments.
* Ability for users to save their posts as drafts and come back to them later.
* Ability for staff/admins to view and approve new comments without having to use the admin panel.
* The ability for staff/admins to upload champion portraits that could be displayed on the post list or slash arts for the actual posts themselves.
* The ability to sort the post list out. Ascending or descending post date, number of likes or the ability to filter by champion/position.
* Add confirmation requirements for editing and deleting posts.
* Position icons displaying on the post list, post, and champion list pages.
 
### **Accessibility**
 
While coding this site I have been mindful to ensure that the website is accessible and friendly. I have achieved this by:
  * Using descriptive alt tags where required.
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
* [Django CrispyForms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used to help quickly create forms on the new post page.
* [POSTGRESQL](https://www.postgresql.org) - An open sourced database management system used in this project.
* [ElephantSQL](https://www.elephantsql.com) - Used to quickly set up and maintain my POSTGRESQL databases.
* [Git](https://git-scm.com) - For version control.
* [Github](https://github.com) - To save and store all the files of the site.
* [CodeAnywhere](https://codeanywhere.com/?ref=marcomartins11) - The IDE used for all of the coding. Also used to write the README.
* [EmailJS](https://www.emailjs.com) - Used to help send the Contact Us form data to the site admin
* [Google Fonts](https://fonts.google.com) - To import the fonts used on the site.
* [Font Awesome](https://fontawesome.com) - For the down arrows used.
* [OperaGX](https://www.opera.com/gx) - Dev Tools to troubleshoot and test features, solve issues with responsiveness and styling.
* [Cloudinary](https://cloudinary.com) was used as an external static file hosting site, which is required due to the ephemeral system used with Heroku apps, which would cause all images to be lost if the app has to be rebuilt for any reason.
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) - Chrome DevTool extension that I use on my OperaGX browser.
***
## **Deployment & Local Development**
 
### **Deployment**
The site was orginally deployed using Heroku.
 
To do this I:
1. Logged into [Heroku](https://www.heroku.com)
2. This leads to the dashboard. I then clicked on "New" on the right hand side and clicked "Create New App".
3. I set my app name to 'everyday-legends' and the region to Europe. Then I clicked "Create App"
4. On the app page. I clicked onto the "Settings" tab, then "reveal config vars".
5. I added 5 config Vars. These were for the cloudinary URL + secret api key, the ElephantSQL database key, a port and a secret key
6. I then clicked onto the "Deploy" tab.
7. On the "Deployment Method" section, I clicked to connect to github and searched for the "everyday-legends" repository and connected it.
8. Further down the page, I enabled automatic deployments so that Heroku would rebuild and deploy the app whenever changes are pushed to the github repository. There is an option below to manually build the app if that is preferred.
 
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
* [Code Institute](https://codeinstitute.net) - Used the LMS to learn about Agile development, Bootstrap, Testing, Django and more. Also used their slack group to ask questions about various things.
* Code Institute Slack - Used to get answers for specific queries.
* [Stack Overflow](https://stackoverflow.com) - Used as my main search point after Slack to get the answers I needed.
* [Django](https://docs.djangoproject.com/en/3.2/) - Documentation used for various parts of Django and its libraries.
 
### **Code Used**
 
I have taken and edited some code for the basic templates to show my views on the home page. Code taken from https://github.com/Welshy92/i-think-blog/blob/main/templates/index.html
 
### **Acknowledgments**
 
* [Jo Heyndels](https://www.linkedin.com/in/joke-heyndels/) - Member of the Code Institute team that helped me with a few of my Django and CodeAnywhere enquiries/concerns.
* [Niel McEwen](https://www.linkedin.com/in/niel-mcewen-43b3a0/?originalSubdomain=ie) - Member of the Code Institute team that also helped me with some of the CodeAnywhere enquiries/concerns.
* [Kasia Bogucka](https://www.linkedin.com/in/kasbogucka/) - Member of the Code Institute team that has created some nice video content for both this project specifically and for CodeAnywhere.
* [Ian Meigh](https://www.linkedin.com/in/ianmeigh/) - Code Institute Alumni that helped me figure out what to do with my EditPost view.
* [Seán Murphy](https://www.linkedin.com/in/sean-murphy-dev/) - Code Institute tutor that helped me get my project deployed after builds were failing on Heroku at the final deployment stage.



