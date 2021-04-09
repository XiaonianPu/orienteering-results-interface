import binascii
from datetime import time, timedelta, datetime

OPERATION_LENGTH = 2
TIME_LENGTH = 8
START_POS = 2
FINISH_POS = START_POS + TIME_LENGTH + OPERATION_LENGTH
CLEAR_POS = FINISH_POS + TIME_LENGTH + OPERATION_LENGTH

FIRST_PUNCH = 2
SECOND_PUNCH = FIRST_PUNCH + TIME_LENGTH + OPERATION_LENGTH
THIRD_PUNCH = SECOND_PUNCH + TIME_LENGTH + OPERATION_LENGTH


# 返回时 分 秒 1/100秒
def time_str_to_time(time_str: str) -> time:
    if time_str.startswith("FFFFFF"):
        return time(0, 0, 0)
    elif len(time_str) > 6:
        return time(int(time_str[0:2], 16), int(time_str[2:4], 16), int(time_str[4:6], 16), int(time_str[6:8], 16))
    else:
        return time(int(time_str[0:2], 16), int(time_str[2:4], 16), int(time_str[4:6], 16))


def get_delta_time(current: time, previous: time) -> time:
    c_delta = timedelta(hours=current.hour, minutes=current.minute, seconds=current.second)
    p_delta = timedelta(hours=previous.hour, minutes=previous.minute, seconds=previous.second)
    delta = c_delta - p_delta
    return time.fromisoformat(str(delta))


class PunchMeta:
    def __init__(self, raw_data):
        self.name = None
        self.raw_data = raw_data
        self.chip_no = None
        self.start_time = None
        self.clear_time = None
        self.finish_time = None
        self.hex_string = None
        self.station_no = None
        self.result_block_list = []
        self.punch_list = []
        self.event_type = "INDIVIDUAL"
        self.convert_to_hex_string()
        self.decode_result()

    def convert_to_hex_string(self):
        self.hex_string = str(binascii.hexlify(self.raw_data).upper())[2:-1]

    def decode_result(self):
        self.station_no = self.hex_string[:8]
        self.result_block_list = self.hex_string.split(self.station_no)[1:]
        self.chip_no = self.result_block_list[0][2:-2]

        self.clear_time = time_str_to_time(self.result_block_list[1][CLEAR_POS + OPERATION_LENGTH:])

        self.start_time = time_str_to_time(self.result_block_list[1][START_POS + OPERATION_LENGTH:FINISH_POS])
        self.finish_time = time_str_to_time(self.result_block_list[1][FINISH_POS + OPERATION_LENGTH:CLEAR_POS])
        punch_block_list = self.result_block_list[2:-1]
        previous_punch_time = self.start_time
        for punch_block in punch_block_list:
            # punch以"0D"字节开头, 一个校验码字节结尾
            trimmed_punch_block = punch_block[2:-2]
            # 处理第一块打卡记录
            for i in range(3):
                shift = i * 8
                punch = trimmed_punch_block[shift:shift + 8]
                if punch.startswith("FF"):
                    break
                punch_id = int(punch[:2], 16)
                punch_time = time_str_to_time(punch[2:])
                # 处理时间差, 第一个点的时间差是与起点做比较
                delta_time = get_delta_time(punch_time, previous_punch_time)
                previous_punch_time = punch_time
                #  累积时间是与起点的时间差
                cumulate_time = get_delta_time(punch_time, self.start_time)
                self.punch_list.append((punch_id, cumulate_time, delta_time))