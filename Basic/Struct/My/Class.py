import time

from Network import Database


class Class:
    def __init__(self, class_name, competition_id, pk_class_id=None) -> None:
        self.competition_id = competition_id
        self.class_name = class_name
        self.pk_class_id = int(time.time()*10**6) if pk_class_id is None else pk_class_id
        # print(self.pk_class_id)

    def create(self):
        db, cursor = Database.connect()
        sql = "insert into tb_class values(%s,%s,%s)"
        cursor.execute(sql, (self.pk_class_id, self.competition_id, self.class_name))
        res = db.commit()
        Database.close()
        if res == 0:
            raise Exception("Create fail")
        return self

    @staticmethod
    def request(competition_id="", pk_class_id=""):
        db, cursor = Database.connect()
        sql = 'select * from tb_class where (pk_class_id="{0}" or "{0}"="") and (competition_id="{1}" or "{1}"="")'.format(pk_class_id,competition_id)
        cursor.execute(sql)
        res = cursor.fetchall()
        Database.close(db,cursor)
        if res is not None:
            res_list = []
            for row in res:
                res_list.append(Class(row[1], row[2], row[0]))
            return res_list
        else:
            raise Exception("No records")