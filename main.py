from flask import Flask, render_template, redirect, request
from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

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
    if not username:
        empty_username = "A user name is required"

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)


app.run()