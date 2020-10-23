# 16
def threeSumClose(nums,target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    closest = abs(nums[0] + nums[1] + nums[2] - target)
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            threesum = nums[i] + nums[left] + nums[right]
            if abs(target - threesum) < closest:
                res = threesum
                closest = abs(target - threesum)
            if threesum < target:
                left += 1
            elif threesum > target:
                right -= 1
            else:
                return threesum
    return res
print(threeSumClose([1,-1,0,-9],100))
