'''
2023/09/24 daily challenge

pascal's triangle approach
'''

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        note that query_row is 0-indexed.
        so row 0 has 1 glass, row 1 has 2 glasses, etc.
        '''
        tower = [[0.0] * i for i in range(1, query_row+2)]
        
        row_iter = iter(tower)
        prev_row = next(row_iter)
        
        # fill all champagne to (0, 0) cup
        prev_row[0] = poured * 1.0
        
        for next_row in row_iter:
            for j, val in enumerate(prev_row):
                if val > 1.0:
                    '''
                    excess (the part >1.0) liquid falls equally to
                    the glasses to the left and right of it.
                    '''
                    fall = (val - 1.0) / 2.0
                    next_row[j] += fall
                    next_row[j+1] += fall
            prev_row = next_row

        # always returns 1.0 if glass is full. no excess part.
        return min(1.0, prev_row[query_glass])

