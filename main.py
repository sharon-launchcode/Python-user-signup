from flask import Flask, render_template, redirect, request
from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True



user_input = """
        <form action="/hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <label for="username">User Name: </label>
            <input type="text" id="username" name="username" value='{{username}}' /><br />
            <p id="empty_username" class="error">{{empty_username}}</p>
            <label for="pw1">Password: </label>
            <input type="password" id="pw1" name="pw1" value='{pw1}' /><br />
            <p id="empty_pw1" class="error">{{empty_pw1}}</p>
            <p id="pw1_error" class="error">{{pw1_error}}</p>
            <label for="pw2">Confirm Password: </label>
            <input type="password" id="pw2" name="pw2" value='{{pw2}}' /><br />
            <p id="pw2_error" class="error">{{pw2_error}}</p>
            <p id="empty_pw2" class="error">{{empty_pw2}}</p>
            <p id="pwerror" class="error">{{pw_error}}</p>
            <label for="email">Email (Optional): </label>
            <input type="email" id="email" name="email" value='{{email}}'/><br />
            <p id="emailerror" class="error">{{email_error}}</p>
            <input type="submit" />
        </form>
    </body>
</html>

"""

@app.route("/")
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render()

def save_input():
    user_name = request.form['username']
    email = request.form['email']
    template = jinja_env.get_template('hello_form.html')
    return template.render(user=user_name, email=email)

def empty_fields():
    username = request.form['username']
    pw1 = request.form['pw1']
    pw2 = request.form['pw2']
    empty_username = ''
    empty_pw1 =''
    empty_pw1 =''
    if not username:
        empty_username = "A user name is required"
    if not pw1:
        empty_pw1 = "A password must be supplied" 
    if not pw2:
        empty_pw2 = "A password must be supplied" 
    template = jinja_env.get_template('hello_form.html')
    return template.render(empty_username=empty_username, empty_pw1=empty_pw1, empty_pw2=empty_pw2)  

def return_errors():
    if not pw1_error and not pw2_error and not pw_error:
        return form.format(str)          

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)


app.run()