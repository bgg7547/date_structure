# 暴力
# def biggestCommondivisor(x,y):
#     small = min(x,y)
#     big = max(x,y)
#     if big % small == 0:
#         return small
#     for i in range(small // 2, 0, -1):
#         if big % i == 0 and small % i == 0:
#             return i


#辗转相除
# def biggestCommondivisor(x,y):
#     small = min(x,y)
#     big = max(x,y)
#     if big % small == 0:
#         return small
#     return biggestCommondivisor(small,big % small)

# 更相减损数
# def biggestCommondivisor(x,y):
#     if x - y == 0:
#         return x
#     big = max(x,y)
#     small = min(x,y)
#     return biggestCommondivisor(big - small,small)
# print(biggestCommondivisor(1,1))


# 更，辗组合版
def biggestCommondivisor(x,y):
    big = max(x,y)
    small = min(x,y)
    if big - small == 0:
        return small
    if big % small == 0:
        return small
    return biggestCommondivisor(small,big % small)

print(biggestCommondivisor(124546,5576))


# def minbeishu(x,y):
#
#     i = max(x,y)
#     while True:
#         if i % x == 0 and i % y == 0:
#             return i
#         i += 1
# print(minbeishu(9,0))
