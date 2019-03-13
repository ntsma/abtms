from app.models.auth.DatabaseFactory import DatabaseFactory

class Bussiness():
  def __init__(self, code=0, name="", email="", password="", cnpj="", phone=""):
    self.code = code
    self.name = name
    self.email = email
    self.password = password
    self.cnpj = cnpj
    self.phone = phone
    self.connection = DatabaseFactory().getConnection()


  def getBussiness(self, id):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT bussiness.*, modules.* FROM access INNER JOIN modules INNER JOIN bussiness WHERE access.bussiness=%s AND bussiness.code=%s AND access.module=modules.code"
        cursor.execute(sql, (id, id))
        result = cursor.fetchall()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()


  def login(self, email="", password=""):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT * FROM  bussiness  WHERE  email =%s AND password=%s"
        cursor.execute(sql, (email, password))
        result = cursor.fetchone()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()


  def getUser(self, id):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT bussiness.* FROM bussiness WHERE code=%s"
        cursor.execute(sql, (id))
        result = cursor.fetchall()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()

  def getAllBussinesses(self):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT bussiness.* FROM bussiness"
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()



  def updatePassword(self, password="", email=""):
    try:
        with self.connection.cursor() as cursor:
          sql = "UPDATE bussiness SET bussiness.password=%s WHERE bussiness.email=%s"

          cursor.execute(sql, (password, email))
          self.connection.commit()

          return True
    finally:
        self.connection.close()


  def signup(self, bussiness=None):
    try:
      with self.connection.cursor() as cursor:
        sql = "INSERT INTO  bussiness  ( name ,  email ,  password ,  cnpj ,  phone ) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (bussiness.name, bussiness.email, bussiness.password, bussiness.cnpj, bussiness.phone))
        self.connection.commit()

        return True

    finally:
      self.connection.close()

  def check_permissions(self, user="", module=""):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT * FROM access WHERE user=%s AND module=%s"
        cursor.execute(sql, (user, module))
        result = cursor.fetchone()

        if result:
          return True
        else:
          return False
    finally:
      self.connection.close()



#Returns one user on database by CPF
  def getBussinessByCNPJ(self, cnpj):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT * FROM bussiness WHERE cnpj=%s"
        cursor.execute(sql, (cnpj))
        result = cursor.fetchone()

        return result
    except Exception as e:
        print(e)
        return None
    finally:
      self.connection.close()

#Registers user on module
  def registerModule(self, module, code):
    try:
      with self.connection.cursor() as cursor:
        sql = "INSERT INTO  access  ( bussiness ,  module ) VALUES (%s, %s)"
        cursor.execute(sql, (int(code), int(module)))
        self.connection.commit()

        return True
    except Exception as e:
        print(e)
        return False
    finally:
      self.connection.close()
