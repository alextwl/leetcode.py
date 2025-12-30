'''
2024/08/09 daily challenge
2025/12/30 daily challenge

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


'''
use additional properties of magic square

learnt from official editorial 2:
https://leetcode.com/problems/magic-squares-in-grid/editorial/#approach-2-check-unique-properties-of-magic-square

the sum of a magic square is fixed because each value is distinct
and the sum must be 1+2+3+...+9=45.

each row, column, and diagonal's sum must be 45/3 == 15.
valid 3-value sums are limited in the following combinations:
1+5+9, 1+6+8, 2+4+9, 2+5+8, 2+6+7, 3+4+8, 3+5+7, 4+5+6

thus we can find more properties of a magic square:
(1) the center must be a 5.
(2) each corner must be an even.
(3) each non-corner cell of border must be an odd.

and we can see the border is always in the sequence of
"2943816729438167" clockwise or anticlockwise,
started from any position of the border.
'''


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(x, y):
            if grid[x][y] & 1:
                # according to magic properties,
                # the value of top-left corner must be an even.
                return False

            # border sequence
            seq = "2943816729438167"
            rev_seq = "7618349276183492"

            # indices of a square:
            # 012
            # 345
            # 678
            border = []
            # border indices order by clockwise
            border_idx = [0, 1, 2, 5, 8, 7, 6, 3]
            for k in border_idx:
                v = grid[i + k // 3][j + (k % 3)]
                border.append(v)
            s = ''.join(map(str, border))
            return seq.find(s) != -1 or rev_seq.find(s) != -1

        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if isMagicSquare(i, j):
                    ans += 1
        return ans

