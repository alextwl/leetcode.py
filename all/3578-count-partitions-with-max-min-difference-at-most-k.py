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
        # dp[i] = number of valid ways to partition for nums[:i]
        dp = [0] * (n + 1)
        # prefix[0..i] = prefix sums of dp[0..i]
        prefix = [0] * (n + 1)
        window = []  # window in non-decreasing order

        # base case: the partition is empty, which is valid.
        dp[0] = 1
        prefix[0] = 1

        j = 0
        for i, v in enumerate(nums):
            bisect.insort(window, v)
            while j < i and window[-1] - window[0] > k:
                del window[bisect.bisect_left(window, nums[j])]
                j += 1
            # nums[i] can be in a last segment which starts from or after nums[j].
            # so dp[i + 1] is actually dp[j] + dp[j + 1] + ... + dp[i].
            #
            # in Example 1 we have nums = [9,4,1,3,7] and k = 4,
            # when i = 2, j = 1, dp[3] = 2, we have 2 valid partitions:
            #     [9], [4], [1]
            #     [9], [4, 1]
            # when i = 3, j = 1, dp[4] = 4, we have 4 valid partitions:
            #     [9], [4, 1, 3]
            #     [9], [4], [1, 3]
            #     [9], [4], [1], [3]
            #     [9], [4, 1, 3]
            # when i = 4, j = 3, dp[5] is the final answer,
            # we have the following partitions with last segment appended
            #     derived from dp[3]:
            #     [9], [4], [1], [3, 7]
            #     [9], [4, 1], [3, 7]
            #     derived from dp[4]:
            #     [9], [4, 1, 3], [7]
            #     [9], [4], [1, 3], [7]
            #     [9], [4], [1], [3], [7]
            #     [9], [4, 1, 3], [7]
            # so dp[5] = dp[3] + dp[4] = 6.
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % 1_000_000_007
            # a prefix sum of dp is made for optimization.
            # reduce the complexity from O(n**2) to O(n).
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % 1_000_000_007

        return dp[-1]

