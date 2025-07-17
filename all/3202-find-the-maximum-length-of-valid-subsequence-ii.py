'''
2025/07/17 daily challenge

dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/editorial/#approach-dynamic-programming
'''


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp[x][y] = the length of subsequence ending with last two values modulo k.
        # so the modulo k of a subsequence likes this: [..., x, y, x, y].
        # the pair of dp[x][y] maintains the same remainder of (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ...
        dp = [[0] * k for _ in range(k)]

        ans = 0
        for y in nums:
            y %= k
            for x in range(k):
                # extend a subsequence: [..., x, y, x] + [y]
                dp[x][y] = dp[y][x] + 1
                ans = max(ans, dp[x][y])

        return ans

