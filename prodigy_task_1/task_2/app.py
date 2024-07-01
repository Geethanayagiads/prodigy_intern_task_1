from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_complexity(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password! 👍"
    else:
        feedback = "Weak password. Consider the following improvements:<br>"
        if not length_criteria:
            feedback += "- Ensure the password is at least 8 characters long<br>"
        if not uppercase_criteria:
            feedback += "- Include at least one uppercase letter<br>"
        if not lowercase_criteria:
            feedback += "- Include at least one lowercase letter<br>"
        if not digit_criteria:
            feedback += "- Include at least one digit<br>"
        if not special_char_criteria:
            feedback += "- Include at least one special character (!@#$%^&*(),.?\":{}|<>)<br>"

        return feedback

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        password = request.form['password']
        result = check_password_complexity(password)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
