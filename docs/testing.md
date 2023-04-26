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
 
Full testing was performed on my Windows PC's OperaGX browser. 
 
#### **Introduction**
I tested the program from start to
 
#### **Validation**
To make sure the errors displayed correctly on each data entry. I would enter the word 'cat' and then enter a 0, a -5 and a 1.5 entry to make sure that it wasn't possible to do an incorrect entry. I would then enter a positive integer above 0 to make sure it accepted the correct entry. Starting with Titansteel Bars.
 

 
## **Bugs**
 
### **Solved Bugs**
 
* Option to logout was showing as login when already signed in. Added an if statment to the base.html navbar to see if user was authenticaed.
* Champion list link on the navbar was showing regardless of login/user status. Added an if statement to the base.html to see if the user is staff.
* MIME error appearing on deployed Heroku app, meaning my CSS stylesheet was not being loaded. Installed django-heroku and redeployed the app on Herouku.
* Everyday Legends title in the nav bar link not working. Added correct href.
* Making a new post (both successful and unsuccseful) rendered the next page incorrectly. Made invalid form recreate the form and a valid form now redirects to "index" which is the same as the home page.

 
### **Known Bugs**
 
No other known bugs have been found upon my testing.