'''
2023/12/10 daily challenge

just transpose the matrix by iteration.
'''


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        trans = [[None] * m for _ in range(n)]

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                trans[j][i] = val

        return trans

