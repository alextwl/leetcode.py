'''
2022/10/31 daily challenge

intuitive approach

compare cell with the most top-left cell of the same diagonal.
'''

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        # list all top-left cells of every diagonal
        edge_cells = [(i, 0) for i in range(0, m)] + [(0, j) for j in range(1, n)]
        
        for i, j in edge_cells:
            val = matrix[i][j]
            x , y = i + 1, j + 1
            # check boundary and next cell of diagonal.
            while x < m and y < n:
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1

        # the matrix is Toeplitz.
        return True


'''
clever pythonic approach

learnt from official solution 2.

for all cells, just compare with top-left neighbor,
do *AND* with all its comparsion results plus always-true top-left edge cells.
'''

class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(x == 0 or y == 0 or matrix[x-1][y-1] == val
                   for x, row in enumerate(matrix)
                   for y, val in enumerate(row))
