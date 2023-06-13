'''
2023/06/13 daily challenge

hash approach

find all pairs where row-array grid[i] == column-array list(zip(*grid))[j]
'''

import collections


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # rotate the grid to make a copy with column-array grid
        # and hash the column arrays
        # counter[array tuple] = the number of the same column arrays
        counter = collections.defaultdict(int)
        for arr in zip(*grid):
            counter[arr] += 1

        ans = 0
        # compare each row with all columns and count.
        for arr in grid:
            ans += counter[tuple(arr)]

        return ans

