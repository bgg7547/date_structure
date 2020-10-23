def sort(nums):
    left = 0
    right = len(nums) - 1
    mid = 0
    while mid < right:
        if nums[mid] == 0:
            nums[mid],nums[left] = nums[left], nums[mid]
            left += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid],nums[right] = nums[right],nums[mid]

            right -= 1
        else:
            mid += 1
    return nums
print(sort([1,0,2,1,0,2]))