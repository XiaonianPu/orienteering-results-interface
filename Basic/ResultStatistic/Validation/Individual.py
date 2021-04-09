from Basic.Common.Result import Result
from Basic.ResultStatistic.Interface.PunchMeta import PunchMeta


# 检查所有路线，具备自动匹配能力
def validate(course_list, punch_meta: PunchMeta) -> Result:
    # 从指卡元数据生成成绩信息
    result = Result(punch_meta)
    # 遍历路线. 外层循环跳出条件: 有一个完全匹配的路线
    for course in course_list:
        # 正确的punch列表
        correct_punch_list = []
        # 对于打错的点，本质上是去掉其记录
        i = 0
        for order, control in enumerate(course.control_list):
            for punch in result.punch_list[i:]:
                if punch == control:
                    # 存储正确的检查点编号及其检查点顺序
                    correct_punch_list.append((order, punch))
                    i += 1
                    break
        # 出现完全匹配, 也就是有效
        if len(correct_punch_list) == len(course.control_list):
            result.course_match_confidence = 1.0
            result.course_name = course.name
            result.correct_punch_list = correct_punch_list
            result.is_valid = True
            # 有效就不用再判断了
            break
        # 不完全匹配, 也就是无效, 选择正确率最高的作为预测路线
        else:
            percentage = len(correct_punch_list) / len(course.control_list)
            # 大于的话就认为是了
            if percentage > result.course_match_confidence:
                result.course_match_confidence = percentage
                result.course_name = course.name
                result.correct_punch_list = correct_punch_list
                result.is_valid = False
            else:
                pass
    #  返回包含成绩有效性的Result
    return result
