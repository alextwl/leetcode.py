'''
2026/05/24 daily challenge

depth first search + dynamic programming (memorization) approach

learnt from official editorial:
https://leetcode.com/problems/jump-game-v/editorial/#approach-memoization-search
'''


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n  # dp[i] = max(dp[j]) + 1

        def dfs(start):
            if dp[start] > 0:
                # visited
                return

            curr_val = arr[start]
            dp[start] = 1  # base: the start point is also a visited point.

            # left side
            i = start - 1
            while i >= 0 and start - i <= d and curr_val > arr[i]:
                dfs(i)
                dp[start] = max(dp[start], dp[i] + 1)
                i -= 1
            # right side
            i = start + 1
            while i < n and i - start <= d and curr_val > arr[i]:
                dfs(i)
                dp[start] = max(dp[start], dp[i] + 1)
                i += 1

        for st in range(n):
            dfs(st)

        return max(dp)

