# # 26给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# # 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
from typing import List
def t26(nums:List):
    slow = 0
    fast = 1         #找到和慢的不同元素
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1,nums

print(t26([0,0,1,1,1,2,2,3,3,4]))
#
#         # 2
# # def planB(nums):
# #     n = len(set(nums))
# #     i = 0
# #     while i < n -1:
# #         pass
#
# # 283 移动零  错误做法
# def move0(nums):
#     slow = 0
#     fast = 0
#     while fast <= len(nums)-1:
#         if nums[slow] == 0 and nums[len(nums) -1] != 0 or nums[len(nums) -1] == 0 and fast < len(nums)-1 and nums[slow] == 0:
#             while nums[fast] == 0 and  fast < len(nums)-1:
#                fast += 1
#             nums[slow],nums[fast] = nums[fast],nums[slow]
#         slow += 1
#         fast += 1
#     return nums,slow,fast
# print(move0([0,1,2,0,3]))

#  正确
# def move0(nums):
#     slow = 0
#     fast = 0
#     while fast < len(nums):
#         if nums[fast] == 0:
#             fast += 1
#         else:
#             nums[slow] = nums[fast]
#             fast += 1
#             slow += 1
#     for i in range(slow, len(nums)):
#         nums[i]=0
#     return nums
# print(move0([0,1,2,0,3]))

# t27
# slow = 0
# fast = 0
# while fast < len(nums):
#     if nums[fast] == val:
#         fast += 1
#     else:
#         nums[slow] = nums[fast]
#         fast += 1
#         slow += 1
# return slow


#80  给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#   26去重 相当于count = 1
# 最多为2 ： count = 2 的时候可以往下走  =1 的时候可以走

def quchon(nums):
    slow = 0
    count = 1
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
            nums[slow] = nums[fast]
            fast += 1
            count = 1
    return slow + 1


