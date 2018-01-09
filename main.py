from flask import Flask, render_template, redirect, request
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('hello_form.html')

def empty_fields():
    username = request.form['username']
    pw1 = request.form['pw1']
    pw2 = request.form['pw2']
    if not username:
        empty_username = "A user name is required"
    if not pw1:
        empty_pw1 = "A password must be supplied" 
    if not pw2:
        empty_pw2 = "A password must be supplied" 
    return render_template('hello_form.html', empty_username=empty_username, empty_pw1=empty_pw1, empty_pw2=empty_pw2)  

def pw_mismatch():
    pw1 = request.form['pw1']
    pw2 = request.form['pw2']
    if pw1 != pw2:
        pw_error = "mismatch"
    return remder_template('hello_form.html', pw_error=pw_error) 

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return render_template('hello_greeting.html', name=first_name)
 
app.run()