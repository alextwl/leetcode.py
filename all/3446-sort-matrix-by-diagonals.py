'''
2025/08/28 daily challenge
'''


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        arr = []  # diagonal stack

        # top-right triangle, non-decreasing
        for k in range(1, n - 1):
            for i in range(0, n - k):
                j = k + i
                arr.append(grid[i][j])
            arr.sort(reverse=True)
            for i in range(0, n - k):
                j = k + i
                grid[i][j] = arr.pop()

        # bottom-left triangle + middle, non-increasing
        for k in range(0, n - 1):
            for j in range(0, n - k):
                i = k + j
                arr.append(grid[i][j])
            arr.sort()
            for j in range(0, n - k):
                i = k + j
                grid[i][j] = arr.pop()

        return grid

