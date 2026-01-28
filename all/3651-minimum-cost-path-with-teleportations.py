'''
2026/01/28 daily challenge

bottom-up dynamic programming approach
'''


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        m1, n1 = m - 1, n - 1
        dp = [[float('inf')] * n for _ in range(m)]
        # sort coordinates by cell value
        cells = [(v, i, j) for i, row in enumerate(grid) for j, v in enumerate(row)]
        cells.sort()

        # iterate by count (0 to k) of transportations,
        # but the specific value of count is irrelevant.
        for _ in range(k + 1):
            j = 0
            min_cost = float('inf')
            # find minimum cost within the range of cells with same values
            for i, (v, x, y) in enumerate(cells):
                min_cost = min(min_cost, dp[x][y])
                if (i + 1) < len(cells) and \
                        grid[x][y] == grid[cells[i + 1][1]][cells[i + 1][2]]:
                    continue
                # we can teleport to cells[j] ~ cells[i] with no additional cost,
                # which is min_cost when arriving these cells previously.
                for l in range(j, i + 1):
                    dp[cells[l][1]][cells[l][2]] = min_cost
                j = i + 1

            # bottom-up dp: traverse from each cell normally
            for i in range(m1, -1, -1):
                for j in range(n1, -1, -1):
                    if i == m1 and j == n1:
                        dp[i][j] = 0
                        continue
                    if i < m1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + grid[i + 1][j])
                    if j < n1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + grid[i][j + 1])

        return dp[0][0]

