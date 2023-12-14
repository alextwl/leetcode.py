'''
2023/12/14 daily challenge

count only the number of ones in each row & column.
'''


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesRow = []
        onesCol = [0] * n
        
        for i, row in enumerate(grid):
            curr_ones = 0
            for j, val in enumerate(row):
                if val:
                    curr_ones += 1
                    onesCol[j] += 1
            onesRow.append(curr_ones)
        
        '''
        diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
                   = onesRowi + onesColj - (m - onesRowi) - (n - onesColj)
                   = 2 * (onesRowi + onesColj) - m - n
        '''
        diff = [[0] * n for _ in range(m)]
        mn = m + n
        for i, x in enumerate(onesRow):
            for j, y in enumerate(onesCol):
                diff[i][j] = 2 * (x + y) - mn

        return diff

