'''
2023/06/18 daily challenge

dynamic programming approach
'''

import functools


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @functools.cache
        def dfs(i, j):
            path_count = 1  # only grid[i][j] itself is also a valid path.
            
            for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                # search smaller neighbors
                pi, pj = i+x, j+y
                if (0 <= pi < m and 0 <= pj < n) and grid[pi][pj] < grid[i][j]:
                    path_count += dfs(pi, pj) % 1_000_000_007

            return path_count

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)

        return ans % 1_000_000_007

