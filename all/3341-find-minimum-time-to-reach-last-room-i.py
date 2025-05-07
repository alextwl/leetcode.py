'''
2025/05/07 daily challenge

dijkstra's algorithm approach

note moveTime[x][y] is the minimum requirement before moving to that room,
when we move to it the minimum time is at least (moveTime[x][y] + 1).
'''


import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        n1, m1 = n - 1, m - 1
        min_time = [[float('inf')] * m for _ in range(n)]

        h = [(0, 0, 0)]  # (time travelled, x, y)
        while h:
            t, x, y = heapq.heappop(h)

            if t >= min_time[x][y]:
                continue

            min_time[x][y] = t
            if x == n1 and y == m1:
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < n and 0 <= dy < m:
                    # according to the examples we can wait for time elapsed
                    # until it meets moveTime.
                    heapq.heappush(h, (max(t, moveTime[dx][dy]) + 1, dx, dy))

        return min_time[-1][-1]

