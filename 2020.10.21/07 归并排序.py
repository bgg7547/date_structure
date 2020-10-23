
# 归并   先拆 后合

# def merge(left, right):
#     res = []
#     while left and right:
#         if left[0] > right[0]:
#             res.append(right.pop(0))
#         else:
#             res.append(left.pop(0))
#     if left:
#         res += left
#     if right:
#         res += right
#     return res



def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]
    return merge(merge_sort(left), merge_sort(right))

# 指针版
def merge(left, right):
    res = []
    l = 0
    r = 0
    while l < len(left) and r < len((right)):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return res




print(merge_sort([5,8,4,2,6,9,2]))


