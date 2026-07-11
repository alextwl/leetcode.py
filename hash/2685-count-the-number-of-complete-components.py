'''
2025/03/22 daily challenge
2026/07/11 daily challenge

union find + counter approach

each vertex in the same component must have (number of component nodes - 1) indegrees
to make the component completed.
'''


import collections


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = [v for v in range(n)]
        rank = [0] * n

        def find(v):
            if uf[v] != v:
                uf[v] = find(uf[v])
            return uf[v]
        
        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if rank[a] >= rank[b]:
                uf[b] = uf[a]
                rank[a] += 1
            else:
                uf[a] = uf[b]
                rank[b] += 1

        indegree = [0] * n
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
            union(a, b)

        for v in range(n):
            find(v)

        comp_nodes = collections.Counter(uf)
        incompletes = set()
        for v, parent in enumerate(uf):
            if indegree[v] != comp_nodes[parent] - 1:
                incompletes.add(parent)

        return len(comp_nodes) - len(incompletes)


'''
count the frequency of sorted list of adjacent nodes
'''


import collections


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[i] for i in range(n)]  # graph for each node with self-loop
        ctr = collections.defaultdict(int)  # ctr[pattern of adjacent nodes] = freq

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        for x, adjs in enumerate(g):
            adjs.sort()
            key = tuple(adjs)  # convert to a hashable type
            ctr[key] += 1

        return sum(len(key) == freq for key, freq in ctr.items())

