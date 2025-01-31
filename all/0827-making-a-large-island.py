'''
2025/01/31 daily challenge

union find approach
'''


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        uf = dict()
        rank = dict()

        def find(coord):
            if uf.setdefault(coord, coord) != coord:
                uf[coord] = find(uf[coord])
            return uf[coord]
        
        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if rank.setdefault(a, 1) >= rank.setdefault(b, 1):
                a, b = b, a
            uf[a] = b
            # combine dimensions of two islands
            rank[b] += rank[a]
        
        m, n = len(grid), len(grid[0])

        # scan islands
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        dx += r
                        dy += c
                        if 0 <= dx < m and 0 <= dy < n and grid[dx][dy]:
                            union((r, c), (dx, dy))
        ans = 0
        # scan waters
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if not val:
                    islands = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        dx += r
                        dy += c
                        if 0 <= dx < m and 0 <= dy < n and grid[dx][dy]:
                            islands.add(find((dx, dy)))
                    # maximize ans with adjacent islands plus current water
                    ans = max(ans, sum(rank.get(coord, 1) for coord in islands) + 1)
        return ans if ans else m * n


'''
depth first search approach

faster than union find ver
'''


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_to_dim = dict()
        m, n = len(grid), len(grid[0])

        def dfs(x, y, island_num):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = island_num
            return 1 + dfs(x - 1, y, island_num) + \
                dfs(x + 1, y, island_num) + \
                dfs(x, y - 1, island_num) + \
                dfs(x, y + 1, island_num)

        # scan islands
        k = 2  # island_num
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    island_to_dim[k] = dfs(r, c, k)
                    k += 1

        ans = 0
        # scan waters
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    adj_islands = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        dx += r
                        dy += c
                        if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] > 1:
                            adj_islands.add(grid[dx][dy])
                    ans = max(ans, 1 + sum(island_to_dim[adj] for adj in adj_islands))
        return ans if ans else m * n

