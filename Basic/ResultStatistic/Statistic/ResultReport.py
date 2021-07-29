import re
from datetime import time
from time import strptime

import pandas as pd
from pandas import DataFrame


class ResultReport:
    def __init__(self, sheet) -> None:
        super().__init__()
        self.individual_split_time = []
        self.split_data = DataFrame()
        self.total_data = DataFrame()
        for i in range(2, sheet.nrows, 2):
            individual = IndividualSplitResult(sheet, i)
            self.split_data[individual.name] = individual.split_time_series()
            self.total_data[individual.name] = individual.total_time_series()
        self.split_data = self.split_data.T
        self.total_data = self.total_data.T


class IndividualSplitResult:
    def __init__(self, sheet, index) -> None:
        super().__init__()
        self.name = sheet.cell_value(index, 2)
        self.split_time = []
        self.total_time = []
        time_string = sheet.cell_value(index, 4)
        if time_string != '':
            t = time.fromisoformat(re.sub('\([1-9][0-9]?\)', '', time_string))
            t_in_second = t.second + t.minute * 60+t.hour*3600
        else:
            return
        self.split_time.append(t_in_second)
        self.total_time.append(t_in_second)
        for i in range(4, sheet.ncols):
            time_string = sheet.cell_value(index + 1, i)
            if time_string != '':
                t = time.fromisoformat(re.sub('\([1-9][0-9]?\)', '', time_string))
                t_in_second = t.second+t.minute*60+t.hour*3600
            else:
                return
            self.split_time.append(t_in_second)
            total_time = self.total_time[-1] + t_in_second
            self.total_time.append(total_time)

    def split_time_series(self):
        d = pd.Series(data=self.split_time, name=self.name)
        return d

    def total_time_series(self):
        d = pd.Series(data=self.total_time, name=self.name)
        return d
