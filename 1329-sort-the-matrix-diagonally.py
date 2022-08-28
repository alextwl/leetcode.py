'''
2022/08/29 daily challenge
'''

import collections

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        d = collections.defaultdict(list)
        
        # each cell of a diagonal line has the same difference of i-j.
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        
        for diaglist in d.values():
            diaglist.sort(reverse=1)  # for later popping from descending order (because we iterate (m,n) from (0,0))
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop()
        
        return mat
