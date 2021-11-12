import time
from datetime import datetime

from Struct.OEvent.Result import Result
from Struct.OEvent.Competition import Competition
from Struct.OEvent.Competitor import Competitor
from Struct.OEvent.Event import Event

END_OF_LINE = "\r\n"


def print_line(str_in) -> str:
    res = str_in + END_OF_LINE
    print(str_in)
    return res


def to_bytes(res_str):
    return res_str.encode('gbk')


PRINTER_LINE_WIDTH = 32 # ASCII CHAR


def print_result(result: Result, competitor: Competitor = None, event: Event = None,
                 competition: Competition = None) -> str:
    # 每行32个ASCII/16个汉字
    ts = int(time.time())
    result.print_time = datetime.fromtimestamp(ts)
    res = "\r\n"
    if event is not None and competition is not None:
        title = "{0} - {1}".format(event.event_name, competition.competition_name)
        res += print_line("{}".format(title))
        res += print_line("Stage: {}".format(str(competition.stage_no)))
        res += print_line("Date: {}".format(competition.competition_date.date().isoformat()))
    if competitor is not None:
        res += print_line("Name: {} {}".format(competitor.firstname, competitor.lastname))
        res += print_line("Club: {}".format(competitor.club_name))
        res += print_line("Chip: {}".format(competitor.chip_no))
        res += print_line("Category: {}".format(competitor.cat_name))
    res += print_line("Course/Confidence:")
    res += print_line("{}/{}".format(result.course_name, result.course_match_confidence))

    res += print_line("Clear T: {}".format(result.clear_time.isoformat(timespec='seconds')))
    res += print_line("Start T: {}".format(result.start_time.isoformat(timespec='seconds')))
    res += print_line("- - - - - - - - - - - - - - - - ")
    res += print_line("{} | {} =    {}  |  {}".format("Seq", "NO.", "Acc.", "Spl"))
    for order, punch in enumerate(result.punch_list):
        res += print_line(
            " {:0>2} | {:0>3d} = {} | {}".format(order + 1, punch["punch_id"], punch["cumulate_time"].isoformat(timespec='seconds'),
                                                 punch["delta_time"].isoformat(timespec='seconds')[3:]))
    res += print_line("Finish:     {} | {}".format(result.finish_time.isoformat(timespec='seconds'),
                                                result.last_to_finish.isoformat(timespec='seconds')[3:]))
    res += print_line("Total:      {}".format(result.competition_time.isoformat(timespec='seconds')))
    res += print_line("")
    res += print_line("Validation: < {} >".format("OK" if result.is_valid else "MP"))
    res += print_line("")
    res += print_line("Print: {}".format(result.print_time.isoformat(' ')))
    res += print_line("")
    res += print_line("* * * * * * * * * * * * * * * *")
    res += print_line("   小谷围高校定向运动联合训练   ")
    res += print_line("          成绩统计插件          ")
    res += print_line("  Version 0.5  |  Python 3.7.5")
    res += print_line(" By Xiaonian Pu, SCUT, 2021/05")
    res += print_line("* * * * * * * * * * * * * * * *\r\n\r\n")
    return res
