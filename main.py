from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

signupform = """
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
        <form action="/signup" method="post">
         
            <label for="username">User Name: </label>
            <input type="text" id="username" name="username" value='{username}' /><br />
            <textarea name="text">{0}</textarea><br />
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

@app.route('/')

def validate_pw ():
    #return signupform
    return render_template('test.html', name='Sharon')
    #return signupform.format(pw1='', pw2='', pwerror='', email='', emailerror='')

app.run()