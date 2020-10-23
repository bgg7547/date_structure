# 中心扩散，每个都是中心，往左右扩散 相同继续扩，不同break，

# def longestPalindrome(s):
#     n = len(s)
#     if n < 2:
#         return n
#     max_lenth = 1
#     res = s[0]
#     for i in range(n - 1):
#         odd = centerSpread(s,i,i)
#         even = centerSpread(s,i,i + 1)
#         maxstr = odd if len(odd) > len(even) else even
#         if len(maxstr) > max_lenth:
#             max_lenth = len(maxstr)
#             res = maxstr
#     return res
#
# def centerSpread(s,left,right):
#     lenth = len(s)
#     i = left
#     j = right
#     while i >= 0 and j < lenth:
#         if s[i] == s[j]:
#             i -= 1
#             j += 1
#         else:
#             break
#     return s[i + 1: j]

# print(longestPalindrome("0,1,1,1,0,1,1,1,2"))

def centerSpread(s, i, i1):
    lenth = len(s)
    j = i1
    while i >= 0 and j < lenth:
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break
    return s[i + 1:j]


def longestPalindrome(s):
    lenth = len(s)
    if lenth < 2:     #字符串长度小于2的情况
        return s
    max_lenth = 1
    res = s[0]
    for i in range(lenth - 1):
        odd = centerSpread(s,i,i)
        even = centerSpread(s,i,i+1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > max_lenth:
            max_lenth = len(maxstr)
            res = maxstr
    return res
print(longestPalindrome("011101112"))



