# Ironworks Personal Trainer Booking System

**Portfolio Project 3 - Python Essentials**

## Project Overview

![Main Mockup](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/mockup/mockup.png)

[Link to live site](https://ironworks-booking.herokuapp.com/)

[Link to google sheet used for the data storage](https://docs.google.com/spreadsheets/d/1Y5uWBQ5PCS4LM2vL3NYcshhGn-3tMyMbel-V3aOZBSQ/edit?usp=sharing)

---

# Table of Contents

- [Project Goals](#project-goals)
    - [User Stories](#user-stories)
- [User Manual](#user-manual)
- [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
    - [Data Models](#data-models)
    - [User Interface](#user-interface)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credit](#credit)
- [Acknowledgements](#acknowledgements)
# Project Goals

To create a system for managing personal training session bookings from both a user perspective and
a staff member perspective. The experience needs to be simple and easy follow due to this being
run through command line only. Options need to be given to the user at all times so that they
don't feel stuck along the way.

## User Stories

### First Time Visitor

1. As a **First Time Visitor** I want to be able to book a personal training session.
2. As a **First Time Visitor** I want to be able to choose the trainer I want to book with.
3. As a **First Time Visitor** I want to get feedback from the site through the process.
4. As a **First Time Visitor** I want to be able to check my bmi score

### Returning Visitor

5. As a **Returning Visitor** I want to be able to view the sessions I have booked.
6. As a **Returning Visitor** I want to be able to book another session
7. As a **Returning Visitor** I want to be able to check my bmi score

### Staff Member

8. As a **Staff Member** I want to be able to see who has booked for what sessions.
9. As a **Staff Member** I want to be able to add additional sessions for people to book.
10. As a **Staff Member** I would like a user to only be able book on certain dates.

### Site Owner

11. As a **Site Owner** I want users to be able to login to the system and book sessions.
12. As a **Site Owner** I want to be able to validate all of the user input and provide feedback if input is invalid.
13. As a **Site Owner** I would like users to be able to get back to the welcome screen at any point through the process.
14. As a **Site Owner** I would like to get basic medical information from the user when they create
a new account

# User Manual

Ironworks Personal Trainer Booking System requries user input for the system to work. For this reason the
sytem has been built in a way that is easy for the user to navigate by providing the user with options at
each point. The system also takes in user input for passing through to the google sheet where data is stored or it uses it to workout a computation for the user and provides the answer back to them. By chaining the functions together the system can reuse inputs rather than asking the user for the same information again.

## 1. Welcome Screen

<details><summary>Screenshot of welcome screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-1.png"></details>

This is the first screen that the user sees when the application runs. For the user to move on their are 2 options:
- login - takes the user to login to their account if they have one. [Section 3](#3-login)
- create account - takes the user to create a new account if they don't have an account. [Section 2](#2-create-account)

## 2. Ceate Account

<details><summary>Screenshot of create account screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-2.png"></details>

At the create account screen you will be asked for the username you would like to register with. When you have entered your desired username the system will check to see if it is available. If its not available you should get an error message saying that and asking for you to try again. Once an available username is entered it will take you to complete a basic medical form. Following that you will be presented with 2 options:
- login - takes the user to their account. [Section 3](#3-login)
- exit - takes user back to welcome screen. [Section 1](#1-welcome-screen)

## 3. Login

<details><summary>Screenshot of login screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-3.png"></details>

Much like with the create account, the login page asks you to enter a username. Difference this time is it will check to see if it exists and allow you to move to the next screen. If you login with a user account then you will be presented with 3 options:
- book - takes you to the part of the system where you can book a session with one of the trainers. [Section 4](#4-book)
- booked sessions - takes you to view the sessions you have booked. [Section 5](#5-booked-sessions)
- BMI calculation - takes you to where with a input of weight and height from the user it can calculate their BMI. [Section 6](#6-bmi-calculation)

## 4. Book

<details><summary>Screenshot of book screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-4.png"></details>

When selected to go to book a session as a user you will first be shown a list of available dates for each trainer. The system then asks who you would like to book with. It checks to see if your selection is valid and if so it will then ask you for the date you would like to book. Date format to use is dd-mm-yyyy and if a valid date is entered it will confirm this back to you.

<details><summary>Screenshot of booking confirmation screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-5.png"></details>

Following that you are presented with 2 options:
- booked sessions - takes you to view the sessions you have booked. [Section 5](#5-booked-sessions)
- exit - takes user back to welcome screen. [Section 1](#1-welcome-screen)

## 5. Booked Sessions

<details><summary>Screenshot of booked screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-6.png"></details>

The booked sessions screen shows you the session dates that are booked with which trainer. At the end it gives you 2 options:
- book - takes you to the part of the system where you can book a session with one of the trainers. [Section 4](#4-book)
- exit - takes user back to welcome screen. [Section 1](#1-welcome-screen)

## 6. BMI calculation

<details><summary>Screenshot of BMI calculation screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-7.png"></details>

The BMI calculation allows you to enter your weight and height and it will return your score. Only the score is provided and no interpretation of what that score means is given. This is for calculation purposes only. Once done it will provide you with 2 options:
- booked sessions - takes you to view the sessions you have booked.
- book - takes you to the part of the system where you can book a session with one of the trainers. [Section 4](#4-book)
- exit - takes user back to welcome screen. [Section 1](#1-welcome-screen)

## 7. View staff session (Staff Account)

<details><summary>Screenshot of staff sessions screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-8.png"></details>

When you login with a staff account you can view booked sessions or add a new session. By selecting view booked sessions it will show you a list of the sessions you have made available and if any of the dates have been booked it will show the name of the person who has booked that session. At the end it gives you 2 options:
- add a new session - this allows a staff member to make a new date available for people to book. [Section 8](#)
- exit - takes user back to welcome screen. [Section 1](#1-welcome-screen)

## 8. Add a new session (Staff Account)

<details><summary>Screenshot of add a new session screen</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/user-manual/user-manual-9.png"></details>

The second option in a staff account is being able to make an additional date available. The system will ask you for the date that you would like to add. Once it has check that this date is not currently in use it will add it and users will be able to book that session. After that has completed you are given 2 options:
- view scheduled sessions - takes the user to view their sessions. [Section 7](#)
- exit - takes user back to welcome screen. [Section 1](#1-welcome-screen)

# Technical Design

## Flowchart
The flowchart for this site was created in Lucid Charts and can be seen below.
1. <details><summary>Flowchart</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/flowchart/ironworks-flowchart.png"></details>

## Data models
I have used various data models within this project. A Class has been used to for the BMI calc as it can take in attributes and use a method to do the calculation of BMI using those attributes. Dictionaries have been used to pair up the dates with the users who have booked. Lists have also been used throughout the site.

## User Interface

Due to the nature of this project in that the focus is on using the python there isn't much flexibility in making an aesthetically pleasing site. That being said I focused on making the system as easy to use as possible. This is done by giving simple options allowing easier interaction for the user. When more than a single option is needed I have tried to explain what exactly the user needs to enter and if a specific format is needed then show that.

# Technologies Used

## Languages
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks, libraries and other tools
- [Git](https://git-scm.com/)
Used for version control of the site and push code from VScode to Github
- [Github](https://github.com/)
Used as the remote repository to store the code. Github pages is also where the live site is hosted.
- [Gitpod](https://www.gitpod.io/)
Used as the IDE for writing the code and file management
- [Lucid Charts](https://www.lucidchart.com/)
Used to create flowchart for the site
- [Heroku](https://www.heroku.com)
Used to deploy the application.
- [Google Sheets](https://calendar.google.com/)
Users input data edits content on within Google Sheets
- [Google Cloud Platform](https://console.cloud.google.com/)
All data send and received using the Google API through the Google Cloud Platform

## Third Party Libraries
- google.oauth2.service_account:

Allows the application to access the google API without storing the usernames and passwords of the google accounts in the application files its self. A creds.json file is created with all details the API needs to access the google account. In deployment to heroku this information is store in the config var section.
- gspread:

Allows the application to access google sheets created by the site owner. Using various commands the app can open, select, create or delete worksheets. It can also get cell values, update cell values, append to whole rows, find data within a worksheet or get cell properties. This has allowed the app do everything it does as the data is stored in the google sheet and most all of the functions rely on access the worksheet.

# Features
This site has 3 features
## Feature 1 - Create account
Create account has 2 main sections to it:

1. Choose a username
2. PARQ form

### Section 1 - Choose a username

Allows a user to create an account if they don't have one. Input username is checked to see if it is available. If that passes then the username is appended to the users google worksheet and the app takes the user to the PARQ form.

![Feature 1 Section 1](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/features/feature-1-sec-1.png)

### Section 2 - PARQ form

PARQ form is to gather some basic medical information for the personal trainer before the user comes in for a session. The app asks the user for some inputs and then those inputs are stores within the parq google worksheet.

![Feature 1 Section 2](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/features/feature-1-sec-2.png)

### User Stories covered by this feature

3 As a **First Time Visitor** I want to get feedback from the site through the process.

12 As a **Site Owner** I want to be able to validate all of the user input and provide feedback if input is invalid.

14 As a **Site Owner** I would like to get basic medical information from the user when they create a new account

## Feature 2 - User account section
User account has 3 main sections to it:

1. Book a session
2. View booked sessions
3. Use BMI calculator

### Section 1 - Book a session

One of the largest functions in the app. It starts with showing the available sessions to book for each trainer. Then allows the user to select which trainer they want to book with. Finally the user enters which date they want to book which is checked to see if available and if so the users username is put against that trainer and date in the relevant trainer google worksheet.

![Feature 2 Section 1](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/features/feature-2-sec-1.png)

### Section 2 - View booked sessions

This displays a list of sessions the user has booked and who with.

![Feature 2 Section 2](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/features/feature-2-sec-2.png)

### Section 3 - Use BMI calculator

This section of the app asks the user for 2 inputs of weight and height. It then returns the BMI score based on those inputs.

![Feature 2 Section 3](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/features/feature-2-sec-3.png)

### User Stories covered by this feature

1 As a **First Time Visitor** I want to be able to book a personal training session.

2 As a **First Time Visitor** I want to be able to choose the trainer I want to book with.

3 As a **First Time Visitor** I want to get feedback from the site through the process.

4 As a **First Time Visitor** I want to be able to check my bmi score.

5 As a **Returning Visitor** I want to be able to view the sessions I have booked.

6 As a **Returning Visitor** I want to be able to book another session.

7 As a **Returning Visitor** I want to be able to check my bmi score.

11 As a **Site Owner** I want users to be able to login to the system and book sessions.

12 As a **Site Owner** I want to be able to validate all of the user input and provide feedback if input is invalid.

13 As a **Site Owner** I would like users to be able to get back to the welcome screen at any point through the process.

## Feature 3 - Staff account section
Staff account has 2 main sections to it:

1. View scheduled sessions
2. Add a new scheduled session

### Section 1 - View scheduled sessions

Displays the scheduled sessions for users with a staff account. It gets the data from the relevant google worksheet and shows the dates they currently have scheduled and either 'AVAILABLE' if not yet booked by a user or the users username.

![Feature 3 Section 1](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/features/feature-3-sec-1.png)

### Section 2 - Add a new scheduled session

A staff member in this section can schedule a new date for users to be able to book to. The app asks for a date and checks to see if the date isn't currently in use. If not it adds it to the relevant google sheet and makes it 'AVAILABLE' for users to book a session.

![Feature 3 Section 2](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/features/feature-3-sec-2.png)

### User Stories covered by this feature

8 As a **Staff Member** I want to be able to see who has booked for what sessions.

9 As a **Staff Member** I want to be able to add additional sessions for people to book.

10 As a **Staff Member** I would like a user to only be able book on certain dates.

12 As a **Site Owner** I want to be able to validate all of the user input and provide feedback if input is invalid.

13 As a **Site Owner** I would like users to be able to get back to the welcome screen at any point through the process.

# Validation
## Validation
[PEP8](http://pep8online.com/) and [Pylint](https://www.pylint.org/) have been used to validate all of the python code within the site. All files have passed with 0 errors. Click on the below to see each screenshot:
PEP8
1. <details><summary>run.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/PEP8/pep8-run.png"></details>
1. <details><summary>bmi.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/PEP8/pep8-bmi.png"></details>
1. <details><summary>google_sheet.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/PEP8/pep8-google-sheet.png"></details>
1. <details><summary>parq.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/PEP8/pep8-parq.png"></details>
Pylint
1. <details><summary>run.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/Pylint/pylint-run.png"></details>
1. <details><summary>bmi.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/Pylint/pylint-bmi.png"></details>
1. <details><summary>google_sheet.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/Pylint/pylint-google-sheet.png"></details>
1. <details><summary>parq.py</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/validation/Pylint/pylint-parq.png"></details>

# Testing of User Stories
### 1. As a First Time Visitor I want to be able to book a personal training session.

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|User section|At welcome screen enter c to create account. Enter a username. Complete parq form. Enter l to login. Enter username just created. Enter b to book a session. Enter k to book with Karen. Enter an available date with Karen.|App response of Great! "date" has been booked for you with Karen|Works as expected|
|2|User section|At welcome screen enter l to login. Enter username. Enter b to book a session. Enter s to book with Steve. Enter an available date with Steve.|App response of Great! "date" has been booked for you with Steve|Works as expected|


<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-1-1.png"></details>

<details><summary>Screenshot to show user story test 2</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-1-2.png"></details>
<br>

### 2. As a First Time Visitor I want to be able to choose the trainer I want to book with.

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|User section|At welcome screen enter c to create account. Enter a username. Complete parq form. Enter l to login. Enter username just created. Enter b to book a session. Enter k to book with Karen.|App response of Karen selected|Works as expected|
|2|User section|At welcome screen enter l to login. Enter username. Enter b to book a session. Enter s to book with Steve.|App response of Steve selected|Works as expected|


<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-2-1.png"></details>

<details><summary>Screenshot to show user story test 2</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-2-2.png"></details>
<br>

### 3. As a First Time Visitor I want to get feedback from the site through the process.

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|Login|At welcome screen enter l to login. Enter username fnergfjre.|App response of fnergfjre is not a valid username.|Works as expected|
|2|User section|At welcome screen enter l to login. Enter username. Enter b to book a session. Enter s to book with Steve. Enter an unavailable date with Steve.|App response of |Works as expected|

<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-3-1.png"></details>

<details><summary>Screenshot to show user story test 2</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-3-2.png"></details>
<br>

### 4. As a First Time Visitor I want to be able to check my bmi score.

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|Login|At welcome screen enter l to login. Enter username charlie. Enter c to go to BMI calc. Enter weight 100. Enter height 200.|App response of Your BMI score is 25.0|Works as expected|

<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-4.png"></details>
<br>

### 5. As a Returning Visitor I want to be able to view the sessions I have booked.

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|Login|At welcome screen enter l to login. Enter username charlie. Enter s to go to view booked sessions.|App displays booked sessions split by trainer|Works as expected|

<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-5.png"></details>
<br>

### 6. As a Returning Visitor I want to be able to book another session.

Follows the same test as user story 1

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|User section|At welcome screen enter l to login. Enter username. Enter b to book a session. Enter s to book with Steve. Enter an available date with Steve.|App response of Great! "date" has been booked for you with Steve|Works as expected|

<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-1-2.png"></details>
<br>

### 7. As a Returning Visitor I want to be able to check my bmi score.

Follows same test as user story 4

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|Login|At welcome screen enter l to login. Enter username charlie. Enter c to go to BMI calc. Enter weight 100. Enter height 200.|App response of Your BMI score is 25.0|Works as expected|

<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-4.png"></details>
<br>

### 8. As a Staff Member I want to be able to see who has booked for what sessions.

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|Login|At welcome screen enter l to login. Enter username karen. Enter s to view scheduled sessions|App displays scheduled sessions|Works as expected|

<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-8.png"></details>
<br>

### 9. As a Staff Member I want to be able to add additional sessions for people to book.

|Test|Feature|Action|Expected Result|Actual Result|
|---|---|---|---|---|
|1|Login|At welcome screen enter l to login. Enter username steve. Enter a to add a new scheduled session. Enter 10-11-2021|App response is Great! 10-11-2021 has been added to your schedule|Works as expected|

<details><summary>Screenshot to show user story test 1</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/testing/user-story-9.png"></details>

# Bugs
- Bug:
- Fix:

# Deployment

### Heroku

The steps I took to deploy to Heroku. If you want to do it yourself follow:

1. Create an account at [heroku.com](https://.heroku.com/)
2. Click on new and select create a new app.
3. Add a unique app name and select your region.
4. Click on create app.
5. Click on Settings.
6. Under Config Vars add your sensitive data (I used this for creds.json file) and set an additional to KEY: port VALUE: 8000.
7. I have set buildpacks to <Python> and <NodeJS>. Must be in that order.
8. Go to Deploy and at Deployment method click on Connect to Github.
9. Enter your repository name and click on it when it shows.
10. Choose the branch you want to buid your app from. I used main for this project.
11. I have used Enable Automatic Deploys which keeps the app up to date with your Github repository

### Google API

Steps I took to set up the google API. If you want to do it yourself follow:

1. You need a google account. Either Login or create a Google account.
2. Go to https://console.cloud.google.com/
3. Click on the New Project icon.
4. Add Project name and details.
5. Under API's and services enable Google Drive and Sheets. These are the ones I have used but there are
more so you can look through the lirbary.
6. Create a credential service account. Maybe different if you use different APIs.
7. Download the credential and upload it to your workspace in a JSON file.
8. Under API's and services enable Google Drive and Sheets (or ones that you are using).
9. Compelete the needed tasks to be performed in the documentation for the [Drive](https://developers.google.com/drive/?hl=en_GB) and [Sheets](https://developers.google.com/sheets?hl=en_GB) API.
10. Add them to your code.

# Credit

# Acknowledgements
- To Mo Shami, my mentor, for getting me through this with great advice and support
- To the Code Institute slack community for finding out great advice, guidance and resources.