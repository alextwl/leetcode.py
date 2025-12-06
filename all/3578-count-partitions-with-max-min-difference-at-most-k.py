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
            # when i = 0, j = 0, dp[1] = 1, we have 1 valid partition:
            #     [9]
            # when i = 1, j = 1, dp[2] = 1, we have 1 valid partition:
            #   derived from dp[1]:
            #     [9], [4]
            # when i = 2, j = 1, dp[3] = dp[1] + dp[2] = 2,
            # we have 2 valid partitions:
            #   derived from dp[1]:
            #     [9], [4, 1]
            #   derived from dp[2]:
            #     [9], [4], [1]
            # when i = 3, j = 1, dp[4] = dp[1] + dp[2] + dp[3] = 4,
            # we have 4 valid partitions:
            #   derived from dp[1]:
            #     [9], [4, 1, 3]
            #   derived from dp[2]:
            #     [9], [4], [1, 3]
            #   derived from dp[3]:
            #     [9], [4, 1], [3]
            #     [9], [4], [1], [3]
            # when i = 4, j = 3, dp[5] is the final answer,
            # we have the following partitions with last segment appended:
            #   derived from dp[3]:
            #     [9], [4, 1], [3, 7]
            #     [9], [4], [1], [3, 7]
            #   derived from dp[4]:
            #     [9], [4, 1, 3], [7]
            #     [9], [4], [1, 3], [7]
            #     [9], [4, 1], [3], [7]
            #     [9], [4], [1], [3], [7]
            # so dp[5] = dp[3] + dp[4] = 6.
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % 1_000_000_007
            # a prefix sum of dp is made for optimization.
            # reduce the complexity from O(n**2) to O(n).
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % 1_000_000_007

        return dp[-1]


'''
monotonic stack + sliding window + dynamic programming approach

learnt from official editorial 2:
https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/editorial/#approach-2-monotonic-queue-optimization

it utilizes two monotonic deque for min/max value tracking in the sliding window.
also see problem 239 for practicing.
'''


import collections


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)

        dp[0] = 1
        prefix[0] = 1

        # monotonic stacks
        # nums[q_min[0]] is min val in the window
        q_min = collections.deque()
        # nums[q_max[0]] is max val in the window
        q_max = collections.deque()
        j = 0
        for i, v in enumerate(nums):
            while q_min and nums[q_min[-1]] >= v:
                # any value larger than nums[i] is no longer relevant
                q_min.pop()
            q_min.append(i)

            while q_max and nums[q_max[-1]] <= v:
                # any value smaller than nums[i] is no longer relevant
                q_max.pop()
            q_max.append(i)

            # slide the window
            while q_min and q_max and nums[q_max[0]] - nums[q_min[0]] > k:
                # we are shrinking the window from the left side,
                # but it doesn't always pop from these monotonic queues.
                # only if the index of min or max value was out of window,
                # it's popped.
                if q_min[0] == j:
                    q_min.popleft()
                if q_max[0] == j:
                    q_max.popleft()
                j += 1

            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % 1_000_000_007
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % 1_000_000_007

        return dp[-1]

