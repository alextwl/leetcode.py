'''
2025/11/14 daily challenge

difference array + prefix sum approach
'''


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # build difference array for each rows
        mat = [[0] * n for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            col3 = col2 + 1
            for i in range(row1, row2 + 1):
                mat[i][col1] += 1
                if col3 < n:
                    mat[i][col3] -= 1

        # convert the arrays to prefix sum matrix
        for row in mat:
            for j in range(1, n):
                row[j] += row[j - 1]

        return mat

