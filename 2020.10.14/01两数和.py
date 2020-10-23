
# 对撞指针
# def twoSum(nums,target):
#     l = 0
#     r = len(nums) - 1
#     while l < r:
#         he = nums[l] + nums[r]
#         if he < target:
#             l += 1
#         elif he > target:
#             r -= 1
#         else:
#             return [l,r]

# 哈希值
# def twoSum(nums,target):
#     sum_dic = {}
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         if temp in sum_dic:
#             return [i,sum_dic[temp]]
#         else:
#             sum_dic[nums[i]] = i
# print(twoSum([1,2,4,5,7],8))

# #暴力
# def twoSum(nums,target):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#

