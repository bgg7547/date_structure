#  有序数组  (对撞指针)  无序 ：先排序
# def twoSum(nums,target):
#     head = 0
#     tail = len(nums) - 1
#     while head < tail:
#         twosum = nums[head] + nums[tail]
#         if  twosum == target:
#             print(nums[head],nums[tail])
#             head += 1
#             tail -= 1
#         else:
#             if twosum < target:
#                 head += 1
#             else:
#                 tail -= 1

# 哈希算法
def twoSum(nums,target):
    num_dic = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in num_dic:
            print(nums[i],temp)
            return [i,num_dic[temp]]
        else:
            num_dic[nums[i]] = i
print(twoSum([1,2,4,7,11,15],9))