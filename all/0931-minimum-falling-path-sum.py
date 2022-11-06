'''
dynamic programming approach

think it reversely,
from the second row, add the min(previous elements from upper row) to each cell of rows recursively.

that is: matrix[i][j] = matrix[i][j] + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])

finally, the minimum value of the last row cells is the minimum sum of falling path.
'''

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(1, n):
            for j in range(0, n):
                matrix[i][j] += min(matrix[i-1][k] for k in range(j-1, j+2) if 0 <= k < n)  # oneliner with boundary check
        
        return min(matrix[-1])

