'''
2025/08/27 daily challenge

recursive depth first search + memorization approach

learnt from official editorial:
https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/editorial/#approach-memoization-search

note **each** sequence makes **at most one** clockwise 90-degree turn,
we use k to maintain the count of remaining turns.
'''


import functools


# coordinate deltas in clockwise order
DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @functools.cache
        def dfs(x0, y0, di, k, target):
            # di: index of current direction
            # k: remaining count of turns
            x1 = x0 + DIRS[di][0]
            y1 = y0 + DIRS[di][1]

            if not(0 <= x1 < m and 0 <= y1 < n) or grid[x1][y1] != target:
                return 0

            # direction remains unchanged in the next step
            ret = dfs(x1, y1, di, k, 2 - target)

            if k:
                # make a turn in the next step
                k -= 1
                ret = max(ret, dfs(x1, y1, (di + 1) % 4, k, 2 - target))
            return ret + 1

        ans = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    for di in range(4):
                        ans = max(ans, dfs(i, j, di, 1, 2) + 1)

        return ans

