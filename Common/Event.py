from typing import Type


class Event:
    def __init__(self, event_name, event_date, event_location) -> None:
        super().__init__()
        self.event_location = event_location
        self.event_date = event_date
        self.event_name = event_name
