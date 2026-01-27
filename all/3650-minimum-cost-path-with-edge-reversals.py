'''
2026/01/27 daily challenge

shortest path search (Dijkstra's algorithm) approach

treat reversed edges as doubled-cost edges in the same graph.

implementing minimum cost arriving each node also guarantees
each node's switch being used at most once and valid for single move.
'''


import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        target = n - 1

        # g[u] = [(v0, w0), (v1, w1) ...]
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            # reversed edge with doubled weight
            g[v].append((u, w * 2))
        
        min_cost = [float('inf')] * n
        h = [(0, 0, None)]  # (path_cost, node, prev_node)
        while h:
            cost, node, prev = heapq.heappop(h)
            if cost >= min_cost[node]:
                continue
            min_cost[node] = cost
            if node == target:
                return cost
            for adj, weight in g[node]:
                if adj == prev: continue
                heapq.heappush(h, (cost + weight, adj, node))
        return -1

