# def countSort(nums):
#     countlist = [0] * (max(nums) + 1)
#     for i in nums:
#         countlist[i] += 1
#     res = []
#     for j in range(len(countlist)):
#         res += [j] * countlist[j]
#     return res

def countSort(nums):
    dic = {}
    for i in nums:
        dic[i] = nums.count(i)
    return dic


print(countSort([9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]))



