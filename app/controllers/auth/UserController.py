from flask import render_template, request, jsonify, redirect, session

from app import app

from app.models.auth.User import User
from app.models.auth.Bussiness import Bussiness

from app.models.auth.Encrypto import Encrypto

@app.route("/auth/login/", methods=["POST"])
def login():
  email = request.form.get("email")
  password = request.form.get("password")

  user = User()

  result = user.login(email=email, password=password)


  if result:
    message = {
      "name": result["name"],
      "email": email,
      "message": "OK",
      "code": 200
    }

    token = Encrypto().encode(message)
    session["type"] = "pessoa"
    session["id"] = result["code"]

    return token, 200

  else:
    message = {
      "name": "",
      "email": "",
      "message": "NOT FOUND",
      "code": 404
    }

    token = Encrypto().encode(message)

    return token, 404

@app.route("/auth/login/bussiness/", methods=["POST"])
def loginb():
  email = request.form.get("email")
  password = request.form.get("password")

  bussiness = Bussiness()

  result = bussiness.login(email=email, password=password)


  if result:
    message = {
      "name": result["name"],
      "email": email,
      "message": "OK",
      "code": 200
    }

    token = Encrypto().encode(message)

    session["type"] = "empresa"
    session["id"] = result["code"]

    return token, 200

  else:
    message = {
      "name": "",
      "email": "",
      "message": "NOT FOUND",
      "code": 404
    }

    token = Encrypto().encode(message)

    return token, 404


@app.route("/auth/signup/person/", methods=["POST"])
def signup():
  name = request.form.get("name")
  email = request.form.get("email")
  password = request.form.get("password")
  cpf = request.form.get("cpf")
  phone = request.form.get("phone")

  user = User(name=name, email=email, password=password, cpf=cpf, phone=phone)

  result = user.signup(user=user)

  if result:
    u = User().getUserByCPF(cpf)

    if User().registerModule(module=1, code=u["code"]):
        return "OK", 200
  else:
    return "ERROR", 403


@app.route("/auth/signup/bussiness/", methods=["POST"])
def signupb():
  name = request.form.get("name")
  email = request.form.get("email")
  password = request.form.get("password")
  cnpj = request.form.get("cnpj")
  phone = request.form.get("phone")

  b = Bussiness(name=name, email=email, password=password, cnpj=cnpj, phone=phone)

  result = b.signup(bussiness=b)

  if result:
    bu = Bussiness().getBussinessByCNPJ(cnpj)
    
    if Bussiness().registerModule(module=1, code=bu["code"]):
      return "OK", 200
    else:
      return "ERROR", 403
