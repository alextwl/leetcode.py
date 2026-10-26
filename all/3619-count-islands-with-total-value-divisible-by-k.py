'''
2026/10/26 daily challenge

depth first search approach
'''


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not(0 <= i < m and 0 <= j < n):
                return 0
            if not grid[i][j]:
                return 0

            # we summarize only the remainders,
            # no need to deal with big numbers later.
            val = grid[i][j] % k
            grid[i][j] = 0  # visited
            return val + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        islands = 0
        for x, row in enumerate(grid):
            for y in range(n):
                if row[y] and dfs(x, y) % k == 0:
                    islands += 1
        return islands

