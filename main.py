from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

userform = """
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
        <form action="/signup" method="post">
         
            <label for="username">User Name: </label>
            <input type="text" id="username" name="username" value="" /><br />
            <textarea name="text">{0}</textarea><br />
            <label for="pw1">Password: </label>
            <input type="password" id="pw1" name="pw1" value="" /><br />
            <label for="pw2">Confirm Password: </label>
            <input type="password" id="pw2" name="pw2" value="" /><br />
            <label for="email">Email (Optional): </label>
            <input type="email" id="email" name="email" value="" /><br />
            <button type="submit" value="submit">Submit</button>
           
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")
 
@app.route("/", methods=['POST'])


app.run()