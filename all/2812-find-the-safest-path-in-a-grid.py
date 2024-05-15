'''
2024/05/15 daily challenge

level order traversal + modified Dijkstra's + greedy method approach

learnt from official solution 2:
https://leetcode.com/problems/find-the-safest-path-in-a-grid/solution/
'''

import collections
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            # shortcut: start or end point contains a thief
            return 0
        
        n = len(grid)
        
        # 1st stage
        # BFS from all thieves
        q = collections.deque()
        
        # convert cell values to the safest factors.
        # queue thieves with zeroed value, mark non-thief cell to -1 (unvisited)
        for i, row in enumerate(grid):
            for j in range(n):
                if row[j]:
                    q.append((i, j))
                    row[j] = 0
                else:
                    row[j] = -1
        
        # run BFS (level order)
        lv = 1  # next level (== distance to the nearest thief)
        while q:
            width = len(q)
            for _ in range(width):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx += x
                    dy += y
                    if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == -1:
                        grid[dx][dy] = lv
                        q.append((dx, dy))
            lv += 1

        # 2nd stage
        # modified Dijkstra's algorithm
        h = [(-grid[0][0], 0, 0)]  # max heap, (path's manhattan distance to thief, x, y)
        grid[0][0] = -1  # **visited**
        
        end_point = (n - 1, n - 1)

        while h:
            path_dist, x, y = heapq.heappop(h)
            
            if (x, y) == end_point:
                return -path_dist
            
            # queue neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] != -1:
                    # the manhattan distance of path is to the **nearest** thief, try to minimize it for the path.
                    next_path_dist = min(-path_dist, grid[dx][dy])
                    heapq.heappush(h, (-next_path_dist, dx, dy))
                    grid[dx][dy] = -1

        # undefined behavior: there must be a path from start to end.
        return -1

