'''
2025/03/23 daily challenge

Dijkstra's algorithm + dynamic programming approach
'''


import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        dp = [0] * n
        shortest = [float('inf')] * n
        dp[-1] = 1
        shortest[-1] = 0

        g = {u: dict() for u in range(n)}
        for u, v, t in roads:
            g[u][v] = t
            g[v][u] = t
        
        h = []  # [(path_len, dst, src)]
        u = n - 1
        for v, t in g[n-1].items():
            heapq.heappush(h, (t, v, u))
        
        while h:
            path_len, dst, src = heapq.heappop(h)

            if path_len > shortest[dst]:
                continue

            if path_len == shortest[dst]:
                dp[dst] = (dp[dst] + dp[src]) % 1_000_000_007
            else:
                # path_len < shortest[dst]
                shortest[dst] = path_len
                dp[dst] = dp[src]
                if dst > 0:
                    src = dst
                    for dst, t in g[src].items():
                        heapq.heappush(h, (path_len + t, dst, src))

        return dp[0]

