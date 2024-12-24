'''
2024/12/24 daily challenge

topological sort approach

note the path of the minimum possible diameter may fully reside in tree 1 or tree 2
even if two trees are combined.
'''


import collections


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def get_depth(edges):
            n = len(edges) + 1
            g = [set() for _ in range(n)]
            indegree = [0] * n

            for a, b in edges:
                g[a].add(b)
                g[b].add(a)
                indegree[a] += 1
                indegree[b] += 1

            q = collections.deque()
            for i, v in enumerate(indegree):
                if v == 1:
                    q.append(i)

            max_depth = [0] * n
            diameter = 0

            while q:
                node = q.popleft()
                if indegree[node] == 1:
                    next_node = g[node].pop()
                    indegree[node] = 0

                    g[next_node].remove(node)
                    indegree[next_node] -= 1
                    diameter = max(diameter, max_depth[next_node] + 1 + max_depth[node])
                    max_depth[next_node] = max(max_depth[next_node], max_depth[node] + 1)

                    if indegree[next_node] == 1:
                        q.append(next_node)

            return (max(max_depth), diameter)

        depth1, dia1 = get_depth(edges1)
        depth2, dia2 = get_depth(edges2)
        return max(dia1, dia2, depth1 + 1 + depth2)

