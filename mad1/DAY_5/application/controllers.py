from flask import render_template, request,current_app as app, redirect, url_for, flash
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt



from .model import *


#---------------- initiallizing login manager-------
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)






@app.route("/")
def home():
    return render_template('home.html')



@app.route("/login",methods=["GET","POST"] )
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        user_mail = request.form["user_mail"]
        password = request.form["password"]
        user = User.query.filter_by(user_mail= user_mail).first()
        if not user:
            flash("you are not registered please register")
            return redirect("/register")
        else:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect("/user_home")
            else:
                flash("brother doesn\'t match")
                return redirect("/login")
        

    

@app.route("/register",methods=["GET","POST"] )
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        user_name = request.form["user_name"]
        user_mail = request.form["user_mail"]
        password = request.form["password"]
        user = User.query.filter_by(user_mail= user_mail).first()
        # print(user)
        # print(user.user_mail)
        # print(user.password)
        if user:
            flash("user mail already registerd please login")
            return redirect("/login")
        hashed_password= bcrypt.generate_password_hash(password)
        input = User(user_name=user_name, user_mail=user_mail, password=hashed_password)
        db.session.add(input)
        db.session.commit()
        flash("you are now registerd please login")
        return redirect(url_for("login"))
    



@app.route("/user_home",methods=["GET","POST"])
@login_required
def user_home():
    if request.method == "GET":
        return render_template("form.html")
    

   
@app.route("/form_post", methods=["POST"])
def form_post():
    if request.method == "POST":
        return "hello i am here"
    

