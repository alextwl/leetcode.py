'''
2024/11/21 daily challenge

simulation approach
'''


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0: unguarded
        # 1: guarded
        # 2: guard
        # 3: wall
        grid = [[0] * n for _ in range(m)]

        for x, y in guards:
            grid[x][y] = 2
        for x, y in walls:
            grid[x][y] = 3

        def guard_cells(x, y):
            # up
            for col in range(y - 1, -1, -1):
                if grid[x][col] > 1:
                    break
                grid[x][col] = 1
            # down
            for col in range(y + 1, n):
                if grid[x][col] > 1:
                    break
                grid[x][col] = 1
            # left
            for row in range(x - 1, -1, -1):
                if grid[row][y] > 1:
                    break
                grid[row][y] = 1
            # right
            for row in range(x + 1, m):
                if grid[row][y] > 1:
                    break
                grid[row][y] = 1
            return

        for i, j in guards:
            guard_cells(i, j)

        # count unguarded
        unguarded = 0

        for r in grid:
            for cell in r:
                if cell == 0:
                    unguarded += 1

        return unguarded

