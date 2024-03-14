from flask import render_template, request,current_app as app, redirect, url_for, flash, session
from .model import Show, db


@app.route("/admin_login", methods=["GET","POST"])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")
    if request.method == "POST":
        email= request.form["user_mail"]
        password = request.form["password"]
        if (email == 'admin@gmail.com' and password == "1234"):
            session['email'] = email
            return redirect('/admin')
        else:
            flash("you are not allowed to see admin func.")
            return redirect('/login')
        
@app.route("/admin")
def admin_dashboard():
    if ('email' in session):
        email_in_session = session["email"]
        shows = Show.query.all()
        return render_template('admin.html',shows=shows)
    else:
        flash("you are not allowed to see admin func.")
        return redirect('/login')
    
@app.route("/logoutAdmin")
def logoutAdmin():
    if ('email' in session):
        session.pop('email',None)
        return redirect('/login')
    else:
        flash("you are not allowed to see admin func.")
        return redirect('/login')
    

@app.route("/add_show", methods=["GET","POST"])
def add_show():
    if request.method == "GET":
        return render_template("add_show.html")
    if request.method == "POST":
        print("hello")
        show_name = request.form["name"]
        language = request.form["lang"]
        duration = request.form["duration"]
        show_poster = request.files["show_poster"]
        show_poster.save('static/'+ show_poster.filename)
        poster_img_path = str("./static/"+show_poster.filename)
        input = Show(show_name=show_name, language=language,duration=duration,poster_img_path = poster_img_path)
        db.session.add(input)
        db.session.commit()
        return redirect('/admin')




# @app.route("/edit_show")
# def edit_show():


@app.route("/dlt_show/<int:show_id>")
def dlt_show(show_id):
    show = Show.query.filter_by(show_id=show_id).first()
    db.session.delete(show)
    db.session.commit()
    return redirect('/admin')