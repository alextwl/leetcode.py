'''
2025/03/28 daily challenge

sorting + min heap approach

proceed queries in sorted order and search the grid by heap gradually.
'''


import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        query_idx = sorted([(v, i) for i, v in enumerate(queries)])
        ans = [0] * len(queries)

        visited = [[False] * n for _ in range(m)]
        points = 0  # a dp space for points earned.
        # start from top-left corner
        h = [(grid[0][0], 0, 0)]  # min-heap: (cell value, x, y)
        visited[0][0] = True

        for q_val, i in query_idx:
            # earn points for cells if its value was smaller than q_val
            while h and h[0][0] < q_val:
                _, x, y = heapq.heappop(h)
                # the current cell's value is strictly smaller than the query,
                # we can earn this point and visit adjacent cells.
                points += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx += x
                    dy += y
                    if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy]:
                        heapq.heappush(h, (grid[dx][dy], dx, dy))
                        visited[dx][dy] = True
            ans[i] = points
        return ans

