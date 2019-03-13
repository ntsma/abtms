from app.models.auth.DatabaseFactory import DatabaseFactory

class ComprovantePF():
    def __init__(self, charge_id=0, code=0, user=0, year=0, status="", path=""):
        self.code = code
        self.charge_id = charge_id
        self.user = user
        self.year = year
        self.status = status
        self.path = path
        self.connection = DatabaseFactory().getConnection()

    def create(self):
        try:
          with self.connection.cursor() as cursor:
            sql = "INSERT INTO comprovante_pessoa  ( user, year, status, charge_id, path ) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(sql, (self.user, self.year, self.status, self.charge_id, self.path))
            self.connection.commit()

            return True
        except Exception as e:
            print(e)
            return False
        finally:
          self.connection.close()

    def update(self, code, status):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE comprovante_pessoa SET status=%s WHERE code=%s"

                cursor.execute(sql, (status, code))
                self.connection.commit()

                return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.connection.close()

    def getComprovanteByCharge(self, charge_id):
        try:
            with self.connection.cursor() as cursor:
              sql = "SELECT * FROM comprovante_pessoa WHERE charge_id=%s"

              cursor.execute(sql, (charge_id))
              result = cursor.fetchone()

              return result
        except Exception as e:
            print(e)
            return None
        finally:
            self.connection.close()

    def getAllComprovantesByUser(self, user):
        try:
            with self.connection.cursor() as cursor:
              sql = "SELECT * FROM comprovante_pessoa WHERE user=%s"

              cursor.execute(sql, (user))
              result = cursor.fetchall()

              return result
        except Exception as e:
            print(e)
            return None
        finally:
            self.connection.close()
