from app import app
from flask import render_template, request, redirect, url_for
from person import Person, people


@app.route('/home') 
@app.route('/') 
def home():
    return render_template('Home.html', title="Home", people=people )

@app.route('/info', methods=["GET", "POST"]) 
def info():
    if request.method =='POST':
        try:
            age = int(request.form['Age'])
            if age <=0:
                return render_template('Info.html', title="Info", error = "Укажите правельный возраст")
            elif len(request.form["Fname"])<=3:
                return render_template('Info.html', title="Info", error = "Укажите правельное имя") 
            elif len(request.form["Lname"])<=3:
                return render_template('Info.html', title="Info", error = "Укажите правельную фамилию") 
            Person(request.form["Fname"], request.form['Lname'], age) 
        except:
            return render_template('Info.html', title="Info", error = "Пройзошла ошибка!")
        return render_template('Info.html', title="Info")


    return render_template('Info.html', title="Info")