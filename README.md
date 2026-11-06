# MamaCover – Maternal Healthcare Coverage Tracker

## About the Project

MamaCover is a learning and innovation project aimed at helping pregnant mothers monitor their healthcare coverage and receive reminders about possible coverage interruptions.

The idea is to explore how software, APIs, mobile payments, and SMS notifications could help mothers prepare for healthcare expenses before reaching a health facility.

This is a prototype for learning, experimentation, and portfolio development. It is not a production healthcare service.

## Problem Statement

Some expectant mothers may discover that their health coverage is inactive or that their benefits are insufficient only when seeking medical care. MamaCover explores ways to make coverage information and reminders more accessible.

## Proposed Features

- Healthcare coverage status tracking.
- Reminders about possible coverage interruptions.
- SMS notifications.
- M-Pesa sandbox payment integration.
- A web interface for managing and viewing coverage information.
- USSD access as a future development goal.

## Technologies and Tools

- Python
- Flask
- Git and GitHub
- Postman
- Safaricom Daraja API sandbox
- ngrok for local webhook testing
- Africa's Talking for possible USSD and SMS integration
- Mock data and simulated API responses where live API access is unavailable

## Current Progress

- [x] Defined the project idea and problem statement.
- [x] Created a Flask webhook endpoint for callback testing.
- [x] Set up a Python virtual environment.
- [x] Installed Flask.
- [x] Set up ngrok to expose the local Flask server for testing.
- [x] Complete testing of the public callback endpoint.
- [x] Obtain and test a Daraja sandbox access token.
- [ ] Test an M-Pesa sandbox STK Push request.
- [ ] Receive and inspect payment callback data.
- [ ] Develop the coverage tracking backend.
- [ ] Add mock coverage records and status checks.
- [ ] Explore SMS and USSD integration.
- [ ] Build a simple user interface.
- [ ] Document testing results and lessons learned.

## Learning Objectives

Through this project, I aim to improve my skills in Python programming, backend development, API integration, data handling, software testing, and version control.

## Important Notes

The prototype will use simulated healthcare data unless authorized access to real services becomes available. No real patient information, passwords, API secrets, access tokens, or payment credentials should be committed to this repository.

## Project Status

**Status:** In development — learning and testing phase.

More features, source code, documentation, and testing results will be added as development progresses.
