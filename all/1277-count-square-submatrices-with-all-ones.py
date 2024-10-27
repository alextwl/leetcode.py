'''
2024/10/27 daily challenge

dynamic programming approach (top-down ver)
'''


import functools


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @functools.cache
        def count(x, y):
            if x >= m or y >= n:
                return 0
            if matrix[x][y] == 0:
                return 0

            xy1 = count(x, y+1)
            x1y1 = count(x+1, y+1)
            x1y = count(x+1, y)
            return 1 + min(xy1, min(x1y1, x1y))

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += count(i, j)

        return ans

