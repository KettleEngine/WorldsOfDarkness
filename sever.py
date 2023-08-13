from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def mainMenu():
    
    return render_template('main.html')

@app.route('/v20')
def v20sheet():
    return render_template('vampire/V20/characterSheet.html')

if __name__ == '__main__':
   app.run(debug=True)