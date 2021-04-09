from Basic.ResultStatistic.Interface.PunchMeta import PunchMeta


class Result:
    def __init__(self, punch_meta: PunchMeta) -> None:
        super().__init__()
        self.name = punch_meta.name
        self.chip_no = punch_meta.chip_no
        self.start_time = punch_meta.start_time
        self.clear_time = punch_meta.finish_time
        self.finish_time = punch_meta.finish_time
        self.print_time = None
        self.course_type = "INDIVIDUAL"
        self.course_name = ""
        self.is_valid = False
        self.punch_list = punch_meta.punch_list
        self.course_match_confidence = 0.0
        self.correct_punch_list = []

