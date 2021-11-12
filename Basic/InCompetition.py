# from Struct.Class import Class
# from Struct.Competition import Competition
# from Struct.Course import Course
# from Struct.Event import Event
# from Struct.Format import Format
from SerialThread import SerialThread
from ResultStatistic.Interface.DataStandard3 import DS3
import sys
import os
import datetime
import time

from Struct.OEvent.Competition import Competition
from Struct.OEvent.Event import Event

USE_REMOTE_DB = False

if __name__ == "__main__":
    event_id = input("Input COMPETITION_ID:")
    event = Event.request(int(event_id))
    if event is not None:
        print("Event name: {0}\nEvent Place:{1}\nNumber of stage:{2}\n".format(event.event_name,event.event_location,event.num_of_stage))
    else:
        raise Exception("Event request failed")
    stage = input("Input STAGE:")
    competition = Competition.request(event_id, stage)
    if competition is not None:
        print("Stage name: {0}\nStage date:{1}\n".format(competition.competition_name,competition.competition_date))
    else:
        raise Exception("stage request failed")
    path = "../data/"
    fl = os.listdir(path)
    filtered_fl = list(filter(lambda file: file.endswith(".Courses.xml"), fl))
    print("Chose the IOFXML file of {0} - stage {1}\n".format(event.event_name,competition.stage_no))
    for index, file in enumerate(filtered_fl):
        print("Index: {0}   ----    {1}".format(str(index+1), file))
    selected_file_index = int(input("Please input index:"))
    print("\n\nSelect file is: {0}\n".format(path+filtered_fl[selected_file_index-1]))
    ds3 = DS3(path+filtered_fl[selected_file_index-1])
    print("Contained courses name:")
    for index, course in enumerate(ds3.course_list):
        print("[{0}]   Title: {1}, Length: {2}m, Climb: {3}m".format(str(index), course.course_title, str(course.course_length), str(course.course_climb)))
    thread1 = SerialThread("COM5", "COM6", ds3, event, competition)
    thread1.start()
    if USE_REMOTE_DB:
        # format_list = Format.request()
        # event_list = Event.request()
        # competition_list = Competition.request(pk_competition_id=1617985934)
        # class_list = Class.request(competition_list[0].pk_competition_id)
        # Course(ds3.course_xml_list[0],class_list[0].pk_class_id).create()
        pass
