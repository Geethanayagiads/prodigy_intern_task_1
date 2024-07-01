# prodigy_intern_task_1
# Password Complexity Checker

This Python program assesses the strength of a password based on specified criteria and provides feedback to users on the password's strength.

## Features

- **Password Strength Criteria:**
  - Length: Checks if the password meets a minimum length requirement.
  - Uppercase Letters: Checks if the password contains at least one uppercase letter.
  - Lowercase Letters: Checks if the password contains at least one lowercase letter.
  - Numbers: Checks if the password contains at least one numeric digit.
  - Special Characters: Checks if the password contains at least one special character.

- **User Interface:**
  - Utilizes Flask for the web interface.
  - Provides a user-friendly input form for entering and checking passwords.
  - Displays feedback on the password's strength (Weak, Medium, Strong).

## Usage

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Geethanayagiads/prodigy_intern_task_1/tree/main/prodigy_task_1
   cd prodigy_intern_task_1

2. Install dependencies:
   pip install -r requirements.txt


Running the Program
1. Run the Flask application:
   python password_checker_flask.py
   
2. Open your web browser and go to http://localhost:5000 to access the Password Complexity Checker.

Example
Input:
Password: "StrongPassword123!"
Output:
Strength: Strong
Files
password_checker_flask.py: Python script implementing the Password Complexity Checker.
templates/index.html: HTML template for the Flask web interface.
  
