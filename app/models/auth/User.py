from app.models.auth.DatabaseFactory import DatabaseFactory

class User():
  def __init__(self, code=0, name="", email="", password="", cpf="", phone=""):
    self.code = code
    self.name = name
    self.email = email
    self.password = password
    self.cpf = cpf
    self.phone = phone
    self.connection = DatabaseFactory().getConnection()


  def login(self, email="", password=""):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT  code,  name  FROM  users  WHERE  email =%s AND password=%s"
        cursor.execute(sql, (email, password))
        result = cursor.fetchone()

        if result:
          return result
        else:
          return None
    finally:
      self.connection.close()


  def signup(self, user=None):
    try:
      with self.connection.cursor() as cursor:
        sql = "INSERT INTO users (name, email, password, cpf, phone, isStudent, studentType, isPaid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (user.name, user.email, user.password, self.cpf, self.phone, 0, 'nd', 0))
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
  def getUserByCPF(self, cpf):
    try:
      with self.connection.cursor() as cursor:
        sql = "SELECT * FROM users WHERE cpf=%s"
        cursor.execute(sql, (cpf))
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
        sql = "INSERT INTO access(user, module) VALUES (%s, %s)"
        cursor.execute(sql, (int(code), int(module)))
        self.connection.commit()

        return True
    except Exception as e:
        print(e)
        return False
    finally:
      self.connection.close()
