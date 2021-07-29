import time
from Network import Database


class Event:
    def __init__(self, pk_event_id, event_name, event_location,  num_of_stage) -> None:
        self.event_location = event_location
        self.num_of_stage = num_of_stage
        self.event_name = event_name
        self.pk_event_id = pk_event_id

        self.stage_name = None
        self.stage_date = None

    @staticmethod
    def request(pk_event_id):
        db, cursor = Database.connect()
        sql = 'select COMPETITIONNAME, NUMBEROFSTAGES, COMPETITIONPLACE from OEVCOMPETITION where ID=?'
        cursor.execute(sql, (pk_event_id,))
        res = cursor.fetchone()
        stage = 0
        if res is not None:
            stage = res[1]
            name = res[0]
            place = res[2]
            return Event(pk_event_id, name, place, stage)
        else:
            raise Exception("No records")
