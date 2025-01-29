'''
2025/01/29 daily challenge

topological sort by removing acyclic parts approach

return cycle edge that occurs last in the input
'''


import collections


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        g = collections.defaultdict(set)
        edge_status = [True] * n
        edge2idx = dict()
        indegrees = [0] * (n + 1)  # nodes labeled from 1 to n

        for i, (a, b) in enumerate(edges):
            if a > b:
                a, b = b, a
            g[a].add(b)
            g[b].add(a)
            edge2idx[(a, b)] = i
            indegrees[a] += 1
            indegrees[b] += 1

        q = collections.deque([i for i, v in enumerate(indegrees) if v == 1])

        while q:
            a = q.popleft()
            b = g[a].pop()
            g[b].remove(a)
            # indegrees[a] = 0
            indegrees[b] -= 1
            if indegrees[b] == 1:
                q.append(b)
            if a > b:
                a, b = b, a
            edge_status[edge2idx[(a, b)]] = False

        # find answer that occurs last in the input
        for flag, edge in zip(reversed(edge_status), reversed(edges)):
            if flag:
                return edge

        # undefined behavior
        return -1

