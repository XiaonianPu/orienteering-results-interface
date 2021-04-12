import threading
import time
import serial

import ResultStatistic.Interface.Printer as pt
from ResultStatistic.Interface.DataStandard3 import DS3
from ResultStatistic.Interface.PunchMeta import PunchMeta
import ResultStatistic.Validation.Individual as Individual


class SerialThread(threading.Thread):
    def __init__(self, station_com_num, printer_com_num=None, course_data=None):
        threading.Thread.__init__(self)
        self.course_data = course_data
        self.station_com_num = station_com_num
        self.printer_com_num = printer_com_num
        try:
            self.station = serial.Serial(station_com_num, timeout=0.5)
        except OSError:
            print("主站端口打开失败")
            self.station = None
        try:
            self.printer = serial.Serial(printer_com_num, timeout=0.5)
        except OSError:
            print("打印机端口打开失败")
            self.printer = None

    def run(self) -> None:
        while True:
            time.sleep(0.5)
            if self.station is not None and self.station.inWaiting() > 0:
                time.sleep(0.5)
                _data = self.station.read_all()
                punch_meta = PunchMeta(_data)
                result = Individual.validate(self.course_data.course_list, punch_meta)
                res_str = pt.print_result(result)
                if self.printer_com_num is not None:
                    _bytes = pt.to_bytes(res_str)
                    try:
                        self.printer.write(_bytes)
                    except Exception:
                        print("Exception occurred")