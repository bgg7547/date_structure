#  136  只出现一次的数
# 异或 相异为1,相同为0  不管顺序-0
#  [1,2,3] --> 1
def olineone(data):
    res = 0
    for i in data:
        res = res ^ i
    return res


