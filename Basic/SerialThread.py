import threading
import time
from os import environ

import serial

import ResultStatistic.Interface.Printer as pt
import ResultStatistic.Validation.Individual as Individual
from ResultStatistic.Interface.PunchMeta import PunchMeta
from Struct.OEvent.Competition import Competition
from Struct.OEvent.Competitor import Competitor
from Struct.OEvent.Event import Event


class SerialThread(threading.Thread):
    def __init__(self, station_com_num, printer_com_num=None, course_data=None, event: Event = None,
                 competition: Competition = None):
        threading.Thread.__init__(self)
        self.competition = competition
        self.event = event
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
                # 十六进制原数据
                _data = self.station.read_all()
                # 解析成元数据
                punch_meta = PunchMeta(_data)
                # Competitor Info
                competitor = None
                try:
                    competitor = Competitor.request_by_chip(punch_meta.chip_no, self.competition.stage_no)
                except Exception:
                    print("Chip NO. not registered")
                # 成绩
                result = Individual.validate(self.course_data.course_list, punch_meta)
                result.oevent_stage = self.competition.stage_no
                # 如果启用数据库存储，需要建立Punch结构并进行上传
                if environ["DB_REMOTE"] == "TRUE":
                    try:
                        result.upload_punch()
                        result.upload_result()
                    except Exception as e:
                        print(str(e))

                res_str = pt.print_result(result, competitor, self.event, self.competition)
                if self.printer_com_num is not None:
                    _bytes = pt.to_bytes(res_str)
                    try:
                        self.printer.write(_bytes)
                    except Exception:
                        print("Exception occurred")
