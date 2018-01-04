from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

input_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color"#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <style>
            .error {{color:red;}}
        </style>
        <form action="/validate-input" method="post">
         
            <label for="username">User Name: </label>
            <input type="text" id="username" name="username" value='{username}' /><br />
            <label for="pw1">Password: </label>
            <input type="password" id="pw1" name="pw1" value='{pw1}' /><br />
            <label for="pw2">Confirm Password: </label>
            <input type="password" id="pw2" name="pw2" value='{pw2}' /><br />
            <p id="pwerror" class="error">{pw_error}</p>
            <label for="email">Email (Optional): </label>
            <input type="email" id="email" name="email" value='{email}' /><br />
            <p id="emailerror" class="error">{email_error}</p>
            <button type="submit" value="submit">Submit</button>
           
        </form>
    </body>
</html>
"""

@app.route('/validate-input')

def display_input_form ():
    return input_form.format(username='', pw1='', pw2='', pw_error='', email='', email_error='')

def is_integer(num):
    try:
       int(num)
       return True
    except ValueError:   
       return False

@app.route('/validate-input', methods=['POST'])
def validate_pw():
    pw1 = request.form['pw1']
    pw2 = request.form['pw2']

    pw_error = ''
    email_error = ''

    if not is_integer(pw1):
        pw_error = 'pw1 Not an integer'
    else:
        pw1 =  int(pw1)
        if pw1 >  23 or pw1 < 0:
            pw_error = 'pw1 Out of range'
    return pw_error

app.run()