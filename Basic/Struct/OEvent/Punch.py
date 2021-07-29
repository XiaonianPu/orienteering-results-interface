import datetime
import time


from Network import Database
from Util.TimeUtil import get_time_in_int


class Punch:
    def __init__(self, control_id, punch_time: datetime.time, readout_id, seq=0) -> None:
        super().__init__()
        self.pk_punch_id = seq
        self.control_id = control_id
        self.readout_id = readout_id
        # OEvent使用绝对时间, 且Punch表只精确到秒
        self.punch_time = get_time_in_int(punch_time, interval="1")

    def upload_punch(self):
        db, cursor = Database.connect()
        sql = "select MAX(ID) from OEVSIPUNCHES"
        cursor.execute(sql)
        res = cursor.fetchone()
        _id = 0
        if res[0] is not None:
            _id = res[0]+1
        sql = "insert into OEVSIPUNCHES values(?,?,?,?)"
        cursor.execute(sql, (_id, self.readout_id, self.control_id, self.punch_time))
        res = db.commit()
        if res == 0:
            raise Exception("Upload Punch Data Failed")
        Database.close()