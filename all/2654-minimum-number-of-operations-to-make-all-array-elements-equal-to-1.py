'''
2025/11/12 daily challenge

O(n**2) greedy method approach
'''


import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)
        if math.gcd(*nums) > 1:
            return -1

        n = len(nums)
        # find minimum length of interval with gcd == 1
        min_len = n
        for i, v in enumerate(nums):
            g = v
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    # we need (min_len - 1) ops to obtain a 1.
                    break
        # a 1 provided by previous interval,
        # we need (n - 1) ops to replace remaining values with 1.
        return min_len - 1 + n - 1

