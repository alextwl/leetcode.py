'''
iteration + in-place approach

time=O(mn), space=O(1)
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroize_1st_row = False
        zeroize_1st_col = False

        '''
        inevitably we need to iterate the entire matrix first.
        if a zero cell was found, set the first cell of its row and col to zero.
        (as in-place sets of zero rows & zero cols.)
        '''
        for i, row_list in enumerate(matrix):
            for j, val in enumerate(row_list):
                if not val:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    # check if we need to zeroize the entire first row or first column later.
                    if i == 0:
                        zeroize_1st_row = True
                    if j == 0:
                        zeroize_1st_col = True

        '''
        set zeroes in-place according to cells of first row & first col
        (but without overwrite the first row & the first col)
        '''
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(1, len(matrix)):
                    matrix[row][col] = 0

        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(1, len(matrix[0])):
                    matrix[row][col] = 0
        
        '''
        overwrite the first row or the first column if necessary
        '''
        if zeroize_1st_row:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        if zeroize_1st_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        
        return

