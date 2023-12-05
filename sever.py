from flask import Flask, render_template, request
import os
from methods import *

app = Flask(__name__)
methods = methods()

@app.route('/')
def mainMenu():
    
    return render_template('main.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        result = [email, password]
        print(result, "post")
        return render_template('general/login.html')
    else:
        return render_template('general/login.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if methods.addUser(username, email, password) == True:
            print("user: ", username, " added")
        else:
            print("Email is already registered")
        return render_template('general/register.html')
    else:
        return render_template('general/register.html')

@app.route('/v20')
def v20sheet():
    return render_template('vampire/V20/characterSheet.html')

if __name__ == '__main__':
   app.run(debug=True)