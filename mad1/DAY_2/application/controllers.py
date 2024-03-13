from flask import render_template, request,current_app as app

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        name = request.form["entered_name"]
        return render_template('home.html',name1=name)
    
@app.route("/form_post", methods=["POST"])
def form_post():
    if request.method == "POST":
        return "hello i am here"