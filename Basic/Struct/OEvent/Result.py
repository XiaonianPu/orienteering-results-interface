import datetime
import time
from datetime import timedelta

import snowflake
from Basic.ResultStatistic.Interface.PunchMeta import PunchMeta
# from Network import Database
from Network import Database
from Struct.OEvent.Punch import Punch
from Util.TimeUtil import get_time_in_int


class Result:
    def __init__(self, punch_meta: PunchMeta, entry_id=None, stage_id=None) -> None:
        super().__init__()
        # 也叫readout_id
        self.pk_result_id = int(time.time())
        self.entry_id = entry_id
        self.start_time = punch_meta.start_time
        self.clear_time = punch_meta.clear_time
        self.finish_time = punch_meta.finish_time
        self.competition_time = punch_meta.competition_time
        self.chip_no = punch_meta.chip_no
        self.is_valid = None

        self.print_time = None
        self.course_type = "INDIVIDUAL"
        self.course_name = ""
        self.punch_list = punch_meta.punch_list
        self.last_to_finish = punch_meta.last_to_finish
        self.course_match_confidence = 0.0
        self.correct_punch_list = []
        self.all_punch_list = []

        self.oevent_punch_list = []
        self.oevent_stage = stage_id

    def upload_punch(self):
        for index, punch in enumerate(self.punch_list):
            oevent_punch = Punch(punch["punch_id"],punch["punch_time"], self.pk_result_id, seq=index)
            oevent_punch.upload_punch()

    def upload_result(self):
        db, cursor = Database.connect()
        sql = "insert into OEVSICARDREADOUT values(?,?,?,?,?,?,?,?,?)"
        param = (
            self.pk_result_id,
            self.chip_no,
            datetime.datetime.now(),
            int(get_time_in_int(self.clear_time, interval="1")),
            int(get_time_in_int(self.clear_time, interval="1")),
            int(get_time_in_int(self.start_time, interval="1")),
            int(get_time_in_int(self.finish_time, interval="1")),
            0,
            self.pk_result_id
        )
        cursor.execute(sql, param)
        res = db.commit()
        if res == 0:
            raise Exception("Upload Result Data Failed")

        sql = "update OEVCOMPETITOR set STARTTIME{0}=?, FINISHTIME{0}=?, PUNCHID{0}=?, COMPETITIONTIME{0}=?, FINISHTYPE{0}=? where CHIPNUMBER{0}=?".format(self.oevent_stage)
        valid = 1 if self.is_valid else 5
        param = (
            int(get_time_in_int(self.start_time)),
            int(get_time_in_int(self.finish_time)),
            self.pk_result_id,
            int(get_time_in_int(self.competition_time)),
            valid,
            self.chip_no
        )
        cursor.execute(sql, param)
        res = db.commit()
        if res == 0:
            raise Exception("Upload Result Data Failed")
        Database.close()

