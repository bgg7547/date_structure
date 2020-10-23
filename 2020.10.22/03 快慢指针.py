# 快指针去找不符合的，和慢的换

# 去重
def removal(nums):
    s = 0
    f = 1
    while f < len(nums):
        if nums[f] == nums[s]:
            f += 1
        else:
            s += 1
            nums[s] = nums[f]
            f += 1
    return s + 1,nums
# print(removal([1,1,1,2,2,3,4]))

# 移动0
def move0(nums):
    s = 0
    f = 0
    while f < len(nums):
        if nums[f] == 0:
            f += 1
        else:
            nums[s] = nums[f]
            s += 1
            f += 1
    for i in range(s,len(nums)):
        nums[i] = 0
    return nums
# print(move0([5,0,4,3,0,2,0,0]))

# 删除指定元素
def removedata(nums,data):
    s = 0
    f = 0
    while f < len(nums):
        if nums[f] == data:
            f += 1
        else:
            nums[s] = nums[f]
            s += 1
            f += 1
    return nums
print(removedata([2,3,4,5,3,3],3))