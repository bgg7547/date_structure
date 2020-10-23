from randomList import randomList
# def selectSort(nums):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1,len(nums)):
#             if nums[i] > nums[j]:
#                 nums[i],nums[j] = nums[j],nums[i]
#         print(nums)
#     return nums
def selectSort(nums):
    for i in range(len(nums) - 1):
        minindex = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minindex]:
                minindex = j
        nums[i],nums[minindex] = nums[minindex],nums[i]
        print(nums)
a = randomList.randomList(10)
print(a)
# print(selectSort(a))
selectSort(a)