'''
2025/08/22 daily challenge

linear search approach

find 4 corners of a rectangle

time=2600ms, Beats 92.81%
'''


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        x0 = x1 = None

        # find x
        for i, row in enumerate(grid):
            for v in row:
                if v:
                    x0 = i
                    break
            if x0 is not None:
                break
        for i in range(m - 1, x0 - 1, -1):
            for v in grid[i]:
                if v:
                    x1 = i
                    break
            if x1 is not None:
                break

        # find y
        y0, y1 = n, -1
        for i in range(x0, x1 + 1):
            row = grid[i]
            for j in range(y0):
                if row[j]:
                    y0 = j
                    break
            for j in range(n - 1, y1, -1):
                if row[j]:
                    y1 = j
                    break

        return (x1 - x0 + 1) * (y1 - y0 + 1)

