# Ironworks Personal Trainer Booking System

**Portfolio Project 3 - Python Essentials**

## Project Overview

![Main Mockup](https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/mockup/mockup.png)

[Link to live site](https://ironworks-booking.herokuapp.com/)

---

# Table of Contents

- [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#user-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
- [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
    - [Data Models](#data-models)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credit](#credit)
- [Acknowledgements](#acknowledgements)
# Project Goals

## User Stories

### First Time Visitor

1. As a **First Time Visitor** I want to be able to book a personal training session.
2. As a **First Time Visitor** I want to be able to choose the trainer I want to book with.
3. As a **First Time Visitor** I want to get feedback from the site through the process.

### Returning Visitor

4. As a **Returning Visitor** I want to be able to view the sessions I have booked.
5. As a **Returning Visitor** I want to be able to cancel a booked session.

## Staff Member

6. As a **Staff Member** I want to be able to see who has booked for what sessions.
7. As a **Staff Member** I want to be able to add additional sessions for people to book.
8. As a **Staff Member** I would user to only be able book on certain dates.

## Site Owner Goals

9. As a **Site Owner** I want users to be able to login to the system and book sessions.
10. As a **Site Owner** I want to be able to validate all of the user input and provide feedback if input is invalid.
11. As a **Site Owner** I would like users to be able to get back to the welcome screen at any point through the process.

# Technical Design

## Flowchart
The flowchart for this site was created in Lucid Charts and can be seen below.
1. <details><summary>Flowchart</summary><img src="https://github.com/charliewatson1504/CI_PP3_Ironworks/blob/main/docs/flowchart/ironworks-flowchart.png"></details>

## Data models
I have used various data models within this project. Dictionaries have been used to pair up the dates with the users who have booked. Lists have also been used throughout the site.

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

# Features
This site has ?? pages with ?? features
## Feature 1 - Home Page
The homepage has ?? main sections to it:

### Section 1 -

![Feature 1 Section 1](#)

### User Stories covered by this feature
3- As a First Time Visitor

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
### 1. As a First Time Visitor

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 

<details><summary>Screenshot to show user story test</summary><img src="#"></details>

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