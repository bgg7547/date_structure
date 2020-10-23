from typing import List


class Solution:
    def threesumclosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_value = abs(nums[0] + nums[1] + nums[2] - target)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if abs(res - target) < min_value:
                    min_value = abs(res - target)
                    result = res
                if res > target:
                    right -= 1
                elif res < target:
                    left += 1
                else:
                    return res
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.threesumclosest(nums=[1, 2, 4, 8, 16, 32, 64, 128], target=82)
    print(result)
