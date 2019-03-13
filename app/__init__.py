# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, session, request, redirect
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__, static_folder='static', static_url_path='')


app.config["SECRET_KEY"] = "@session"


from app.controllers.auth import UserController
from app.controllers.abtms import Default
from app.controllers.abtms import StudentStatement
from app.controllers.abtms import PaymentController
from app.controllers.abtms import NotificationController
from app.controllers.api import Members
from app.controllers.abtms import ComprovanteController


from app.models.abtms.User import User
from app.models.auth.Bussiness import Bussiness
from app.models.abtms.StudentStatement import StudentStatement
from app.models.abtms.BankingBillet import BankingBillet
from app.models.abtms.ComprovantePF import ComprovantePF


app.config.update(
        DEBUG=True,
        #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'edusvieirap@gmail.com',
        MAIL_PASSWORD = '@edusvieirap'
        )

mail = Mail(app)


@app.route("/abtms/users/<code>/student/", methods=["post"])
def res_student(code):
  res = request.form.get("type")

  if res == "nd":
    User().updateUserType(res=0, code=code)
    User().updateType(type=res, code=code)
    StudentStatement().updateStatus(status="Negado", code=session["id"])

  else:
    User().updateUserType(res=1, code=code)
    User().updateType(type=res, code=code)
    StudentStatement().updateStatus(status="Aprovado", code=session["id"])

  return redirect("/abtms/modules/")


@app.route("/abtms/users/<code>/student")
def auth_student(code):
  user = User().getUserByCPF(code)
  return render_template("student.html", user=user)

@app.route("/abtms/auth/reset/pf/")
def rreset():
    return render_template("reset_pf.html")

@app.route("/abtms/auth/reset/pf/", methods=["POST"])
def reset():
    cpf = request.form.get("cpf")

    user = User().getUserByCPF(cpf)

    title = "Recuperação de Senha"
    message = "Olá, {0}, sua senha é {1}. Caso deseje mudar de senha, clique no link abaixo http://127.0.0.1:8000/abtms/reset/{2}".format(user["name"], user["password"], user["email"])

    msg = Message(
        title,
        sender='edusvieirap@gmail.com',
        recipients=
        [user["email"]])

    msg.html = message
    mail.send(msg)

    return "Ok", 200

@app.route("/abtms/auth/reset/")
def rre():
    return render_template("reset.html")


@app.route("/abtms/auth/reset/pj/")
def rresetpj():
    return render_template("reset_pj.html")

@app.route("/abtms/auth/reset/pj/", methods=["POST"])
def resetpj():
    cnpj = request.form.get("cnpj")

    user = User().getUserByCNPJ(cnpj)

    title = "Recuperação de Senha"
    message = "Olá, {0}, sua senha é {1}. Caso deseje mudar de senha, clique no link abaixo http://127.0.0.1:8000/abtms/reset/pj/{2}".format(user["name"], user["password"], user["email"])

    msg = Message(
        title,
        sender='edusvieirap@gmail.com',
        recipients=
        [user["email"]])

    msg.html = message
    mail.send(msg)

    return "Ok", 200


def check(module):
    if session["type"] == "pessoa":
      user = User().getUser(session["id"])
    else:
      user = Bussiness().getBussiness(session["id"])

    for row in user:
        if row["modules.name"] == module:
            return True

    return False


@app.route("/abtms/finance/")
def finance():
    if check(module="Financeiro"):
        return render_template("finance.html")
    else:
        return render_template("405.html")


@app.route("/abtms/admin/")
def admin():
    if check(module="Administrador"):
        user = User().getUser(session["id"])

        users = User().getAllUsers()
        bussinesses = Bussiness().getAllBussinesses()
        dashboard = get_informations()
        studentStatements = StudentStatement().getAllStudentStatements()

        print(studentStatements)

        return render_template("admin.html", user=user, users=users, bussinesses=bussinesses, dashboard=dashboard, studentStatements=studentStatements)
    else:
        return render_template("405.html")


def get_informations():
    users = User().getAllUsers()
    bussinesses = Bussiness().getAllBussinesses()
    bankingBillets = BankingBillet().getAllBankingBillets()

    numPendentBankingBillets = 0
    numCanceledBankingBillets = 0

    for bb in bankingBillets:
        if bb["status"] == "Esperando":
            numPendentBankingBillets += 1
        elif bb["status"] == "Cancelado":
            numCanceledBankingBillets += 1

    numActivedMembers = 0

    for user in users:
        if user["isPaid"] == 1:
            numActivedMembers += 1

    for bussiness in bussinesses:
        if bussiness["isPaid"] == 1:
            numActivedMembers += 1

    numMembers = len(users) + len(bussinesses)
    numPendentMemebers = numMembers - numActivedMembers

    dashboard = {
        "numMembers": numMembers,
        "numActivedMembers": numActivedMembers,
        "numPendentMemebers": numPendentMemebers,
        "free": 0,
        "pendentCharges": numPendentBankingBillets,
        "canceledCharges": numCanceledBankingBillets
    }

    return (dashboard)


@app.route("/abtms/members/")
def members():
    if check(module="Associação"):
        studentStatement = None
        if session["type"] == "pessoa":
          user = User().getUser(session["id"])
          studentStatements = StudentStatement().getAllStudentStatementsByUser(session["id"])
          bankingBillets = BankingBillet().getAllBankingBilletsByCPF(user[0]["cpf"])
          comprovantes = ComprovantePF().getAllComprovantesByUser(session["id"])
        else:
          user = Bussiness().getBussiness(session["id"])

          bankingBillets = None
          comprovantes = None

        return render_template("members.html", user=user, bankingBillets=bankingBillets, studentStatements=studentStatements, comprovantes=comprovantes)
    else:
        return render_template("405.html")

@app.route("/abtms/login/", methods=["GET"])
def rlogin():
  return render_template("login.html")


@app.route("/abtms/logout/")
def logout():
    session.pop("id")

    return redirect("/abtms/")

@app.route("/abtms/users/", methods=["POST"])
def update_user():
    id = session["id"]
    name = request.form.get("name")
    email = request.form.get("email")

    if User().updateUser(name=name, email=email, id=id):
        user = User().getUser(session["id"])
        return render_template("warnings/UpdatePersonalInformation.html", user=user)
    else:
        return "Error", 500

@app.route("/abtms/password/", methods=["POST"])
def update_pass():
    password = request.form.get("password")
    email = request.form.get("email")

    if User().updatePassword(password=password, email=email):
        return "OK", 200
    else:
        return "Error", 500


@app.route("/abtms/settings/pf/")
def settings():
    user = User().getUser(session["id"])

    return render_template("settings.html", user=user)

@app.route("/abtms/settings/pj/")
def settingspj():
    user = Bussiness().getUser(session["id"])

    return render_template("settingspj.html", user=user)

@app.route("/abtms/signup/", methods=["GET"])
def rsignup():
  return render_template("signup.html")

@app.route("/abtms/signup/person/", methods=["GET"])
def rsignupperson():
  return render_template("person.html")


@app.route("/abtms/signup/bussiness/", methods=["GET"])
def rsignupbussiness():
  return render_template("bussiness.html")



@app.route("/abtms/")
def index():
  return render_template("index.html")


@app.route("/abtms/modules/")
def modules():
  if session["type"] == "pessoa":
    user = User().getUser(session["id"])
  else:
    user = Bussiness().getBussiness(session["id"])

  tam = len(user)

  return render_template("modules.html", user=user, tam=tam)
