from flask import Flask, request, redirect, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from form import Register, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask-feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route("/")
def root():
    return redirect("register.html")

@app.route('/register', methods=["GET", "POST"])
def register():

    form = Register()

    if form.validate_on_submit():
        name = form.name.data,
        pwd = form.pwd.data,
        email = form.email.data,
        first_name = form.first_name.data,
        last_name = form.last_name.data

        user = User.register(name, pwd, email, first_name, last_name)
        db.session.add(user)
        db.session.commit()

        session['username'] = user.username

        return redirect('/secret')
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():

    form = Login()

    if form.validate_on_submit():
        name = form.name.data,
        pwd = form.pwd.data

        user = User.auth(name, pwd)

        if user:
            session['username'] = user.username
            return redirect('/seceret')

        else:
            form.username.errors("login.html", form=form)

@app.route('/users/<username>')
def user_info():

    username = User.username,
    email = User.email,
    first_name = User.first_name,
    last_name = User.last_name


    return render_template('user.html', username=username,email=email, first_name=first_name, last_name=last_name)

@app.route('/secret')
def secret():
    render_template("secret.html")

@app.route('/logout')
def logout():
    session.pop('username')

    return redirect("/login")