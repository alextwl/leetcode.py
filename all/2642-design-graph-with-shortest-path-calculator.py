'''
2023/11/11 daily challenge

Dijkstra's algorithm approach
'''

import collections
import heapq
import math


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = collections.defaultdict(dict)
        for u, v, cost in edges:
            self.g[u][v] = cost

    def addEdge(self, edge: List[int]) -> None:
        self.g[edge[0]][edge[1]] = edge[2]

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            # corner case: the source & destination are the same
            return 0

        # the shortest distance from node1 to key
        dist = {node1: 0}
        # min heap
        h = []
        for dest, cost in self.g[node1].items():
            heapq.heappush(h, (cost, dest))  # (the accumulated cost, the next stop)

        # dijkstra
        while(h):
            path_cost, node = heapq.heappop(h)
            if path_cost >= dist.get(node, math.inf):
                continue
            
            if node == node2:
                return path_cost
            
            dist[node] = path_cost
            
            for dest, cost in self.g[node].items():
                heapq.heappush(h, (path_cost + cost, dest))

        return -1

