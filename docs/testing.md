# **WoW AH Averages - Testing**
![Picture of Home page](/assets/images/preview-image.png)
 
[Everyday Legends on Heroku.](https://everyday-legends.herokuapp.com)

 
## **Contents**
 
* [Back to README](../README.md)
* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)

Testing was a regular occurrence during the development of this project.
 
## **Automated Testing**
 
I used a PEP8 program developed by Code Institute to test my python code for errors. A lot of errors were thrown up originally.

![PEP8 results]
 
***
## **Manual Testing**
 
A full spelling and grammar check of the code + documents was completed by copying the code into Google Docs.
 
### **Full Testing**
 
Full testing was performed on my Windows 10 PC's OperaGX browser. Some other testing was performed on Google chrome and Mozilla Firefox on my Windows 11 laptop, and my google chrome browser on my Android phone. 
 
#### **Validation**
I made sure that:
* All links worked (opening in a seperate tab where needed).
* All renders and redirects worked correctly.
* Messages diplayed when needed and displayed correctly.
* Nav bar showed correct links depending on the type of user.
* Main user posts had full CRUD functionality.
* Logged in users can like or comment on posts.
* Login, Logout and registration features all work.
* Contact us form works correctly. Verified that an email has been recieved.
* Page is resposive towards the screen size.
 
## **Bugs**
 
### **Solved Bugs**
 
* Option to logout was showing as login when already signed in. Added an if statment to the base.html navbar to see if user was authenticaed.
* Champion list link on the navbar was showing regardless of login/user status. Added an if statement to the base.html to see if the user is staff.
* MIME error appearing on deployed Heroku app, meaning my CSS stylesheet was not being loaded. Installed django-heroku and redeployed the app on Herouku.
* Everyday Legends title in the nav bar link not working. Added correct href.
* Making a new post (both successful and unsuccseful) rendered the next page incorrectly. Made invalid form recreate the form and a valid form now redirects to "index" which is the same as the home page.
* The pagination button was causeing some whitespace on smaller screen sizes between the button and the footer. Fixed by overriding the margin size of the css class.
* Submit button in create post was hiding behind the footer. Added a 30 pixel boarder at the bottom of the main-content to ensure the footer is pushed below the content.
* Liking a post was throwing up an error for incorrect attribute "user-post". Corrected to "user_post".
* Button on contact us page not applying post-btn2 css class. Reduced specificity of class as it's not required.

 
### **Known Bugs**
 
No other known bugs have been found upon my testing.