'''
2024/07/27 daily challenge
2026/01/29 daily challenge

depth first search approach (for shortest path)
'''


import collections
import math


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # convert original/changed to graph
        g = collections.defaultdict(dict)
        for a, b, w in zip(original, changed, cost):
            g[a][b] = min(g[a].get(b, 1000001), w)

        # calculate shortest pathes from all originals to all changed
        min_dist = collections.defaultdict(dict)
        for start in g.keys():
            from_start = min_dist[start]
            # DFS
            stack = [(start, 0)]  # (node, path_len)
            while stack:
                node, path_len = stack.pop()
                if from_start.get(node, math.inf) <= path_len:
                    continue
                
                from_start[node] = path_len

                # note there might not have an edge from node to any destination.
                if node in g:
                    for child, w in g[node].items():
                        stack.append((child, path_len + w))

        # create new mapper with min cost
        mapper = {}
        for a, dest_costs in min_dist.items():
            for b, w in dest_costs.items():
                mapper[(a, b)] = w
        #print(str(mapper))

        ans = 0
        for pair in zip(source, target):
            if pair[0] == pair[1]:
                continue
            if pair not in mapper:
                return -1
            ans += mapper[pair]

        return ans


'''
Floyd-Warshall algorithm approach
'''


ASCII_A = ord('a')
INF = float('inf')


def c2idx(c):
    return ord(c) - ASCII_A


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[INF] * 26 for _ in range(26)]
        for u in range(26):
            dist[u][u] = 0
        for u, v, w in zip(map(c2idx, original), map(c2idx, changed), cost):
            dist[u][v] = min(dist[u][v], w)
        
        for k, k_to in enumerate(dist):
            for i, i_to in enumerate(dist):
                i_k = i_to[k]
                if i_k == INF:
                    continue
                for j in range(26):
                    i_k_j = i_k + k_to[j]
                    if i_to[j] > i_k_j:
                        i_to[j] = i_k_j
        ans = 0
        for u, v in zip(map(c2idx, source), map(c2idx, target)):
            w = dist[u][v]
            if w == INF:
                return -1
            ans += w
        return ans

