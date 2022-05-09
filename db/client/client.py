from sqlite3 import connect
import sqlalchemy 
from sqlalchemy.orm import sessionmaker

class MySqlConnection:
    def __init__(self,host,port,user,password,db_name,rebuild_db=False):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port
        self.rebuild_db = rebuild_db

        session = sessionmaker(
            #это еще не все 
        )
    def get_connection(self,db_created=False):
        engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name if db_created else ""}',
            encoding = 'utf-8'
        )
        return engine.connect()
    
    def connect(self):
        connection = self.get_connection()
        if self.rebuild_db:
            connection.execute(f'DROP DATABASE IF EXISTS {self.db_name}')
            connection.execute(f'CREATE DATABASE {self.db_name}')
        return self.get_connection(db_created=True)
