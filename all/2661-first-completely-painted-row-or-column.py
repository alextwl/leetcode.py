'''
2025/01/20 daily challenge

counter approach
'''


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rc = dict()
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                rc[v] = (i, j)

        m, n = len(mat), len(mat[0])
        # remaining number of unpainted cells in each row & column
        cnt_row = [n] * m
        cnt_col = [m] * n

        for k, v in enumerate(arr):
            i, j = rc[v]
            cnt_row[i] -= 1
            if not cnt_row[i]:
                return k
            cnt_col[j] -= 1
            if not cnt_col[j]:
                return k
        # undefined behavior
        return -1

