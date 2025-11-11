'''
2025/11/11 daily challenge

bottom-up dynamic programming approach
'''


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            # reverse loop: avoid duplicate picks in the same iteration
            # (i.e. pick strs[k] up twice in dp[i][j])
            # see 0/1 knapsack problem
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones -1, -1):
                    dp[i][j] = max(dp[i-zeros][j-ones] + 1, dp[i][j])

        return dp[-1][-1]

