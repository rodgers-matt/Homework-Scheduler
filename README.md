# Homework-Scheduler
An application that uses Kivy and the Google Calendar API to schedule assignments to your Google Calendar. 
## Requirements
* This program requires you to create a creditials.json file. Simply go to https://developers.google.com/calendar/quickstart/python and enable the Google Calendar API in step 1. This will give you a creditals.json file that will need to be placed in the same directory as the main.py file.
* This program requires Kivy. More information about installation can be found at https://kivy.org.
* The hws.kv file is required to be in the same directory as the main.py file.

## How to use
* When you first run the program, you are greeted by the welcome screen. Click anywhere in this screen to proceed.

![Welcome](Welcome.PNG?raw=true)

* The next screen is the submit screen. Here, you will input the information about your assignment.
* First, input your assignment name into the Assignment text box.
* Next, input the class name into the Class Name text box.
* Finally, input the date that this assignment is due in the Due Date section.
* Once you hit Submit, the assignment is then added into your Google Calendar. 

![Submit](Submit.PNG?raw=true)
