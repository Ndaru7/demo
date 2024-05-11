from flask import Flask, redirect, url_for, render_template, request, session, flash
#Import datetime untuk fungsi timedelta
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "dev"
app.permanent_session_lifetime = timedelta(minutes=5)

#fungsi halaman HOME
@app.route("/")
def home():
    return render_template("index.html")

#fungsi halaman LOGIN
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        #Tapi kenapa fungsi session.permanent tidak berfungsi :)
        session.permament = True 
        user = request.form["username"]
        session["user"] = user
        flash("LOGIN Berhasil!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Anda sudah LOGIN!")
            return redirect(url_for("user"))

        return render_template("login.html")

#fungsi USER
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("Anda belum LOGIN!")
        return redirect(url_for("login"))
#fungsi LOGOUT
@app.route("/logout")
def logout():
    flash("Anda telah LOGOUT!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
