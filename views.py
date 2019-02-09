from app import app
from flask import render_template
from flask import request

@app.route('/') 
def home():
    return render_template('Home.html')

@app.route('/vadim') 
def vadim():
    return render_template('Vadim.html')

@app.route('/test') 
def test():
    return render_template('test.html')