from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('hello_form.html')

@app.route("/", methods=['POST'])
def validate_fields():
    username = request.form["username"]
    pw1 = request.form["pw1"]
    pw2 = request.form["pw2"]
    email = request.form["email"]

    username_error = ''
    pw1_error = ''
    pw2_error = ''
    pw_error = ''
    email_error = ''

    if len(username) < 3:
        username = ''
        username_error = 'Username must be more than 3 characters'
    elif len(username) > 20:
        username = ''
        username_error = 'Username must be less than 20 characters'
    else:
        username = username
    #https://www.infoworld.com/article/2655121/security/password-size-does-matter.html
    #https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/password
    if 20 < len(pw1) < 3:
        pw1 = ''
        pw1_error = 'Password must contain more than 3characters long, 20 max, minimum 14 recommended'

    if 20 < len(pw2) < 3:
        pw2 = ''
        pw2_error = 'Verification password must contain more than 3 characters long, 20 max, minimum 14 recommended'    

    if pw1 != pw2:
        pw1 = ''
        pw2 = ''
        pw_error = 'Passwords do not match'

    #Criteria for email are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long
    if len(email) > 0:
        if not(email.endswith('@') or email.startswith('@') or email.endswith('.') or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email=email
        else:
            email = ''
            email_error = 'Improperly formed email  -- it must contain an @ sign, only one period, and is between 3 and 20 characters long'
    else:
        email = ''

    if username == "":
        username_error = 'Username must be more than 3 characters but no more than 20'
    if pw1 == "":
        pw1_error = 'Your first password field was left empty. Set a password, no fewer than 3 and no longer than 20 characters'
    if pw2 == "":
        pw2_error = 'Your second password field was left empty. Enter a password to match the one above, no fewer than 3 and no longer than 20 characters'


    if not username_error and not pw1_error and not pw2_error and not email_error:
        return render_template('hello_greeting.html', username = username)

    else:
        return render_template('hello_form.html', username_error=username_error, pw1_error=pw1_error, pw2_error=pw2_error, email_error=email_error,
        username=username, pw1=pw1, pw2=pw2, email=email)

app.run()