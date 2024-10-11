# Job Application Form App

## Description
The Job Application Form App is a web-based application that allows users to submit their job applications easily. It captures essential details such as name, email, available start date, and current occupation. The application sends a confirmation email to the applicant and stores the information in a SQLite database.

## Features
- Responsive design with Bootstrap
- Data storage using SQLAlchemy
- Email notifications upon submission
- Flash messages for user feedback

## Technologies Used
- Python
- Flask
- SQLAlchemy
- Flask-Mail
- Bootstrap
- SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/job-application-form.git
   cd job-application-form
2.  Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3.  Install the required packages:
  ```bash
  pip install -r requirements.txt
4.  Set up your Gmail credentials in the app configuration (app.py):
  ``bash
  app.config["MAIL_USERNAME"] = "your_email@gmail.com"
  app.config["MAIL_PASSWORD"] = "your_password"
5. Run the application:
  ```bash
  python app.py

