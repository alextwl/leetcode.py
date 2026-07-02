'''
2026/07/02 daily challenge

breadth first search (0-1 BFS) approach

running Dijkstra's algorithm will TLE.
'''


import collections


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        m1, n1 = m - 1, n - 1

        q = collections.deque([(0, 0)])
        costs = [[float("inf")] * n for _ in range(m)]
        costs[0][0] = grid[0][0]

        while q:
            x, y = q.popleft()
            if x == m1 and y == n1:
                return True
            prev_cost = costs[x][y]

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < m and 0 <= dy < n:
                    curr_cost = prev_cost + grid[dx][dy]
                    if curr_cost >= health:
                        continue
                    if curr_cost < costs[dx][dy]:
                        costs[dx][dy] = curr_cost
                        # 0-1 BFS queueing
                        if grid[dx][dy]:
                            q.append((dx, dy))
                        else:
                            q.appendleft((dx, dy))
        return False

