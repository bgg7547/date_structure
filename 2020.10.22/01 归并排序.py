# def merge(left, right):
#     res = []
#     while left and right:
#         if left[0] > right[0]:
#             res.append(right.pop(0))
#         else:
#             res.append(left.pop(0))
#     if left:
#         res.extend(left)
#     if right:
#         res.extend(right)
#     return res


def mergr_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left,right = nums[:mid], nums[mid:]
    return (merge(mergr_sort(left), mergr_sort(right)))



# 非python
def merge(left, right):
    res = [0] * 10
    m = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res[m] = right[j]
            m += 1
            j += 1
        else:
            res[m] = left[i]
            m += 1
            i += 1
    if left:
        res += left
    if right:
        res += right
    return res
print(mergr_sort([2,4,7,0,1,3,5]))

