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

