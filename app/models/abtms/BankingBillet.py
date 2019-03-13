# Class BankingBillet
# It is resposable for:
#   Save banking billets on database

from app.models.auth.DatabaseFactory import DatabaseFactory

class BankingBillet():
    def __init__(self, created_at="", value="0", cpf="", charge_id="", expire_at=""):
        self.created_at = created_at
        self.value = value
        self.cpf = cpf
        self.charge_id = charge_id
        self.expire_at = expire_at
        self.connection = DatabaseFactory().getConnection()

    def save(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO  bankingBillets  ( status, value ,  created_at ,  cpf ,  charge_id ,  expire_at ) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(sql, ("Esperando", self.value, self.created_at, self.cpf, self.charge_id, self.expire_at))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()

    def getAllBankingBilletsByCPF(self, cpf):
        with self.connection.cursor() as cursor:
          sql = "select * from bankingBillets where cpf=%s"

          cursor.execute(sql, (cpf))
          result = cursor.fetchall()

          if result:
            return result
          else:
            return None

    def getAllBankingBillets(self):
        try:
            with self.connection.cursor() as cursor:
              sql = "select * from bankingBillets"

              cursor.execute(sql)
              result = cursor.fetchall()

              return result
        except:
            return None

    def updateStatusFromBankingBillet(self, charge_id="", status=""):
        with self.connection.cursor() as cursor:
            sql = "update bankingBillets set status=%s where charge_id=%s"

            cursor.execute(sql, (status, charge_id))
            self.connection.commit()

            return True
