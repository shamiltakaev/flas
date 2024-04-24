from flask import render_template, url_for, redirect
from app import app
from app.forms import RegisterForm
from app.data.db_session import create_session


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def signin():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect("/login")
    return render_template("register.html", form=form)



