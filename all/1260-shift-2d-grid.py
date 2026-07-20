'''
2026/07/20 daily challenge

flatten the grid, shift, and then convert to the new grid.
'''


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        if k == 0:
            return grid

        arr = []
        for row in grid:
            arr.extend(row)
        arr = arr[-k:] + arr[:-k]

        ans = []
        it = iter(arr)
        for _ in range(m):
            row = []
            for _ in range(n):
                row.append(next(it))
            ans.append(row)

        return ans

