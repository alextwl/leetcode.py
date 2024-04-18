'''
2024/04/18 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()

        # search the beginning
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    q.append((i, j))
                    break
            if q:
                break
        else:
            # there's no such island.
            return 0

        perimeter = 0

        while q:
            x, y = q.popleft()
            
            if grid[x][y] != 1:
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j]:
                    if grid[i][j] == 1:
                        q.append((i, j))
                else:
                    perimeter += 1

            grid[x][y] = 2

        return perimeter

