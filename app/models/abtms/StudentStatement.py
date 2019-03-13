from app.models.auth.DatabaseFactory import DatabaseFactory


class StudentStatement():
  def __init__(self, user=None, path="", createdAt=""):
    self.user = user
    self.path = path
    self.createdAt = createdAt
    self.connection = DatabaseFactory().getConnection()


  def create(self):
    try:
      with self.connection.cursor() as cursor:
        sql = "INSERT INTO  studentStatement  ( user ,  path ,  createdAt, status ) VALUES (%s, %s, %s, %s)"
        print(self.user)
        cursor.execute(sql, (self.user[0]["code"], self.path, self.createdAt, "Em Processamento"))
        self.connection.commit()

        return True

    finally:
      self.connection.close()


  def getAllStudentStatementsByUser(self, code):
    try:
      with self.connection.cursor() as cursor:
        sql = "select * from studentStatement where user=%s"

        cursor.execute(sql, (code))
        result = cursor.fetchall()

        return result
    except:
        return None
    finally:
      self.connection.close()

  def getAllStudentStatements(self):
    try:
      with self.connection.cursor() as cursor:
        sql = "select studentStatement.*, users.* from studentStatement inner join users where users.code = studentStatement.user"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    except:
        return None
    finally:
      self.connection.close()


  def updateStatus(self, status="", code=""):
    with self.connection.cursor() as cursor:
      sql = "UPDATE studentStatement SET status = %s WHERE user = %s ORDER BY createdAt DESC LIMIT 1"

      cursor.execute(sql, (status, code))
      self.connection.commit()

      return True

      self.connection.close()
