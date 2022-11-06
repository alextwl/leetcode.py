'''
dynamic programming approach

similar to problem 931.

start from the second row, add min(adjacent cells of upper row) to current cell,
finally the minimum value of last row is the minimum path sum.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        for i in range(1, n):
            for j in range(0, i+1):  # derive the width of current row from the height i.
                # be careful of the boundary check, the width of upper row is always shorter than current row
                triangle[i][j] += min(triangle[i-1][k] for k in range(j-1, j+1) if 0 <= k < i)        
        return min(triangle[-1])
