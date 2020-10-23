from typing import List

def threeSum(self, nums: List[int]):
    for a in range(len(nums)):
        target = 0 - nums[a]
        for i in range(a + 1,len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [a,i, j]

