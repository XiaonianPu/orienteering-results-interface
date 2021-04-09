import threading
import time
import serial

import ResultStatistic.Interface.Printer as pt
from ResultStatistic.Interface.DataStandard3 import DS3
from ResultStatistic.Interface.PunchMeta import PunchMeta
import ResultStatistic.Validation.Individual as Individual


class SerialThread(threading.Thread):
    def __init__(self, course_xml_path, station_com_num, printer_com_num=None):
        threading.Thread.__init__(self)
        self.course_xml_path = course_xml_path
        self.course_data = DS3(course_xml_path)
        self.station_com_num = station_com_num
        self.printer_com_num = printer_com_num

        self.station = serial.Serial(station_com_num, timeout=0.5)
        self.printer = serial.Serial(printer_com_num, timeout=0.5)

    def run(self) -> None:
        while True:
            time.sleep(0.5)
            if self.station.inWaiting() > 0:
                time.sleep(0.5)
                _data = self.station.read_all()
                punch_meta = PunchMeta(_data)
                result = Individual.validate(self.course_data.course_list, punch_meta)
                res_str = pt.print_result(result)
                if self.printer_com_num is not None:
                    _bytes = pt.to_bytes(res_str)
                    self.printer.write(_bytes)
