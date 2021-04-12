import time
from datetime import date

from Network import Database


class Competition:
    def __init__(self, competition_name, competition_date: date,  format_id, event_id, pk_competition_id=None) -> None:
        self.competition_date = competition_date
        self.competition_name = competition_name
        self.format_id = format_id
        self.event_id = event_id
        self.pk_competition_id = int(time.time()) if pk_competition_id is None else pk_competition_id

    def create(self):
        db, cursor = Database.connect()
        sql = "insert into tb_competition values(%s,%s,%s,%s,%s)"
        cursor.execute(sql, (self.pk_competition_id, self.competition_name, self.competition_date, self.format_id, self.event_id))
        res = db.commit()
        Database.close(db,cursor)
        if res == 0:
            raise Exception("Create fail")
        else:
            return self

    def update(self):
        db, cursor = Database.connect()
        sql = "update tb_competition set competition_name=%s, competition_date=%s where pk_competition_id=%d"
        cursor.execute(sql, (self.competition_name, self.competition_date, self.pk_competition_id))
        res = db.commit()
        Database.close(db,cursor)
        if res == 0:
            raise Exception("Update fail")

    @staticmethod
    def request(pk_event_id="", pk_competition_id=""):
        db, cursor = Database.connect()
        sql = 'select * from tb_competition where (pk_competition_id="{0}" or "{0}"="") and (event_id="{1}"  or "{1}"="")'.format(pk_competition_id,pk_event_id)
        cursor.execute(sql)
        res = cursor.fetchall()
        Database.close(db,cursor)
        if res is not None:
            res_list = []
            for row in res:
                res_list.append(Competition(row[1], row[2], row[3], row[4], row[0]))
            return res_list
        else:
            raise Exception("No records")

    def delete(self):
        db, cursor = Database.connect()
        sql = "delete from tb_competition where pk_competition_id=(%d)"
        res = cursor.execute(sql, self.pk_competition_id)
        Database.close(db, cursor)
        if res == 1:
            self.competition_name = self.competition_date = self.format_id = self.event_id = self.pk_competition_id = None
