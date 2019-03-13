# encoding: utf-8

from gerencianet import Gerencianet

class Payment():
    def create_transation(self, value=0):
        credentials = {
            'client_id': 'Client_Id_b566548b1a24e22fd6f0232c40eb95fb9e9b2a01',
            'client_secret': 'Client_Secret_e0b31bb41de41041921819ed90c6d68fd201cd81',
            'sandbox': True
        }

        gn = Gerencianet(credentials)

        body = {
            'items': [{
                'name': "Inscrição De Associado",
                'value': int(value),
                'amount': 1
            }
          ],
          "metadata": {
            "notification_url": "http://200.137.131.117/abtms/notifications/",
            "custom_id": "Eduardo"
          }
        }

        res = gn.create_charge(body=body)

        return res["data"]["charge_id"]


    def create_banking_billet(self, user, charge_id, email, expire_at):
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
                'banking_billet': {
                    'expire_at': expire_at,
                    'customer': {
                        'name': user[0]["name"],
                        'email': user[0]["email"],
                        'cpf': user[0]["cpf"],
                        'phone_number': user[0]["phone"]
                    }
                }
            }
        }

        gn.pay_charge(params=params, body=body)


    def create_banking_billetPJ(self, user, charge_id, email, expire_at):
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
                'banking_billet': {
                    'expire_at': expire_at,
                    'customer': {
                        'name': "Eduardo Silva Vieira",
                        'email': user[0]["email"],
                        'cpf': "61049006313",
                        'phone_number': user[0]["phone"],
                        'juridical_person': {
                                        'corporate_name': user[0]["name"],
                                        'cnpj': user[0]["cnpj"]
                                    }
                    }
                }
            }
        }

        gn.pay_charge(params=params, body=body)



    def getBankingBillet(self, charge_id):
        options = {
            'client_id': 'Client_Id_b566548b1a24e22fd6f0232c40eb95fb9e9b2a01',
            'client_secret': 'Client_Secret_e0b31bb41de41041921819ed90c6d68fd201cd81',
            'sandbox': True
        }

        gn = Gerencianet(options)

        params = {
            'id': int(charge_id)
        }

        response =  gn.detail_charge(params=params)

        return response["data"]["payment"]["banking_billet"]["pdf"]["charge"]


    def getTransation(self, charge_id):
        options = {
            'client_id': 'Client_Id_b566548b1a24e22fd6f0232c40eb95fb9e9b2a01',
            'client_secret': 'Client_Secret_e0b31bb41de41041921819ed90c6d68fd201cd81',
            'sandbox': True
        }

        gn = Gerencianet(options)

        params = {
            'id': int(charge_id)
        }

        response =  gn.detail_charge(params=params)

        return response
