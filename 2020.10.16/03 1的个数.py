# 191      1的个数
# n & n-1 每次消除最右边的1  (按位与)
def count1(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count
print(count1(11))