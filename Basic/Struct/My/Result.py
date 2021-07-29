import time
from Basic.ResultStatistic.Interface.PunchMeta import PunchMeta
# from Network import Database
from Network import Database
from Struct.OEvent.Punch import Punch


class Result:
    def __init__(self, punch_meta: PunchMeta, entry_id=None, valid=None) -> None:
        super().__init__()
        # 也叫readout_id
        self.pk_result_id = int(time.time())
        self.entry_id = entry_id
        self.start_time = punch_meta.start_time
        self.clear_time = punch_meta.clear_time
        self.finish_time = punch_meta.finish_time
        self.valid = valid

        self.print_time = None
        self.course_type = "INDIVIDUAL"
        self.course_name = ""
        self.punch_list = punch_meta.punch_list
        self.last_to_finish = punch_meta.last_to_finish
        self.course_match_confidence = 0.0
        self.correct_punch_list = []
        self.all_punch_list = []