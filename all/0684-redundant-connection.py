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


'''
Union find approach (rank ver)

use union find structure as disjoint set union and
find the edge that its two endpoints were already in the same component.
'''


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(a):
            if uf[a] != a:
                uf[a] = find(uf[a])
            return uf[a]

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return False
            if rank[a] > rank[b]:
                a, b = b, a
            rank[b] += 1
            uf[a] = b
            return True

        for u, v in edges:
            if not union(u, v):
                # the edge is guaranteed the latest because
                # all other edges in the cycle were joined to the component.
                return [u, v]

        # undefined behavior
        return -1

