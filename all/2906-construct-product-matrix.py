'''
2026/03/24 daily challenge

suffix product approach

learnt from official editorial:
https://leetcode.com/problems/construct-product-matrix/editorial/#approach-suffix-product

suffix product multiplied by prefix product makes the answer.
suffix[i][j] * prefix[i][j] % 12345
'''


MOD = 12345


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        p = [[0] * n for _ in range(m)]

        suffix = 1
        for i in range(m - 1, -1, -1):
            row = grid[i]
            p_row = p[i]
            for j in range(n - 1, -1, -1):
                p_row[j] = suffix
                suffix = suffix * row[j] % MOD

        prefix = 1
        for i, row in enumerate(grid):
            p_row = p[i]
            for j, val in enumerate(row):
                p_row[j] = p_row[j] * prefix % MOD
                prefix = prefix * val % MOD

        return p

