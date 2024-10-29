'''
2024/10/29 daily challenge

dynamic programming approach

note the problem asks for the maximum number of moves that **you can perform,**
**NOT** whether you can move the the cells in the last column or not.
'''


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp0 = [0] * m
        dp1 = [0] * m

        overall_max_moves = 0

        for j in range(n - 1):
            for i in range(m):
                dp1[i] = 0
            for i in range(m):
                curr = grid[i][j]
                y = j + 1
                if j > 0 and dp0[i] == 0:
                    # no previous moves reached the cell
                    continue
                for x in range(i - 1, i + 2):
                    if 0 <= x < m and grid[x][y] > curr:
                        dp1[x] = 1  # marks we can reach this cell
            dp0, dp1 = dp1, dp0
            if not any(dp0):
                # we cannot move to the current column, no need to search deeper.
                break
            overall_max_moves += 1

        return overall_max_moves

