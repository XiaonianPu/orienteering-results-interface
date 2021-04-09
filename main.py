from ResultStatistic.Interface.DataStandard3 import DS3
from SerialThread import SerialThread

if __name__ == "__main__":

    thread1 = SerialThread("COM5", "COM6")
    thread1.start()
    ds3 = DS3("data/百米决赛.Courses.xml")
    ds3.parse_course()
    ds3.parse_control()



