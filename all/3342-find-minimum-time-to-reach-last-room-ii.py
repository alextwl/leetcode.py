'''
2025/05/08 daily challenge

Dijkstra's algorithm approach
'''


import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        n1, m1 = n - 1, m - 1
        min_time = [[float('inf')] * m for _ in range(n)]

        h = [(0, 0, 0, 1)]  # (time travelled, x, y, parity)
        while h:
            t, x, y, parity = heapq.heappop(h)

            if t >= min_time[x][y]:
                continue

            min_time[x][y] = t
            if x == n1 and y == m1:
                break
            
            parity ^= 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < n and 0 <= dy < m:
                    tt = max(t, moveTime[dx][dy]) + 1 + parity
                    if tt >= min_time[dx][dy]: continue
                    heapq.heappush(h, (tt, dx, dy, parity))

        return min_time[-1][-1]

