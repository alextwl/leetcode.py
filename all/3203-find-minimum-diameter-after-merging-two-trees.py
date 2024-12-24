'''
2024/12/24 daily challenge

topological sort approach

note the path of the minimum possible diameter may fully reside
in tree 1 or tree 2 even if two trees are combined.
'''


import collections
import math


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def get_diameter(edges):
            n = len(edges) + 1
            g = [set() for _ in range(n)]

            for a, b in edges:
                g[a].add(b)
                g[b].add(a)

            indegree = [len(adjs) for adjs in g]

            q = collections.deque()
            for i, v in enumerate(indegree):
                if v == 1:
                    q.append(i)

            level_removed = 0
            remaining = n

            while remaining > 2:
                width = len(q)
                remaining -= width
                level_removed += 1

                for _ in range(width):
                    node = q.popleft()

                    for next_node in g[node]:
                        indegree[next_node] -= 1
                        if indegree[next_node] == 1:
                            q.append(next_node)
            # need an extra edge to combine two same-depth subtrees
            extra = 1 if remaining == 2 else 0
            return level_removed * 2 + extra

        dia1 = get_diameter(edges1)
        dia2 = get_diameter(edges2)
        return max(dia1, dia2, math.ceil(dia1 / 2) + 1 + math.ceil(dia2 / 2))

