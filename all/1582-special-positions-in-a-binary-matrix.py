'''
2023/12/13 daily challenge

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

