import time
from datetime import datetime

from Basic.Common.Result import Result

END_OF_LINE = "\r\n"


def print_line(str_in) -> str:
    res = str_in + END_OF_LINE
    print(res)
    return res


def to_bytes(res_str):
    return res_str.encode('gbk')


def print_result(result: Result) -> str:
    # 每行32个ASCII/16个汉字
    ts = int(time.time())
    result.print_time = datetime.fromtimestamp(ts)
    res = "\r\n"
    # res += print_line("Name: {}".format(result.name))
    # res += print_line("Chip: {}".format(result.chip_no))
    res += print_line("Course/Confidence:")
    res += print_line("{}/{}".format(result.course_name, result.course_match_confidence))

    res += print_line("Clear T: {}".format(result.clear_time.isoformat(timespec='seconds')))
    res += print_line("Start T: {}".format(result.start_time.isoformat(timespec='seconds')))
    res += print_line("- - - - - - - - - - - - - - - - ")
    res += print_line("{} | {} =  {}  |  {}".format("Seq", "NO.", "Acc", "Spl"))
    for order, punch in enumerate(result.all_punch_list):
        res += print_line(
            " {:0>2} | {:0>3d} = {} | {}".format(punch[0], punch[1], punch[2].isoformat(timespec='seconds')[3:], punch[3].isoformat(timespec='seconds')[3:]))
    res += print_line("Finish:  {} | {}".format(result.finish_time.isoformat(timespec='seconds'), result.last_to_finish.isoformat(timespec='seconds')[3:]))
    res += print_line("Print: {}".format(result.print_time.isoformat(' ')))

    res += print_line("Validation: < {} >".format("OK" if result.valid else "MP"))
    res += print_line("* * * * * * * * * * * * * * * *")
    res += print_line("   小谷围高校定向运动联合训练   ")
    res += print_line("          成绩统计插件          ")
    res += print_line("  Version 0.4  |  Python 3.7.5")
    res += print_line(" By Xiaonian Pu, SCUT, 2021/04")
    res += print_line("* * * * * * * * * * * * * * * *\r\n\r\n")
    return res
