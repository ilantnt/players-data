import mysql.connector


mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE mydatabase")
#

class DB:
    def __init__(self,host,user,pwd,db_name):
        self.host = host
        self.user = user
        self.password = pwd
        self.database = db_name
        self.DBManager = self.connect()
        self.cursor = self.DBManager.cursor()

    def connect(self):
        self.DBManager = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.pwd,
            database=self.database
        )

    def insert_db(self,players):
        self.cursor.executemany("""
            INSERT INTO %s (name, gender)
            VALUES (%(name)s, %(gender)s)""", self.database, players)
        self.cursor.commit()