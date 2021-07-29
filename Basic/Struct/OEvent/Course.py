import time
import xml.etree.ElementTree as ET
from Network import Database


class Course:
    def __init__(self, course_xml: ET.Element=None, class_id=None, pk_course_id=None) -> None:
        if course_xml is not None:
            self.course_title = course_xml.find("./Name").text
            self.course_length = int(course_xml.find("./Length").text)
            self.course_climb = int(course_xml.find("./Climb").text)
            self.class_id = class_id
            self.pk_course_id = int(time.time()*10**6) if pk_course_id is None else pk_course_id

        self.course_type = "INDIVIDUAL"
        self.start = course_xml.find("./CourseControl[@type='Start']/Control")
        self.finish = course_xml.find("./CourseControl[@type='Finish']/Control")
        self.control_list = list(
            map(lambda control: int(control[0].text), course_xml.findall("./CourseControl[@type='Control']")))

    def create(self):
        db, cursor = Database.connect()
        sql = "insert into tb_course values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (self.pk_course_id, self.course_title, self.course_length, self.course_type, self.course_climb, self.class_id))
        res = db.commit()
        Database.close()
        if res == 0:
            raise Exception("Create fail")

    def update(self):
        db, cursor = Database.connect()
        sql = "update tb_event set event_name=%s, event_date=%s, event_location=%s where pk_event_id=%d"
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