from ResultStatistic.Interface.ResultReader import ResultReader

if __name__ == "__main__":
    reader = ResultReader('E:\\定向\\华工定向\\2021省锦标赛\\百米.xls', save_path='E:\\定向\\华工定向\\2021省锦标赛\\')
    reader.read()
    list_of_stars_men = ['钟海旭']
    list_of_stars_women = ['翟卓然', '何滢政']
    list_of_stars_100_women = ['邝晓怡', '石宇琪']
    list_of_stars_100_men = ['黄梓熙']
    # reader.plot_split_differ_line_chart('蒲小年')
    # for i in range(1, 23):
    #     reader.plot_split_hist('蒲小年', i)
    reader.plot_differ_line_chart(from_i=0, to_k=5, list_of_stars=list_of_stars_100_men)
    # reader.plot_split_differ_violin_chart()