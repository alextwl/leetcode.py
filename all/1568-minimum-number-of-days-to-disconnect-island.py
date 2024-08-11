'''
2024/08/11 daily challenge

depth first search approach (number of islands + brute force)
'''


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y, visited):
            if not (0 <= x < m and 0 <= y < n) or \
                    visited[x][y] or grid[x][y] == 0:
                # invalid or visited or water cell encountered
                return

            visited[x][y] = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                dfs(dx, dy, visited)

        def get_island_count():
            visited = [[False] * n for _ in range(m)]
            total_islands = 0
            for i in range(m):
                for j in range(n):
                    if not visited[i][j] and grid[i][j]:
                        dfs(i, j, visited)
                        total_islands += 1
            return total_islands

        # note the problem asks for exactly an island,
        # so if there're >1 or no islands then no need to disconnect.
        if get_island_count() != 1:
            return 0
        
        # try to flood each single land to test if we could disconnect the island
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    # water
                    continue
                
                # flood the land
                grid[i][j] = 0
                if get_island_count() != 1:
                    return 1
                # drain the water
                grid[i][j] = 1
        # we need to flood at least 2 land cells to disconnect the island
        return 2

