import binascii
from datetime import time

from Util.TimeUtil import get_delta_time, time_shift, get_time_in_int

OPERATION_LENGTH = 2
TIME_LENGTH = 8
START_POS = 2
FINISH_POS = START_POS + TIME_LENGTH + OPERATION_LENGTH
CLEAR_POS = FINISH_POS + TIME_LENGTH + OPERATION_LENGTH

FIRST_PUNCH = 2
SECOND_PUNCH = FIRST_PUNCH + TIME_LENGTH + OPERATION_LENGTH
THIRD_PUNCH = SECOND_PUNCH + TIME_LENGTH + OPERATION_LENGTH

TIME_SHIFT = time(hour=0,minute=25,second=48)
TIME_SHIFT_IS_DELAYED = True


# 返回时 分 秒 1/100秒
def time_str_to_time(time_str: str) -> time:
    if time_str.startswith("FFFFFF"):
        return time(0, 0, 0)
    elif len(time_str) > 6:
        ptime = time(int(time_str[0:2], 16), int(time_str[2:4], 16), int(time_str[4:6], 16), int(time_str[6:8], 16))
        atime = time_shift(ptime,TIME_SHIFT, TIME_SHIFT_IS_DELAYED)
        return atime
    else:
        ptime = time(int(time_str[0:2], 16), int(time_str[2:4], 16), int(time_str[4:6], 16))
        atime = time_shift(ptime, TIME_SHIFT, TIME_SHIFT_IS_DELAYED)
        return atime


class PunchMeta:
    def __init__(self, raw_data):
        self.name = None
        self.raw_data = raw_data
        self.chip_no = None
        self.start_time = time()
        self.clear_time = time()
        self.finish_time = time()
        self.competition_time = time()
        self.last_to_finish = time()
        self.hex_string = None
        self.station_no = None
        self.result_block_list = []
        # punch_list[i] = (punch_id, cumulate_time, delta_time,absolute_punch_time)
        self.punch_list = []
        self.event_type = "INDIVIDUAL"
        self.convert_to_hex_string()
        self.decode_result()

    def convert_to_hex_string(self):
        self.hex_string = str(binascii.hexlify(self.raw_data).upper())[2:-1]

    def decode_result(self):
        self.station_no = self.hex_string[:8]
        self.result_block_list = self.hex_string.split(self.station_no)[1:]
        self.chip_no = int(self.result_block_list[0][2:-2])

        self.clear_time = time_str_to_time(self.result_block_list[1][CLEAR_POS + OPERATION_LENGTH:])

        self.start_time = time_str_to_time(self.result_block_list[1][START_POS + OPERATION_LENGTH:FINISH_POS])
        self.finish_time = time_str_to_time(self.result_block_list[1][FINISH_POS + OPERATION_LENGTH:CLEAR_POS])
        self.competition_time = get_delta_time(self.finish_time,self.start_time)
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
                if get_time_in_int(self.finish_time) > 0:
                    self.last_to_finish = get_delta_time(self.finish_time, punch_time)
                self.punch_list.append(
                    {"punch_id":punch_id,
                     "cumulate_time":cumulate_time,
                     "delta_time":delta_time,
                     "punch_time":punch_time})

