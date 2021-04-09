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
    result.print_time = datetime.now()
    res = "\r\n"
    res += print_line("选手姓名: {}".format(result.name))
    res += print_line("指卡号码: {}".format(result.chip_no))
    res += print_line("清除时间: {}".format(result.clear_time.isoformat(timespec='seconds')))
    res += print_line("起点时间: {}".format(result.start_time.isoformat(timespec='seconds')))
    res += print_line("- - - - - - - - - - - - - - - - ")
    res += print_line("{}|{}  {}   |{}".format("顺序", "编号", "时间", "差值"))
    for order, punch in enumerate(result.punch_list):
        res += print_line(
            " {:2d} | {:0>3d} = {} | {}".format(order, punch[0], punch[1].isoformat(timespec='seconds')[3:],
                                                punch[2].isoformat(timespec='seconds')[3:]))
    res += print_line("终点时间: {}".format(result.finish_time.isoformat(timespec='seconds')))
    res += print_line("打印时间: {}".format(result.print_time.isoformat(' ')))
    res += print_line("路线名称/匹配置信度: [{}/{}]".format(result.course_name, result.course_match_confidence))
    res += print_line("有效性: < {} >".format("有效" if result.is_valid else "无效"))
    res += print_line(" * * * * * * * * * * * * * * * *")
    res += print_line("小谷围高校定向运动联合训练 成绩统计插件")
    res += print_line("  Version 0.3  |  Python 3.7.5  ")
    res += print_line(" By Xiaonian Pu, SCUT, 2021/04  ")
    res += print_line(" * * * * * * * * * * * * * * * * \r\n\r\n")
    return res
