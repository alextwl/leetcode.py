'''
2024/08/09 daily challenge

simulation approach
'''


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        rows = iter(grid)

        row0 = next(rows)
        row1 = next(rows)

        col_prefix = [i+j for i, j in zip(row0, row1)]

        row_prefix0 = [i+j+k for i, j, k in zip(row0[:-2], row0[1:-1], row0[2:])]
        row_prefix1 = [i+j+k for i, j, k in zip(row1[:-2], row1[1:-1], row1[2:])]

        distinct_set = set(range(1,10))
        
        ans = 0
        for row2 in rows:
            for i, v in enumerate(row2):
                col_prefix[i] += v
            row_prefix2 = [i+j+k for i, j, k in zip(row2[:-2], row2[1:-1], row2[2:])]

            # check row & column sums
            for i, (x, y, z) in enumerate(zip(row_prefix0, row_prefix1, row_prefix2)):
                if not (x == y == z):
                    continue
                if not (x == col_prefix[i] == col_prefix[i+1] == col_prefix[i+2]):
                    continue
                # check diagnoal
                d1 = row0[i] + row1[i+1] + row2[i+2]
                d2 = row0[i+2] + row1[i+1] + row2[i]
                if not (x == d1 == d2):
                    continue
                # check if filled with distinct numbers from 1 to 9
                if set(row0[i:i+3] + row1[i:i+3] + row2[i:i+3]) != distinct_set:
                    continue
                # a magic square found
                ans += 1

            # prepare for next round
            for i, v in enumerate(row0):
                col_prefix[i] -= v
            row0, row1 = row1, row2
            row_prefix0, row_prefix1 = row_prefix1, row_prefix2

        return ans

