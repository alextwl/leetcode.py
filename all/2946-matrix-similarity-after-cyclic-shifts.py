'''
2026/03/27 daily challenge

simulation approach
'''


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k = k % n
        for i, row in enumerate(mat):
            if i & 1:
                # odd-indexed rows
                new_row = row[n-k:] + row[:n-k]
            else:
                # even-indexed rows
                new_row = row[k:] + row[:k]
            if row != new_row:
                return False
        return True

