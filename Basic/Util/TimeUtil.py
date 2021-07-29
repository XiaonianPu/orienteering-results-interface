from datetime import timedelta, time


def get_delta_time(current: time, previous: time) -> time:
    c_delta = timedelta(hours=current.hour, minutes=current.minute, seconds=current.second)
    p_delta = timedelta(hours=previous.hour, minutes=previous.minute, seconds=previous.second)
    delta = c_delta - p_delta
    return time.fromisoformat(str(delta).rjust(8, '0'))


def time_shift(readout_punch_time:time, shift:time, is_delayed:bool):
    if is_delayed:
        read_delta = timedelta(hours=readout_punch_time.hour, minutes=readout_punch_time.minute, seconds=readout_punch_time.second)
        shift_delta = timedelta(hours=shift.hour, minutes=shift.minute, seconds=shift.second)
        actual_delta = read_delta-shift_delta
        return time.fromisoformat(str(actual_delta).rjust(8, '0'))
    else:
        read_delta = timedelta(hours=readout_punch_time.hour, minutes=readout_punch_time.minute,
                               seconds=readout_punch_time.second)
        shift_delta = timedelta(hours=shift.hour, minutes=shift.minute, seconds=shift.second)
        actual_delta = read_delta + shift_delta
        return time.fromisoformat(str(actual_delta).rjust(8, '0'))


def get_time_in_int(current: time, interval="1/100") -> int:
    c_delta = timedelta(hours=current.hour, minutes=current.minute, seconds=current.second)
    p_delta = timedelta()
    delta = c_delta - p_delta
    if interval == "1/100":
        return int(delta.total_seconds() * 100 + delta.microseconds / 100)
    elif interval == "1":
        return int(delta.total_seconds())
    else:
        return 0
