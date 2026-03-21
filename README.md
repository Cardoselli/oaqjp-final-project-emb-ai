# Final Project: AI-Based Web Application Development and Deployment

**Estimated Time:** 1 hour 45 minutes

## Scenario
You have been hired as a software engineer by an e-commerce company to create an AI-based web app that performs analytics on customer feedback for their signature products. To accomplish this requirement, you will create an Emotion Detection system that processes feedback provided by the customer in text format and deciphers the associated emotion expressed.

## Introduction
In this final project, you will be assessed on the knowledge gained on all aspects of app creation and its web deployment throughout this course. You will be required to save screenshots of your results from time to time, with specific nomenclature. These screenshots will have to be uploaded in the peer graded assignment that follows.

In this project, we use the embeddable Watson AI libraries to create an emotion detection application. Emotion detection extends the concept of sentiment analysis by extracting the finer emotions, like joy, sadness, anger, and so on, from statements rather than the simple polarity that sentiment analysis provides. This makes emotion detection a very important branch of study and businesses use such systems widely for their AI based recommendation systems, automated chat bots, and so on.

## Prerequisite
Before you begin this project, make sure you have an active GitHub account. You'll be using GitHub to create and manage the repository for this lab.

## Project Guidelines
For the completion of this project, you'll have to complete the following 8 tasks:
* **Task 1**: Fork and Clone the project repository
* **Task 2**: Create an emotion detection application using Watson NLP library
* **Task 3**: Format the output of the application
* **Task 4**: Package the application
* **Task 5**: Run Unit tests on your application
* **Task 6**: Deploy as web application using Flask
* **Task 7**: Incorporate Error handling
* **Task 8**: Run static code analysis

---


## Packages 
To run this application, you need to install the following Python packages:

```bash
pip3 install flask requests pylint
```
---
## Project Structure
```bash
final_project/
│
├── EmotionDetection/           # Core logic package
│   ├── __init__.py             # Makes the directory a Python package
│   └── emotion_detection.py    # Watson API interaction & formatting
│
├── static/                     # Web assets
│   └── mywebscript.js          # Client-side logic for the interface
│
├── templates/                  # HTML templates
│   └── index.html              # Main user interface 
│
├── server.py                   # Main Flask server 
├── test_emotion_detection.py   # Unit testing script
└── README.md                   # Project documentation
