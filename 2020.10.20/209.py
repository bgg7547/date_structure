from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        cur = 0
        res = float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float("inf") else 0


if __name__ == '__main__':
    s = Solution()
    ss = 7
    nums = [2, 3, 1, 2, 4, 3]
    r = s.minSubArrayLen(ss, nums)
    print(r)
