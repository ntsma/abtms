import os
from werkzeug.security import generate_password_hash, check_password_hash

from flask_mail import Mail
from flask import request, redirect, session, render_template, jsonify, send_from_directory
from flask_mail import Message
from app import app

from app.models.abtms.User import User
from app.models.abtms.StudentStatement import StudentStatement
from datetime import date

UPLOAD_FOLDER = "/home/laws/abtms/app/static/documents/"


mail = Mail(app)

@app.route("/abtms/documents/studentStatement/", methods=["POST"])
def sendStudentStatement():
    createdAt = str(date.today())
    studentStatement = request.files["studentStatement"]

    filename = generate_password_hash(studentStatement.filename) + ".pdf"

    studentStatement.save(os.path.join(UPLOAD_FOLDER, filename))

    path = "/documents/" + filename

    ss = StudentStatement(createdAt=createdAt, path=path, user=User().getUser(session["id"]))

    if ss.create():
      msg = Message(
                "ABTms - Novo Pedido Declaração de Estudante",
                sender='edusvieirap@gmail.com',
                recipients=["edusvieirap@gmail.com"])
      with app.open_resource(app.static_folder + ss.path) as fp:
        msg.attach("Documento.pdf", "application/pdf", fp.read())

        header = "Associado<br>" + "Informações sobre associado: <br>Nome: {0}<br>CPF: {1}<br>".format(ss.user[0]["name"], ss.user[0]["cpf"])
        middle = "O comprovante enviado pelo estudante está em anexo.<br>Para confirmar a autenticidade dele, clique no botão abaixo e escolha a categoria correta do estudante (Graduação ou Pós-Graduação) ou caso não seja válido, escolha a opção 'Não é um estudante'."
        msg.html = header + middle + "<br><a href='http://200.137.131.117/abtms/users/{0}/student'>Ir para Página de Confirmação</a>".format(ss.user[0]["cpf"])
        mail.send(msg)


        return redirect("/abtms/members/")
    else:
        return "Houve um problema ao carregar documento.", 400
