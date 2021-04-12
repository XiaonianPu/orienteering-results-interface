import datetime
import time
from Basic.ResultStatistic.Interface.PunchMeta import PunchMeta


class Punch:
    def __init__(self, punch_order, control_id, punch_time: datetime.time, delta: datetime.time, entry_id) -> None:
        super().__init__()
        self.pk_punch_id = int(time.time())
        self.control_id = control_id
        self.entry_id = entry_id
        self.punch_time = punch_time
        self.punch_order = punch_order

        self.type = "NORMAL"
        self.is_mp = False
        self.time_delta = delta

