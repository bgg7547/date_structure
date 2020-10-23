# 有序数组去重
# def quchong(nums : list):
#     slow = 0
#     fast = 1
#     while fast < len(nums):
#         if nums[slow] == nums[fast]:
#             fast += 1
#         else:
#             slow += 1
#             nums[slow] = nums[fast]
#             fast += 1
#     return slow + 1
# print(quchong([1,1,1,2,2,3,4,4,5]))

# 有序数组去重最多留2个
def zuiduo2(nums):
    count = 1
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            count += 1
            if count == 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        else:
            slow += 1
            count = 1
            nums[slow] = nums[fast]
            fast += 1
    return nums[:slow + 1]
# print(zuiduo2([1,1,1,2,2,3,4,4,5]))

# 移动0
def move0(nums):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow,len(nums)):
        nums[i] = 0
    return nums
print(move0([0,0,1,1,0,2,0,3,0]))

#删除指定元素
# def pop_value(nums,value):
#     slow = 0
#     fast = 0
#     while fast < len(nums):
#         if nums[fast] == value:
#             fast += 1
#         else:
#             nums[slow] = nums[fast]
#             slow += 1
#             fast += 1
#     return nums[0:slow]
# print(pop_value([1,2,3,4,5,2,3,4],4))

