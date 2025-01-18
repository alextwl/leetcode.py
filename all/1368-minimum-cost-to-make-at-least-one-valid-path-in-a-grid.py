'''
2025/01/18 daily challenge

breadth first search approach

convert the grid to a weighted graph and run BFS.
'''


import collections


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        g = dict()
        for i, row in enumerate(grid):
            for j, arrow in enumerate(row):
                g[(i, j)] = curr_node = dict()
                for k, dx, dy in [(1, 0, 1), (2, 0, -1), (3, 1, 0), (4, -1, 0)]:
                    dx += i
                    dy += j
                    if not (0 <= dx < m and 0 <= dy < n):
                        continue
                    curr_node[(dx, dy)] = 0 if k == arrow else 1

        dist = [[10000] * n for _ in range(m)]

        q = collections.deque()
        q.append((0, 0, 0))  # (path_len, i, j)

        while q:
            path_len, i, j = q.popleft()
            if path_len >= dist[i][j]:
                continue
            dist[i][j] = path_len
            for (x, y), weight in g[(i, j)].items():
                q.append((path_len + weight, x, y))

        return dist[-1][-1]

