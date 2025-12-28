'''
min heap + dynamic programming approach

use min heap to track maximum dp[j] for j in i < j <= i + k.
'''


import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # let dp[i] be max score starting at i (for nums[i:])
        # dp[i] = max(dp[j] for j in i < j <= min(n - 1, i + k))
        # use a min heap to track maximum dp[j] within the range.
        h = [(-nums[-1], 0)]  # min heap: (-score, rev index [..., 3, 2, 1, 0])

        it = enumerate(reversed(nums))
        score = next(it)[1]  # current dp value
        for i, v in it:
            j = i - k
            while h and h[0][1] < j:
                heapq.heappop(h)

            score = v - h[0][0]
            heapq.heappush(h, (-score, i))

        # note the actual answer is dp[0], not h[0].
        # the problem asks for standing at index 0 initially.
        return score

