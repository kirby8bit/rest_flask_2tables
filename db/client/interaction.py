from db.client.client import MySqlConnection


class DBinteraction:
    def __init__(self,host,port,user,password,db_name,rebuild_db=False):
        self.MySqlConnection = MySqlConnection(
            host=host,
            user=user,
            port=port,
            password=password,
            db_name=db_name,
            rebuild_db=rebuild_db
        )