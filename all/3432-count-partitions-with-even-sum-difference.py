'''
2025/12/05 daily challenge
'''


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        ans = 0
        for v in nums[:-1]:
            left -= v
            right += v
            if (right - left) & 1 == 0:
                ans += 1
        return ans

