'''
shortest path (Dijkstra's algorithm) + union-find approach

use disjoint set to verify the reachability between
player and free cells near the box.

note we cannot prevent from revisiting a cell, in some situations
we need to revisit cells to push box to the target in a roundabout way.
complicated structure for minimum path length with player's position used.

Runtime=787ms, Beats 5.19%
'''


import collections
import heapq


class DSU:
    def __init__(self, grid, box):
        self.grid = grid
        self.bx = box[0]
        self.by = box[1]
        self.m = len(grid)
        self.n = len(grid[0])
        self.parent = []  # union-find parent structure, uninitialized

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u > v:
            self.parent[v] = u
        elif u < v:
            self.parent[u] = v
    
    def reset(self):
        self.parent = list(range(self.m * self.n))
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell != '#' and (i != self.bx or j != self.by):
                    cell_idx = i * self.n + j
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        dx += i
                        dy += j
                        if 0 <= dx < self.m and 0 <= dy < self.n and \
                                self.grid[dx][dy] != '#' and \
                                (dx != self.bx or dy != self.by):
                            self.union(cell_idx, dx * self.n + dy)


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # min_moves[(box_x, box_y, player_x, player_y)]
        min_moves = collections.defaultdict(lambda: 10000)

        h = []  # min_heap: (path_sum, x, y)
        box = None
        player = None
        target = None

        # search 'B'
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 'B':
                    box = (i, j)
                elif cell == 'T':
                    target = (i, j)
                elif cell == 'S':
                    player = (i, j)

        # union-find check for reachability
        uf = DSU(grid, box)
        h.append((0, box[0], box[1], player[0], player[1]))

        while h:
            path_sum, x, y, px, py = heapq.heappop(h)

            if path_sum >= min_moves[(x, y, px, py)]:
                continue
            min_moves[(x, y, px, py)] = path_sum

            # reset union-find structure with new box coord
            uf.bx = x
            uf.by = y
            uf.reset()
            player_idx = px * n + py

            path_sum += 1
            # check if we could move to 4 directions
            # (dx, dy): next cell to move
            # (rdx, rdy): cell in the counterdirection.
            for dx, dy, rdx, rdy in [(-1, 0, 1, 0),
                                     (1, 0, -1, 0),
                                     (0, -1, 0, 1),
                                     (0, 1, 0, -1)]:
                dx, dy = dx + x, dy + y
                rdx, rdy = rdx + x, rdy + y
                if (0 <= rdx < m and 0 <= rdy < n and grid[rdx][rdy] != '#') and \
                        (0 <= dx < m and 0 <= dy < n and grid[dx][dy] != '#'):
                    # check reachability from player to counterdirection cell
                    rd_idx = rdx * n + rdy
                    if uf.find(rd_idx) != uf.find(player_idx):
                        continue
                    # check if next stop is target
                    if grid[dx][dy] == 'T':
                        return path_sum
                    # box moved to (dx, dy), player moved to (x, y)
                    heapq.heappush(h, (path_sum, dx, dy, x, y))
        return -1

