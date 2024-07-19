'''
2024/07/19 daily challenge

exhaustive method approach
'''


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        row_min = []
        col_max = [0] * n

        for row in matrix:
            min_val = float('inf')
            for j, val in enumerate(row):
                min_val = min(min_val, val)
                col_max[j] = max(col_max[j], val)
            row_min.append(min_val)

        ans = []

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if row_min[i] == col_max[j] == val:
                    ans.append(val)

        return ans

