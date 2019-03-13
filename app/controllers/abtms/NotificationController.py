from flask import request, jsonify
from app import app
from gerencianet import Gerencianet
from app.models.abtms.ComprovantePF import ComprovantePF
from app.models.abtms.Payment import Payment
from app.models.abtms.User import User
from app.models.abtms.Print import Print


@app.route("/abtms/notifications/", methods=["POST", "GET"])
def get_notification():
    token = request.form.get("notification")
    #token = "8d4c8d6a-7cdd-419e-81c8-436e8de21c8d"

    options = {
        'client_id': 'Client_Id_b566548b1a24e22fd6f0232c40eb95fb9e9b2a01',
        'client_secret': 'Client_Secret_e0b31bb41de41041921819ed90c6d68fd201cd81',
        'sandbox': True
    }

    gn = Gerencianet(options)

    params = {
        'token': token
    }

    response = gn.get_notification(params=params)
    status = response["data"][len(response["data"]) - 1]["status"]["current"]

    if status == "paid":
        charge_id = response["data"][len(response["data"]) - 1]["identifiers"]["charge_id"]
        transation = Payment().getTransation(charge_id)

        createdAt = transation["data"]["created_at"]
        user = User().getUserByCPF(transation["data"]["customer"]["cpf"])
        status = "Pago"
        name = transation["data"]["customer"]["name"]

        path = Print().print(name=name, createdAt=createdAt, code=user)

        c = ComprovantePF(charge_id=charge_id, user=user[0]["code"], year=createdAt, status=status, path=path)
        c.create()

    return "Ok"
