from flask import render_template, url_for , flash , redirect
from webblog.models import User, Post
from webblog.forms import RegistrationForm , LoginForm 
from webblog import app,db,bcrypt
from flask_login import login_user , current_user , logout_user

posts = [
    {
        'author': 'Innoviti',
        'title': 'Project 2',
        'content': 'Software Developer',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Enliten IT India',
        'title': 'Project 1',
        'content': 'Full-Stack Dev',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',posts=posts,title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account is created','success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form,title='Regsiter')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password ,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else :
            flash('Login Unsuceesful. Please check Email and Password.','danger')
    return render_template('login.html',form=form,title='Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
def account():
    return render_template('account.html',title='Account')