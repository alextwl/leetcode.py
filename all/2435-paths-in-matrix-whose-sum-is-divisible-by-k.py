'''
2025/11/26 daily challenge

3-D dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/editorial/#approach-dynamic-programming

keep path counts for all remainders (0 ~ k-1) in each cell.
no doubt it uses lots of DP space but works.
'''


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]

        for i, row in enumerate(grid, start=1):
            for j, val in enumerate(row, start=1):
                curr_mod = val % k
                if i == 1 and j == 1:
                    # base case: top-left corner
                    dp[i][j][curr_mod] = 1
                    continue
                
                for target_rem in range(k):
                    prev_mod = (target_rem - curr_mod + k) % k
                    # inherit counts from upper and left cells
                    dp[i][j][target_rem] = (
                        dp[i - 1][j][prev_mod] + dp[i][j - 1][prev_mod]
                        ) % 1_000_000_007

        return dp[-1][-1][0]

