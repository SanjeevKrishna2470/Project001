from flask import Blueprint,render_template,request,flash,redirect,url_for,session
from flask_login import current_user,login_user,login_required,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from . import db
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data=request.form
    print(data)
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user= User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("Log In Successful!",category='success')
                login_user(user, remember=True) #remembers the user across browser session. Creates a long term cookie
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password",category='error')
        else:
            flash('Email does not exist',category='error')
    return render_template("login.html",user=current_user)

@auth.route('/sign-up',methods=['GET','POST'])
def SignUp():
    data=request.form
    print(data)
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        user= User.query.filter_by(email=email).first()
        if user:
            flash('Email Already Exists!',category='error')
        else:
            if len(email) < 4:
                flash("Email must be greater than 3 characters",category='error')
            if len(firstName) < 2:
                flash("First Name must be greater than 2 characters",category='error')
            if password1 !=password2:
                flash("Passwords Don\'t Match! Try Again",category='error')
            if len(password1) < 9:
                flash("Password must have atleast 8 characters", category='error')
            else:
                new_user=User(email= email,firstName=firstName,password=generate_password_hash(password1,'pbkdf2:sha512'))
                db.session.add(new_user)
                db.session.commit()
                flash("Account Successfully Created",category='success')
                return redirect(url_for('views.home'))
            


        

    return render_template("sign-up.html",user=current_user)

@auth.route('/logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('auth.login'))




