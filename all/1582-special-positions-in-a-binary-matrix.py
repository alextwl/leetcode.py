'''
2023/12/13 daily challenge
2026/03/04 daily challenge

counter approach
'''

import collections


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowCount, colCount = collections.defaultdict(int), collections.defaultdict(int)

        candidates = []
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val:
                    rowCount[i] += 1
                    colCount[j] += 1
                    candidates.append((i, j))
        
        ans = 0
        for i, j in candidates:
            if rowCount[i] == 1 and colCount[j] == 1:
                ans += 1

        return ans


'''
optimized brute force ver
'''


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_ones = [0] * m
        col_ones = [0] * n

        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val:
                    row_ones[i] += 1
                    col_ones[j] += 1

        ans = 0
        for i, row in enumerate(mat):
            if row_ones[i] != 1:
                # no need to check this row if no or more than one 1-cells.
                continue
            for j, val in enumerate(row):
                if val and col_ones[j] == 1:
                    ans += 1

        return ans

