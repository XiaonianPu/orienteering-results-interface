from ResultStatistic.Interface.ResultReader import ResultReader

if __name__ == "__main__":
    reader = ResultReader('C:/Users/Administrator/Desktop/0724/短距离赛点排名报表.xls')
    reader.read()
    # reader.plot_split_differ_line_chart(from_i=0,to_k=10)
    reader.plot_differ_line_chart(from_i=0,to_k=10)
    reader.plot_split_differ_violin_chart()