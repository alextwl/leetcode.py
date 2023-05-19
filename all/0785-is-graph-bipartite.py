'''
2023/05/19 daily challenge

Union find approach

the question asks for every edge in the graph
connects a node in set A and a node in set B,
we can sum up in several requirements:

(1) all v in graph[u] are in the same set.
(2) each edge's u and v cannot be in the same set.
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        # Union-find structure
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x > y:
                parent[x] = y
            else:
                parent[y] = x
        
        for u, vset in enumerate(graph):
            # union all v in graph[u]
            if not vset:
                # skip empty set
                continue
            it = iter(vset)
            v1 = next(it)
            for v in it:
                union(v1, v)
            
            # test if there's any v in the same set of u.
            for v in vset:
                if find(u) == find(v):
                    # the graph is *not* bipartite.
                    return False

        return True

