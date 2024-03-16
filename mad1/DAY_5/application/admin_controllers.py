from flask import render_template, request,current_app as app, redirect, url_for, flash, session
from .model import Show, db


def check_file_extension(file_name):
    if file_name.split('.')[1] in ['png','avif']:
        return True
    else:
        return False

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
        page_name = "ADD New Show"
        return render_template("add_show.html", page_name=page_name,method="POST")
    if request.method == "POST":
        print("hello")
        show_name = request.form["name"]
        language = request.form["lang"]
        duration = request.form["duration"]
        show_poster = request.files["show_poster"]
        if check_file_extension(show_poster.filename):
            show_poster.save('static/'+ show_poster.filename)
            poster_img_path = str("./static/"+show_poster.filename)
            input = Show(show_name=show_name, language=language,duration=duration,poster_img_path = poster_img_path)
            db.session.add(input)
            db.session.commit()
            return redirect('/admin')
        else:
            flash("only png and avif files are allowed")
            return redirect('/add_show')
        




@app.route("/edit_show/<int:show_id>", methods=["GET","POST"])
def edit_show(show_id):
    if request.method=="GET":
        show = Show.query.filter_by(show_id=show_id).first()
        page_name = "Edit Show"
        return render_template("add_show.html",show=show, page_name=page_name)
    if request.method == "POST":
        show = Show.query.filter_by(show_id=show_id).first()
        show.show_name = request.form['name']
        show.language = request.form['lang']
        show.duration = request.form['duration']
        poster = request.files["show_poster"]
        if poster:
            if check_file_extension(poster.filename):
                poster.save('static/'+ poster.filename)
                show.poster_img_path = str("./static/"+poster.filename)
            else:
                flash("only png and avif files are allowed")
                return redirect(url_for('edit_show', show_id=show_id))
        
        db.session.commit()
        return redirect('/admin')

@app.route("/dlt_show/<int:show_id>")
def dlt_show(show_id):
    show = Show.query.filter_by(show_id=show_id).first()
    db.session.delete(show)
    db.session.commit()
    return redirect('/admin')
