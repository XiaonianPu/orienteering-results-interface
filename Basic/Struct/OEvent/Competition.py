import time
from datetime import date, datetime

from Network import Database


class Competition:
    def __init__(self, competition_name, competition_date: datetime,  stage_no, event_id) -> None:
        self.stage_no = stage_no
        self.competition_date = competition_date
        self.competition_name = competition_name
        self.event_id = event_id

    @staticmethod
    def request(pk_event_id, stage):
        db, cursor = Database.connect()
        sql = 'select NAME{0}, DATE{0}, FIRSTSTART{0} from OEVCOMPETITION where ID=?'.format(stage)
        cursor.execute(sql, (pk_event_id,))
        res = cursor.fetchone()
        Database.close()
        if res is not None:
            return Competition(res[0],res[1],stage,pk_event_id)
        else:
            raise Exception("No records")