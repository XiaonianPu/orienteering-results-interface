import time
from Basic.main import DB_INSTANCE

class Entry:
    def __init__(self, user_id, club_id, event_id, competition_id, class_id, pk_entry_id=None) -> None:
        super().__init__()

        self.competition_id = competition_id
        self.club_id = club_id
        self.class_id = class_id
        self.user_id = user_id
        self.pk_entry_id = int(time.time()) if pk_entry_id is None else pk_entry_id
