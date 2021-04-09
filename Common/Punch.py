from datetime import time, timedelta


class Punch:
    def __init__(self, punch_order, punch_id, punch_time: time, delta: time) -> None:
        super().__init__()
        self.type = "NORMAL"
        self.id = punch_id
        self.time = punch_time
        self.time_delta = delta
        self.order = punch_order
        self.is_mp = False

