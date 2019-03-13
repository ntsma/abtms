from flask import render_template, request, jsonify, redirect, session

from app import app

from app.models.abtms.User import User
from app.models.auth.Bussiness import Bussiness

@app.route("/abtms/reset/<email>/")
def upPass(email):
    return render_template("reset_password.html", email=email)


@app.route("/abtms/reset/pj/<email>/")
def upPassPJ(email):
    return render_template("reset_passwordPJ.html", email=email)


@app.route("/abtms/reset/", methods=["POST"])
def upudatePass():
    password = request.form.get("password")
    email = request.form.get("email")

    if User().updatePassword(password=password, email=email):
        return redirect("/abtms/login/")

    return redirect("/abtms/")


@app.route("/abtms/reset/pj/", methods=["POST"])
def upudatePassPJ():
    password = request.form.get("password")
    email = request.form.get("email")

    if Bussiness().updatePassword(password=password, email=email):
        return redirect("/abtms/login/")

    return redirect("/abtms/")
