'''
2024/05/15 daily challenge
2026/07/01 daily challenge

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


'''
binary search + breadth first search approach

binary search safeness factors by validating if there's a path with the factor.

Runtime 2952ms, Beats 71.10%
'''


import collections


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            # corner case: thief at the start or the end.
            return 0

        n = len(grid)
        n1 = n - 1

        q0 = collections.deque()
        # remap thieves to 0, empty cells to -1.
        # queue thief coords.
        for i, row in enumerate(grid):
            for j in range(n):
                if row[j] == 1:
                    # thief
                    row[j] = 0
                    q0.append((i, j))
                else:
                    # empty cell
                    row[j] = -1

        # BFS
        while q0:
            width = len(q0)
            for _ in range(width):
                x, y = q0.popleft()
                curr_val = grid[x][y]
                for dx, dy in DIRS:
                    dx += x
                    dy += y
                    if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == -1:
                        # update manhattan distance (safe factor) to empty cell
                        grid[dx][dy] = curr_val + 1
                        q0.append((dx, dy))

        # binary search + BFS for a valid path again
        left = 0
        right = max(0, max(max(row) for row in grid))
        ans = -1
        terminal_min = min(grid[0][0], grid[-1][-1])

        def is_path_valid(min_factor):
            q = collections.deque()
            q.append((0, 0))

            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while q:
                x, y = q.popleft()
                if x == n1 and y == n1:
                    # destination reached, path is valid
                    return True
                for dx, dy in DIRS:
                    dx += x
                    dy += y
                    if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy] and grid[dx][dy] >= min_factor:
                        visited[dx][dy] = True
                        q.append((dx, dy))
            # path not found
            return False

        while left <= right:
            mid = left + (right - left) // 2
            if terminal_min >= mid and is_path_valid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

