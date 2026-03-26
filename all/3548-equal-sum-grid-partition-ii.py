'''
2026/03/26 daily challenge

rotate matrix + hash set + enumeration approach

learnt from official editorial:
https://leetcode.com/problems/equal-sum-grid-partition-ii/editorial/#approach-rotation-matrix--hash-table--enumeration-of-the-upper-matrix-sum

find a horizontal cut and rotate matrix for all cases.
'''


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # find the sum of the entire matrix
        total_sum = 0
        for row in grid:
            for val in row:
                total_sum += val
        
        # we always try to make a horizontal cut,
        # and also rotate the grid to cover vertical cuts.
        for rotate_count in range(4):
            if rotate_count > 0:
                # rotate 90 degree
                m, n = len(grid), len(grid[0])
                new_grid = [[0] * m for _ in range(n)]
                for i, row in enumerate(grid):
                    for j, val in enumerate(row):
                        new_grid[j][m - 1 - i] = val
                grid = new_grid

            m, n = len(grid), len(grid[0])

            curr_sum = 0
            if m < 2:
                # there's only one row, cannot make a horizontal cut, skip.
                continue
            if n == 1:
                # there's only one column.
                for i in range(m - 1):
                    curr_sum += grid[i][0]
                    diff = curr_sum * 2 - total_sum
                    # we can discard at most one cell which is the top cell
                    # or the bottom cell of the current submatrix.
                    if diff == 0 or diff == grid[0][0] or diff == grid[i][0]:
                        return True
                continue
            # for general cases
            seen = set()
            for i in range(m - 1):
                for j, val in enumerate(grid[i]):
                    curr_sum += val
                    seen.add(val)
                diff = curr_sum * 2 - total_sum
                if diff == 0:
                    # we can make a cut without discarding any cell.
                    return True
                if i == 0:
                    # only for the cut between grid[0] and grid[1].
                    if diff == grid[0][0] or diff == grid[0][n - 1]:
                        return True
                    continue
                if diff in seen:
                    # we can make a cut with discarding one cell.
                    return True
        return False

