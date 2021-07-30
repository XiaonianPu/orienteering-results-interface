import xlrd
from matplotlib import pyplot as plt
from pylab import *

from ResultStatistic.Statistic.ResultReport import IndividualSplitResult, ResultReport

mpl.rcParams['font.sans-serif'] = ['SimHei']


class ResultReader:
    NAME_COL_INDEX = 0

    def __init__(self, file_name, type='normal') -> None:
        super().__init__()
        self.type = type
        self.file_name = file_name
        self.book = xlrd.open_workbook(self.file_name)
        self.class_name = None
        self.title = None
        self.sheet = None
        self.result = None

    def plot_split_differ_line_chart(self, from_i=None, to_k=None):
        start = 0 if from_i is None else from_i
        end = len(self.result.split_data) if to_k is None else to_k
        fig = plt.figure(dpi=200, figsize=(10, 6), tight_layout=True)
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel("检查点序号")
        ax.set_ylabel("分段时间差值")
        ax.grid(color="lightgrey", linestyle='-', linewidth=1)
        min_split = self.result.split_data.min()
        rows = [data for data in self.result.split_data.iterrows()]
        for name, data in rows[start:end]:
            ax.plot(range(1, len(data) + 1), data - min_split,
                    label=name,
                    mfc='white',
                    markersize=3.25,
                    linewidth=1.,
                    markevery=1)
        plt.show()

    def plot_split_differ_violin_chart(self):
        fig = plt.figure(dpi=200, figsize=(10, 6), tight_layout=True)
        ax = fig.add_subplot(1, 1, 1)

        ax.set_xlabel("检查点序号", size='x-large')
        ax.set_ylabel("归一化分段用时", size='x-large')
        ax.grid(color="lightgrey", linestyle='-', linewidth=1)
        result_drop_na = self.result.split_data.iloc[:, :].dropna(axis='index')
        result_drop_na_scaled = (result_drop_na - result_drop_na.min()) / (result_drop_na.max() - result_drop_na.min())
        props = ax.boxplot(result_drop_na_scaled, showmeans=True, notch=True)
        ax.set_title(self.title + '\n{}'.format(self.class_name) + '\n各分段归一化(Min-Max Normalization)用时', fontsize='xx-large')
        ax.set_ylim(-0.1, 1.1)
        plt.figtext(0.7, 0.03, 'By Xiaonian Pu @ SCUT', fontsize=15, c='grey')
        plt.figtext(0.05, 0.03, '绿色、红色分别表示对应分段进行归一化操作前最短、最长用时', fontsize=10, c='grey')
        self.boxplot_plot_style_setting(props, ax, box_min=result_drop_na.min(), box_max=result_drop_na.max())
        plt.show()

    @staticmethod
    def violin_plot_style_setting(parts):
        for part in parts["bodies"]:
            part.set_facecolor('c')
            part.set_edgecolor('teal')
            part.set_alpha(0.7)

        linewidth = 1
        color = "black"
        alpha = 0.8
        parts["cmins"].set_color(color)
        parts["cmins"].set_alpha(alpha)
        parts["cmins"].set_linewidth(linewidth)

        parts["cbars"].set_color(color)
        parts["cbars"].set_alpha(alpha)
        parts["cbars"].set_linewidth(linewidth)

        parts["cmaxes"].set_color(color)
        parts["cmaxes"].set_alpha(alpha)
        parts["cmaxes"].set_linewidth(linewidth)

        parts["cmedians"].set_color(color)
        parts["cmedians"].set_alpha(alpha)
        parts["cmedians"].set_linewidth(linewidth)

    @staticmethod
    def boxplot_plot_style_setting(parts, ax, box_min=None, box_max=None):
        caps = parts['caps']
        for index in range(0, len(caps), 2):
            box_id = int(index / 2)
            ax.annotate(str(int(box_min[box_id])), (box_id + 1, -0.05), c='g', weight='heavy', ha='center', size='x-large')
            ax.annotate(str(int(box_max[box_id])), (box_id + 1, 1.02), c='r', weight='heavy', ha='center', size='large')
        pass

    def plot_differ_line_chart(self, from_i=None, to_k=None):
        start = 0 if from_i is None else from_i
        end = len(self.result.total_data) if to_k is None else to_k
        fig = plt.figure(dpi=200, figsize=(10, 6), tight_layout=True)
        fig.autofmt_xdate()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title(self.title + '\n{}'.format(self.class_name) + '\n累计时间差值折线图' + '(前{}名)'.format(end - start), fontsize='xx-large')
        ax.set_xlabel("检查点序号", size='x-large')
        ax.set_ylabel("累计时间差值", size='x-large')
        ax.grid(color="lightgrey", linestyle='-', linewidth=1)
        min_total = self.result.total_data.min()
        rows = [data for data in self.result.total_data.iterrows()]
        for name, data in rows[start:end]:
            ax.plot(range(1, len(data) + 1), data - min_total,
                    label=name,
                    mfc='white',
                    markersize=8,
                    linewidth=3.25,
                    marker='o',
                    markevery=1)
        leg = ax.legend(fontsize='x-large', markerscale=1.5, handlelength=3, loc='best', ncol=3,
                        numpoints=1,
                        borderaxespad=0.3,
                        columnspacing=0.3,
                        labelspacing=0.3,
                        borderpad=0.3,
                        handletextpad=0.3)
        plt.figtext(0.7, 0.03, 'By Xiaonian Pu @ SCUT', fontsize=15, c='grey')
        leg_lines = leg.get_lines()
        plt.setp(leg_lines, linewidth=2.5)

        plt.show()

    def read(self):
        print("Current result file name:{}".format(self.file_name))

        print("Contains class name:")
        name_list = self.book.sheet_names()
        for index, name in enumerate(name_list):
            print("[{}] {}".format(index + 1, name))
        index = int(input("select the class you want to analysis\n")) - 1
        self.sheet = self.book.sheet_by_index(index)
        self.sheet.get_rows()
        self.class_name = self.sheet.name
        print("Class '{}' selected".format(self.class_name))
        self.title = self.sheet.cell_value(0, 0)
        self.result = ResultReport(self.sheet)
