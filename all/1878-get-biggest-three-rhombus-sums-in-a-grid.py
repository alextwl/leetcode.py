'''
2026/03/16 daily challenge

prefix sums + geometry approach

learnt from official editorial:
https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/editorial/#approach-enumerate-all-rhombuses

since the input grid was not big (<= 50),
it's possible to find all rhombuses and maintain top-3 sums.
'''


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # prefix sums of diagonal from top-left to bottom-right '\'
        pfx1 = [[0] * (n + 2) for _ in range(m + 1)]
        # prefix sums of diagonal from top-right to bottom-left '/'
        pfx2 = [[0] * (n + 2) for _ in range(m + 1)]
        for i, row in enumerate(grid, start=1):
            for j, val in enumerate(row, start=1):
                pfx1[i][j] = pfx1[i-1][j-1] + val
                pfx2[i][j] = pfx2[i-1][j+1] + val
        
        # biggest 3 distinct sums
        a0 = a1 = a2 = 0
        for i, row in enumerate(grid):
            for j, cell_val in enumerate(row):
                # zero-width rhombus with only current cell value
                if cell_val > a0:
                    a0, a1, a2 = cell_val, a0, a1
                elif cell_val != a0 and cell_val > a1:
                    a1, a2 = cell_val, a1
                elif cell_val != a0 and cell_val != a1 and cell_val > a2:
                    a2 = cell_val

                # iterate all possible diagonal length of a rhombus
                # with top cell of (i, j).
                for k in range(i + 2, m, 2):
                    #   0
                    #  / \
                    # 2   3
                    #  \ /
                    #   1
                    x0, y0 = i, j
                    x1, y1 = k, j
                    x2, y2 = (i + k) // 2, j - (k - i) // 2
                    x3, y3 = x2, j + (k - i) // 2

                    if y2 < 0 or y3 >= n:
                        break
                    
                    # a rhombus sum =
                    # upper-left edge + 
                    # upper-right edge +
                    # lower-right edge + 
                    # lower-left edge -
                    # 4 corner cells
                    curr = pfx2[x2 + 1][y2 + 1] - pfx2[x0][y0 + 2] + \
                        pfx1[x3 + 1][y3 + 1] - pfx1[x0][y0] + \
                        pfx1[x1 + 1][y1 + 1] - pfx1[x2][y2] + \
                        pfx2[x1 + 1][y1 + 1] - pfx2[x3][y3 + 2] - \
                        (cell_val + grid[x1][y1] + grid[x2][y2] + grid[x3][y3])
                    
                    if curr > a0:
                        a0, a1, a2 = curr, a0, a1
                    elif curr != a0 and curr > a1:
                        a1, a2 = curr, a1
                    elif curr != a0 and curr != a1 and curr > a2:
                        a2 = curr
        
        ans = [v for v in [a0, a1, a2] if v != 0]
        return ans

