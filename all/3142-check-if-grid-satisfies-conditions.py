import itertools


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        # check if it's different from the cell to its right
        # we need to check one row only because another rule
        # asks for all rows to be equivalent.
        for c0, c1 in itertools.pairwise(grid[0]):
            if c0 == c1: return False
        # check if it's equal to the cell below it.
        for r0, r1 in itertools.pairwise(grid):
            for c0, c1 in zip(r0, r1):
                if c0 != c1: return False
        return True

