from Basic.Common.Event import Event
from Basic.Network.Database import Database


class Operation(Database):
    def __init__(self, u, p, host, db) -> None:
        super().__init__(u, p, host, db)

    def create(self, args):
        sql = "insert into tb_event values(%s,%s,%s)"
        res = self.cursor.execute(sql, (event.event_name, event.event_date, event.event_location))

    def update(self, event: Event):
        sql = "update tb_event set event_name=%s, event_date=%s, event_location=%s where pk_event_id=%d"
        res = self.cursor.execute(sql, (event_name, event_date, event_location))

    def request(self, event: Event):
        sql = "delete from tb_event where pk_event_id=(%d)"
        self.cursor.

    def delete(self, event: Event):
        sql = "delete from tb_event where pk_event_id=(%d)"
        res = self.db.cursor.execute(sql,(event.event_id))
        return res

class Competition:


class Classes:


class Course:


class Control:


class Entry:


class Punch:


class Result: