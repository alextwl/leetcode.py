'''
2024/11/28 daily challenge

0-1 breadth first search approach
'''


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # the coordinate of the lower right corner (m - 1, n - 1).
        m1, n1 = len(grid) - 1, len(grid[0]) - 1
        term_node = (m1, n1)
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        q = collections.deque()
        q.append((0, 0, 0))  # (x, y, path_len)

        ans = float('inf')
        # 0-1 BFS
        while q:
            x, y, path_len = q.popleft()

            if visited[x][y]:
                continue
            visited[x][y] = True

            if (x, y) == term_node:
                ans = path_len
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx <= m1 and 0 <= dy <= n1 and not visited[dx][dy]:
                    # 0-1 switch
                    if grid[dx][dy]:
                        q.append((dx, dy, path_len + 1))
                    else:
                        q.appendleft((dx, dy, path_len))

        return ans


'''
Dijkstra's algorithm (min heap) approach

slower than 0-1 BFS.
'''


import collections
import heapq


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # the coordinate of the lower right corner (m - 1, n - 1).
        m1, n1 = len(grid) - 1, len(grid[0]) - 1
        term_node = (m1, n1)
        # the minimum distance from the upper left corner
        dist = collections.defaultdict(lambda: float('inf'))

        h = []
        h.append((0, 0, 0))  # (path_len, x, y)

        # 0-1 BFS
        while h:
            path_len, x, y = heapq.heappop(h)

            if dist[(x, y)] <= path_len:
                continue

            dist[(x, y)] = path_len

            if (x, y) == term_node:
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx <= m1 and 0 <= dy <= n1:
                    heapq.heappush(h, (path_len + grid[dx][dy], dx, dy))

        return dist[(m1, n1)]

