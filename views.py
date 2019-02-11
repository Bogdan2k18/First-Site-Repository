from app import app
from flask import render_template, request, redirect, url_for
from sun_maminoi_podrugi import get_gallary, loginForm, User, registerForm



@app.route('/') 
def home():
    return render_template('Home.html')

@app.route('/gallary') 
def gallary():
    imgs = get_gallary()
    return render_template('gallary.html', imgs = imgs)

@app.route('/test', methods=['GET', 'POST']) 
def test():
    form = loginForm()
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        user = User(name, password)
        if user.status:
            return redirect('gallary')
        else:
            return render_template('test.html', form=form, error="Неверный логин или пароль")
    # if form.validate_on_submit():
    #     return redirect('/gallary')

    return render_template('test.html', form=form)

@app.route('/reg', methods=['GET', 'POST']) 
def reg():
    show = True
    form = registerForm()
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        phone = request.form['phone_number']
        address = request.form['address']
        req = User.add_new(name, password, phone, address)
        return render_template('reg.html', error = req[0], form=form, show = req[1], color = req[2])
    else:
        return render_template('reg.html', form = form, show = True)
        

