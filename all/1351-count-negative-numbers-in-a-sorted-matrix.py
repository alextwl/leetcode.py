'''
2023/06/08 daily challenge
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        negs = 0
        
        bound = n-1  # column index of the first non-negative number from right.
        for i, row in enumerate(grid):
            for j in range(bound, -1, -1):
                if row[j] >= 0:
                    # update the rightmost index to be checked in the next round.
                    bound = j
                    break
            else:
                # numbers of the entire row are negative, stop.
                negs += (m - i) * n
                break
            
            # count the negative part of row.
            negs += (n-1) - bound

        return negs

