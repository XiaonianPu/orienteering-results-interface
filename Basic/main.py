# from Common.Class import Class
# from Common.Competition import Competition
# from Common.Course import Course
# from Common.Event import Event
# from Common.Format import Format
from SerialThread import SerialThread
from ResultStatistic.Interface.DataStandard3 import DS3
import sys
import os
import datetime
import time

USE_REMOTE_DB = False

if __name__ == "__main__":


    ds3 = DS3("../data/0410南步码头 短距离.Courses.xml")
    ds3.parse_course()
    ds3.parse_control()

    thread1 = SerialThread("COM5", "COM6", ds3)
    thread1.start()
    if USE_REMOTE_DB:
        # format_list = Format.request()
        # event_list = Event.request()
        # competition_list = Competition.request(pk_competition_id=1617985934)
        # class_list = Class.request(competition_list[0].pk_competition_id)
        # Course(ds3.course_xml_list[0],class_list[0].pk_class_id).create()
        # Course(ds3.course_xml_list[1],class_list[1].pk_class_id).create()
        # Course(ds3.course_xml_list[2],class_list[2].pk_class_id).create()
        # Course(ds3.course_xml_list[3],class_list[3].pk_class_id).create()
        pass