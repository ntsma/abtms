import pymysql.cursors

class DatabaseFactory():
  def __init__(self):
    self.connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='mysql',
                                 db='authdb',
                                 charset='utf8mb4',     cursorclass=pymysql.cursors.DictCursor)

  def getConnection(self):
    return self.connection
