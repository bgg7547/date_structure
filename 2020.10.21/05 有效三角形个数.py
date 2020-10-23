# # 611
# def validTriangle(nums):
#     nums.sort()
#     count = 0
#     for i in range(2,len(nums)):
#         left = 0
#         right = i - 1
#         while left < right:
#             if nums[left] + nums[right] > nums[i]:
#                 count += right - left
#                 right -= 1
#             else:
#                 left += 1
#     return count
# print(validTriangle([2,2,3,4]))


def validTriangle(nums):
    nums.sort()
    count = 0
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[i] > nums[right]:
                count += right - left + 1
                right -= 1
            else:
                left += 1
    return count


