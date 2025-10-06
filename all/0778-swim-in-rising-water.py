'''
2025/10/06 daily challenge

min heap approach
'''


import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        term = (n - 1, n - 1)
        h = [(grid[0][0], 0, 0)]   # (t, i, j), time requirement also applies to initial point.
        visited = dict()  # key=(i, j), val=min(t)

        while h:
            t, i, j = heapq.heappop(h)
            coord = (i, j)
            if visited.get(coord, 3000) <= t:
                continue
            if coord == term:
                return t
            visited[coord] = t

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += i
                dy += j
                if 0 <= dx < n and 0 <= dy < n:
                    # you can swim infinite distances in zero time.
                    heapq.heappush(h, (max(t, grid[dx][dy]), dx, dy))
        # undefined behavior
        return -1

