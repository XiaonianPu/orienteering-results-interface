from Network.Database import Database


class Event:
    def __init__(self, db:Database) -> None:
        super().__init__()
        self.db = db

    def create(self, event_name, event_date, event_location):
        sql = "insert into tb_event values(%s,%s,%s)"
        res = self.db.cursor.execute(sql,(event_name, event_date, event_location))

    def update(self, event_name, event_date, event_location):
        sql = "update tb_event set event_name=%s, event_date=%s, event_location=%s where pk_event_id=%d"
        res = self.db.cursor.execute(sql, (event_name, event_date, event_location))

    def request(self):
        sql = "delete from tb_event where pk_event_id=(%d)"
        self.db.cursor.

    def delete(self, event_id):
        sql = "delete from tb_event where pk_event_id=(%d)"
        res = self.db.cursor.execute(sql,event_id)
        return res

class Competition:


class Classes:


class Course:


class Control:


class Entry:


class Punch:


class Result: