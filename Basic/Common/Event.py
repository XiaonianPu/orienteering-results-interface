import time
from Network import Database


class Event:
    def __init__(self, event_name, event_date, event_location, pk_event_id) -> None:
        self.event_location = event_location
        self.event_date = event_date
        self.event_name = event_name
        self.pk_event_id = int(time.time()) if pk_event_id is None else pk_event_id

    def create(self):
        db, cursor = Database.connect()
        sql = "insert into tb_event values(%s,%s,%s,%s)"
        res = cursor.execute(sql, (self.pk_event_id, self.event_name, self.event_date, self.event_location))
        Database.DB.commit()
        Database.close(cursor)
        if res == 0:
            raise Exception("Create fail")

    def update(self):
        db, cursor = Database.connect()
        sql = "update tb_event set event_name=%s, event_date=%s, event_location=%s where pk_event_id=%d"
        cursor.execute(sql, (self.event_name, self.event_date, self.event_location, self.pk_event_id))
        res = db.commit()
        Database.close(cursor)
        if res == 0:
            raise Exception("Update fail")

    @staticmethod
    def request(pk_event_id=""):
        db, cursor = Database.connect()
        sql = 'select * from tb_event where (pk_event_id="{0}" or "{0}"="")'.format(pk_event_id)
        cursor.execute(sql)
        res = cursor.fetchall()
        Database.close(cursor)
        if res is not None:
            res_list = []
            for row in res:
                res_list.append(Event(row[1], row[2], row[3], row[0]))
            return res_list
        else:
            raise Exception("No records")

    def delete(self):
        cursor = Database.DB.cursor()
        sql = "delete from tb_event where pk_event_id=(%d)"
        res = cursor.execute(sql, self.pk_event_id)
        Database.DB.close()
        if res == 1:
            self.pk_event_id = self.event_name = self.event_date = self.event_location = None

