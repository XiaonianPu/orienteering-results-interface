import sys
import time
from Network import Database


class Format:
    def __init__(self, format_name, pk_format_id=None) -> None:
        self.format_name = format_name
        self.pk_format_id = int(time.time()) if pk_format_id is None else pk_format_id

    @staticmethod
    def request():
        db, cursor = Database.connect()
        sql = "select * from tb_format"
        cursor.execute(sql)
        res = cursor.fetchall()
        Database.close(cursor)
        if res is not None:
            format_list = []
            for row in res:
                format_list.append(Format(row[1], row[0]))
            return format_list
        else:
            raise Exception("No records")