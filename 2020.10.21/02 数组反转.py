def reverse(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l += 1
        r -= 1
