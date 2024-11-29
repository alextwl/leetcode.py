'''
2024/11/29 daily challenge

Dijkstra's algorithm approach
'''


import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # corner case: we cannot leave starting point
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        term_node = (m - 1, n - 1)

        min_time = [[float('inf')] * n for _ in range(m)]

        h = [(0, 0, 0)]  # (time_elapsed, x, y)

        while h:
            time_elapsed, x, y = heapq.heappop(h)

            if min_time[x][y] <= time_elapsed:
                continue
            min_time[x][y] = time_elapsed

            if (x, y) == term_node:
                break

            time_elapsed += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < m and 0 <= dy < n:
                    time_required = grid[dx][dy]
                    if time_required <= time_elapsed:
                        heapq.heappush(h, (time_elapsed, dx, dy))
                    else:
                        # go to previous cell back and forth (add multiples of 2 steps)
                        # until the elapsed time satisfies the requirement of the next cell
                        new_time = time_elapsed + (((time_required - time_elapsed + 1) >> 1) << 1)
                        heapq.heappush(h, (new_time, dx, dy))

        if min_time[-1][-1] == float('inf'):
            return -1

        return min_time[-1][-1]

