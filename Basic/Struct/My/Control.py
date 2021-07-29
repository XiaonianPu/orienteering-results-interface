import time
import xml.etree.ElementTree as ET
# from Network import Database
from Network import Database


class Control:
    def __init__(self, control_xml: ET.Element, competition_id=None, pk_control_id=None) -> None:
        super().__init__()
        self.competition_id = competition_id
        self.control_number = control_xml.find("./Id").text
        self.control_pos_x = control_xml.find("./MapPosition").attrib["x"]
        self.control_pos_y = control_xml.find("./MapPosition").attrib["y"]
        self.pk_control_id = int(time.time()*10**6) if pk_control_id is None else pk_control_id

    def create(self):
        db, cursor = Database.connect()
        sql = "insert into tb_control values(%s,%s,%s,%s,%s)"
        cursor.execute(sql, (self.pk_control_id, self.control_number, self.control_pos_x, self.control_pos_y, self.competition_id))
        res = db.commit()

        if res == 0:
            raise Exception("Create Control Failed")

        ql = "insert into tb_control values(%s,%s,%s,%s,%s)"
        cursor.execute(sql, (
        self.pk_control_id, self.control_number, self.control_pos_x, self.control_pos_y, self.competition_id))
        res = db.commit()

        Database.close()

    def update(self):
        db, cursor = Database.connect()
        sql = "update tb_control set event_name=%s, event_date=%s, event_location=%s where pk_event_id=%d"
        cursor.execute(sql, (self.event_name, self.event_date, self.event_location, self.pk_event_id))
        res = db.commit()
        Database.close()
        if res == 0:
            raise Exception("Update fail")

    @staticmethod
    def request(pk_event_id=""):
        db, cursor = Database.connect()
        if pk_event_id is None:
            sql = "select * from tb_event"
            cursor.execute(sql)
        else:
            sql = "select * from tb_event where pk_event_id=(%d)"
            cursor.execute(sql, pk_event_id)
        res = cursor.fetchall()
        Database.close()
        if res is not None:
            res_list = []
            for row in res:
                res_list.append(Course(row[1], row[2], row[0]))
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