'''
2026/03/21 daily challenge

in-place value swap
'''


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for dx in range(k // 2):
            x0, x1 = x + dx, x + k - 1 - dx
            for yy in range(y, y + k):
                grid[x0][yy], grid[x1][yy] = grid[x1][yy], grid[x0][yy]
        return grid

