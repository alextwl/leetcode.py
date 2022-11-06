'''
space-optimized version of problem 118.

the problem requests for only the bottom row of pascal triangle.
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lastrow = [1]
        
        for rowIdx in range(1, rowIndex+1):
            row = [0] * (rowIdx+1)
            row[0] = row[-1] = 1
            for col in range(1, rowIdx):
                row[col] = lastrow[col-1] + lastrow[col]
            lastrow = row

        return lastrow
