import pymysql


class Database:
    def __init__(self, u, p, host, db) -> None:
        super().__init__()
        self.conn = pymysql.connect(user=u, password=p, host=host, database=db)
        self.cursor = self.conn.cursor()