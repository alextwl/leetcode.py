'''
2025/12/06 daily challenge

dynamic programming + sliding window approach

learnt from official editorial:
https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/editorial/#approach-1-sliding-window--dynamic-programming
'''


import bisect


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # dp[i] = valid partitions in nums[:i]
        prefix = [0] * (n + 1)  # prefix[0..i] = prefix sums of dp[0..i]
        window = []  # window in non-decreasing order

        dp[0] = 1
        prefix[0] = 1

        j = 0
        for i, v in enumerate(nums):
            bisect.insort(window, v)
            while j < i and window[-1] - window[0] > k:
                del window[bisect.bisect_left(window, nums[j])]
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % 1_000_000_007
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % 1_000_000_007

        return dp[-1]

