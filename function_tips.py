import datetime
def function_tips():
    czj_list=['今天星期一:\n坚持下去不是因为我很坚强,而是我别无选择','今天星期二:\n含泪播种的人一定能笑着收获','今天星期三:\n做对的事情比把事情做对更重要','今天星期四:\n命运给予我们的不是失望之酒,而是机会之杯','今天星期五:\n不要等到明天,明天太遥远,今天就行动','今天是星期六:\n求之若饥,虚心若愚','今天是星期日:\n成功将属于那些从不说不可能的人']
    day = datetime.datetime.now().weekday()
    print(czj_list[day])
function_tips()
