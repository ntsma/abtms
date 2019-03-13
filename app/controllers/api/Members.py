from flask import jsonify
from app import app
import csv
import json

from app.models.abtms.User import User
from app.models.auth.Bussiness import Bussiness
from app.models.abtms.BankingBillet import BankingBillet

def getSituation(situation):
    if situation == 0:
        return "Não Pago"
    return "Pago"


def getType(type):
    if type == "nd":
        return "Pessoa Física"
    elif type == "gra":
        return "Estudante de Graduação"
    elif type == "pos":
        return "Estudante de Pós Graduação"

@app.route("/api/abtms/users/<cpf>/")
def get_user(cpf):
    try:
        result = User().getUserByCPF(cpf)

        user = {
            "name": result[0]["name"],
            "cpf": result[0]["cpf"],
            "type": getType(result[0]["studentType"]),
            "phone": result[0]["phone"],
            "situation": getSituation(result[0]["isPaid"])
        }

        return jsonify(user)
    except:
        print("[ERRO NA API] - CONSULTAR ASSOCIADO PESSOA FÍSICA")
        return None

@app.route("/api/abtms/bussinesses/<cnpj>/")
def get_bussiness(cnpj):
    try:
        result = Bussiness().getBussinessByCNPJ(cnpj)

        user = {
            "name": result["name"],
            "cnpj": result["cnpj"],
            "type": "Pessoa Jurídica",
            "phone": result["phone"],
            "situation": getSituation(result["isPaid"])
        }

        return jsonify(user)
    except:
        print("[ERRO NA API] - CONSULTAR ASSOCIADO PESSOA JURÍDICA")
        return None


@app.route("/api/abtms/members/informations/")
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

    return jsonify(dashboard)


@app.route("/api/abtms/members/informations/csv/")
def get_informations_as_cvs():
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
        "numMembers": str(numMembers),
        "numActivedMembers": str(numActivedMembers),
        "numPendentMemebers": str(numPendentMemebers),
        "free": str(0),
        "pendentCharges": str(numPendentBankingBillets),
        "canceledCharges": str(0)
    }

    #Convertendo para CVS

    x = """[
        {
          "canceledCharges": "0",
          "free": "0",
          "numActivedMembers": "0",
          "numMembers": "10",
          "numPendentMemebers": "10",
          "pendentCharges": "3"
        }

    ]"""

    print(x)

    x = json.loads(str(x))

    f = csv.writer(open("test.csv", "w"))

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["Numero de Associados", "Numero de Ativos", "Numero de Pendentes", "Isentos", "Pagamentos Cancelados", "Pagamentos Pendentes"])

    for x in x:
        f.writerow([x["numMembers"],
                    x["numActivedMembers"],
                    x["numPendentMemebers"],
                    x["free"],
                    x["canceledCharges"],
                    x["pendentCharges"]])


    return "OK"
