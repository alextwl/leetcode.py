'''
2026/05/09 daily challenge

enumeration approach

flatten each layer to 1D array, rotate it, and write it back.
'''


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        for lv in range(0, min(m, n) // 2):
            arr = []

            # start from top-left to top-right
            i = lv
            for j in range(lv, n - lv - 1):
                arr.append(grid[i][j])
            j += 1
            # top-right to bottom-right
            for i in range(lv, m - lv - 1):
                arr.append(grid[i][j])
            i += 1
            # bottom-right to bottom-left
            for j in range(n - lv - 1, lv, -1):
                arr.append(grid[i][j])
            j -= 1
            # bottom-left to top-left
            for i in range(m - lv - 1, lv, -1):
                arr.append(grid[i][j])
            
            kmod = k % len(arr)
            if kmod == 0:
                continue
            # cyclically rotate in counter-clockwise direction
            arr = arr[kmod:] + arr[:kmod]

            # replace from top-left to top-right
            it = iter(arr)
            i = lv
            for j in range(lv, n - lv - 1):
                grid[i][j] = next(it)
            j += 1
            # top-right to bottom-right
            for i in range(lv, m - lv - 1):
                grid[i][j] = next(it)
            i += 1
            # bottom-right to bottom-left
            for j in range(n - lv - 1, lv, -1):
                grid[i][j] = next(it)
            j -= 1
            # bottom-left to top-left
            for i in range(m - lv - 1, lv, -1):
                grid[i][j] = next(it)

        return grid

