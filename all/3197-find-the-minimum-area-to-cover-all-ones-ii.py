'''
2025/08/23 daily challenge

enumeration approach

learnt from official editorial:
https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/editorial/#approach-enumerate
'''


class Solution:
    def rotate(self, grid):
        # rotate grid by 90 degrees counterclockwisely
        m, n = len(grid[0]), len(grid)
        rect = [[0] * n for _ in range(m)]

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                rect[m - j - 1][i] = v

        return rect

    def simple_minSum(self, grid, x0, x1, y0, y1):
        # find minimum sum for a rectangle within specified boundaries
        min_i, max_i = len(grid), 0
        min_j, max_j = len(grid[0]), 0

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                if grid[i][j]:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)
        if min_i > max_i:
            return float('inf')
        return (max_i - min_i + 1) * (max_j - min_j + 1)

    def solve(self, grid):
        m, n = len(grid[0]), len(grid)
        ret = m * n

        # 3 types of separation
        for i in range(n - 1):
            for j in range(m - 1):
                # 1 upper rect + 2 bottom rects
                ret = min(ret,
                          self.simple_minSum(grid, 0, i, 0, m - 1) + \
                          self.simple_minSum(grid, i + 1, n - 1, 0, j) + \
                          self.simple_minSum(grid, i + 1, n - 1, j + 1, m - 1))
                # 2 upper rects + 1 bottom rect
                ret = min(ret,
                          self.simple_minSum(grid, 0, i, 0, j) + \
                          self.simple_minSum(grid, 0, i, j + 1, m - 1) + \
                          self.simple_minSum(grid, i + 1, n - 1, 0, m - 1))
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # 3 horizontal rects
                ret = min(ret,
                          self.simple_minSum(grid, 0, i, 0, m - 1) + \
                          self.simple_minSum(grid, i + 1, j, 0, m - 1) + \
                          self.simple_minSum(grid, j + 1, n - 1, 0, m - 1))
        return ret

    def minimumSum(self, grid: List[List[int]]) -> int:
        # rotated for another 3 types of separation
        grid2 = self.rotate(grid)
        return min(self.solve(grid), self.solve(grid2))

