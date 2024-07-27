'''
2024/07/27 daily challenge

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

