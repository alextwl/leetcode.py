'''
dynamic programming + sliding window approach

note if the total prizes of two overlapping segments was the answer,
we can also split it into two segments which are adjacent, non-overlapped,
and with the same number of total prizes.
'''


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        # dp[k] = max segment width in prizePositions[:k]
        dp = [0] * (n + 1)
        max_width = 0
        left = 0
        lval = prizePositions[0]
        for right, rval in enumerate(prizePositions):
            while rval - lval > k:
                while left < right and prizePositions[left] == lval:
                    left += 1
                lval = prizePositions[left]
            width = right - left + 1
            # inherit the previous best segment or pick the current one
            dp[right + 1] = max(dp[right], width)
            # maximize with the previous segment in prizePositions[:left]
            # plus the current segment
            max_width = max(max_width, dp[left] + width)
        return max_width

