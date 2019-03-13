from flask import request, session, redirect, render_template
from app import app
from gerencianet import Gerencianet

from app.models.abtms.Payment import Payment
from app.models.abtms.BankingBillet import BankingBillet

from app.models.abtms.User import User
from datetime import date

#function defines a expire at after 7 days
def define_expire_at():
    today = date.today()
    expire_at = date.fromordinal(today.toordinal()+7)

    return str(expire_at)

@app.route("/abtms/b/")
def b():
    user = User().getUser(session["id"])
    return render_template("errors/GenerateBankingBillet.html", user=user)

#Function defines a value to transation
def define_value(user):
    value = 0
    if "cpf" in user[0]:
        if user[0]["isStudent"] == 1:
            if user[0]["studentType"] == "grad":
                value = 5650
            else:
                value = 8150
        else:
            value = 15650
    else:
        value = 50650

    return value

@app.route("/abtms/payment/", methods=["POST"])
def pay():
    try:
        email = ""

        if session["type"] == "pessoa":
            user = User().getUser(session["id"])

            payment = Payment()

            value = define_value(user)
            charge_id = payment.create_transation(value=value)
            expire_at = define_expire_at()
            created_at = str(date.today())


            payment.create_banking_billet(user=user, charge_id=charge_id, email=email, expire_at=expire_at)

            bb = BankingBillet(value=value, created_at=created_at, cpf=user[0]["cpf"], charge_id=charge_id, expire_at=expire_at)

            bb.save()
        else:
            user = Bussiness().getBussiness(session["id"])

            payment = Payment()

            value = define_value(user)
            charge_id = payment.create_transation(value=value)
            expire_at = define_expire_at()
            created_at = str(date.today())


            payment.create_banking_billetPJ(user=user, charge_id=charge_id, email=email, expire_at=expire_at)

            bb = BankingBillet(value=value, created_at=created_at, cpf=user[0]["cnpj"], charge_id=charge_id, expire_at=expire_at)

            bb.save()

        return render_template("warnings/GenerateBankingBillet.html", user=user)

    except:
        return render_template("erros/GenerateBankingBillet.html", user=user)


@app.route("/abtms/charge/<charge_id>/")
def get_banking_billet(charge_id):
    url = Payment().getBankingBillet(charge_id)

    return redirect(url)



@app.route("/abtms/payment/creditcard/", methods=["POST"])
def pay_with_creditcard():
    try:
        token = request.form.get("token")
        charge_id = request.form.get("charge_id")

        user = User().getUser(session["id"])

        options = {
            'client_id': 'Client_Id_b566548b1a24e22fd6f0232c40eb95fb9e9b2a01',
            'client_secret': 'Client_Secret_e0b31bb41de41041921819ed90c6d68fd201cd81',
            'sandbox': True
        }

        gn = Gerencianet(options)

        params = {
            'id': charge_id
        }

        body = {
            'payment': {
                'credit_card': {
                    'installments': 1,
                    'payment_token': token,
                    'billing_address': {
                        'street': "Av. JK",
                        'number': 909,
                        'neighborhood': "Bauxita",
                        'zipcode': "35400000",
                        'city': "Ouro Preto",
                        'state': "MG"
                    },
                    'customer': {
                        'name': user[0]["name"],
                        'email': user[0]["email"],
                        'cpf': user[0]["cpf"],
                        'birth': "1977-01-15",
                        'phone_number': user[0]["phone"]
                    }
                }
            }
        }

        gn.pay_charge(params=params, body=body)

        return render_template("warnings/PayWithCreditCard.html", user=user)

    except:
        return render_template("erros/PayWithCreditCard.html", user=user)


@app.route("/abtms/payment/creditcard/")
def redirect_index_payment_credit_card():
    user = User().getUser(session["id"])
    payment = Payment()

    value = define_value(user)
    charge_id = payment.create_transation(value=value)

    return render_template("payment.html", user=user, charge_id=charge_id)
