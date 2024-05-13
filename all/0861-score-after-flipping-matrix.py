'''
2024/05/13 daily challenge

bit manipluation approach

try to manipulate the largest number for each row/column.

use XOR to flip bits.
'''


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_vals = []

        # convert matrix to integers by row
        for row in grid:
            v = 0
            for j, bit in enumerate(row):
                if bit:
                    v += 1 << (n - j - 1)
            row_vals.append(v)

        # try to manipulate the max numbers.
        # just check the MSB to decide whether we should flip the row or not.
        msb_mask = 1 << (n - 1)
        xor_mask = (1 << n) - 1
        for i in range(m):
            if not(row_vals[i] & msb_mask):
                row_vals[i] ^= xor_mask

        # iterate each column except the first column and count 1's bit
        # to decide to flip the column or not.
        for j in range(1, n):
            mask = 1 << (n - j - 1)
            ones_count = 0
            for v in row_vals:
                if v & mask:
                    ones_count += 1
            # flip the column if the number of 1's bit was lesser than half of the number of rows
            if ones_count < ((m >> 1) + (m & 1)):
                for i in range(m):
                    row_vals[i] ^= mask

        return sum(row_vals)

