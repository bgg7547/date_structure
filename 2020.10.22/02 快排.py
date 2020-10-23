def swap(nums, p, q):
    nums[p], nums[q] = nums[q], nums[p]


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
            swap(nums, p, q)
    swap(nums, start, q)
    return q

def quickSort(nums,start,end):
    if start >= end:
        return
    mid = partition(nums,start,end)
    quickSort(nums, start, mid - 1)
    quickSort(nums, mid + 1, end)
    return nums

print(quickSort([4,7,3,5,6,2,3,1],0,7))
