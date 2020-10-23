def threeSum(nums,target):
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums < target:
                left += 1
            elif sums > target:
                right -= 1
            else:
                return [nums[i],nums[left],nums[right]]
print(threeSum([1,3,5,2,8],8))

