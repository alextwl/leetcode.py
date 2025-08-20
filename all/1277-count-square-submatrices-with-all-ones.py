'''
2024/10/27 daily challenge
2025/08/20 daily challenge

dynamic programming approach (top-down ver)

learnt from official solution:
https://leetcode.com/problems/count-square-submatrices-with-all-ones/solution/
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

            # count additional squares with the current cell
            xy1 = count(x, y+1)
            x1y1 = count(x+1, y+1)
            x1y = count(x+1, y)
            return 1 + min(xy1, x1y1, x1y)  # itself + additionals

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += count(i, j)

        return ans


'''
dynamic programming approach (bottom-up ver)
'''


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    count = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])
                    dp[i+1][j+1] = count
                    ans += count
        return ans

