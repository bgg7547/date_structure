
def partition(nums,start,end):
    pivot = nums[start]
    mark = start
    for i in range(mark + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[i], nums[mark] = nums[mark], nums[i]
    nums[start] = nums[mark]
    nums[mark] = pivot
    return mark

def quickSort(nums,start,end):
    if start >= end:
        return
    mid = partition(nums, start, end)
    quickSort(nums, start, mid - 1)
    quickSort(nums, mid + 1, end)
    return nums
print(quickSort([2,3,1,8,4,5],0,5))

