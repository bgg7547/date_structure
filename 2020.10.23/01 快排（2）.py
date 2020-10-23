def sawp(nums, p, q):
    nums[p],nums[q] = nums[q], nums[p]

# 双指针
def partition(nums, start, end):
    poive = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < poive:
            p += 1
        while p <= q and nums[q] >= poive:
            q -= 1
        if p < q:
            sawp(nums, p, q)
    sawp(nums, start, q)
    return q

#单指针
def partition1(nums, start, end):
    poive = nums[start]
    mark = start
    for i in range(start + 1, end + 1):
        if nums[i] < poive:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[start] = nums[mark]
    nums[mark] = poive
    return mark


def quickSort(nums,start,end):
    if start >= end:
        return
    mid = partition1(nums, start, end)
    quickSort(nums, start, mid -1)
    quickSort(nums, mid + 1, end)
    return nums
print(quickSort([2,7,9,4,3,5],0,5))
