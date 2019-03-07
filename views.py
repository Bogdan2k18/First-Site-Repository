from app import app
from flask import render_template, request, redirect, url_for
from person import Person, people

@app.route('/') 
def home():
    return render_template('Home.html', title="HomePage__", people=people )

@app.route('/info') 
def info():
    return render_template('Info.html')