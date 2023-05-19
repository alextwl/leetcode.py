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


'''
depth first search approach
'''


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        '''
        the party number of each node,
        there are only two party {1, -1}
        and all nodes are initialized with 0 (no party).
        '''
        parties = [0] * n
        def dfs(node, party):
            '''
            find if the node belongs to the specific party
            and search its childern.
            '''
            if parties[node] != 0:
                # the node is already assigned, verify its party.
                return parties[node] == party
            
            # assign the party
            # if there's conflict it shall be found when searching childern.
            parties[node] = party

            for v in graph[node]:
                # search the child with the opposite party.
                if not dfs(v, -party):
                    return False

            return True

        # search all nodes
        for u in range(n):
            # search u only if u didn't belong to any party.
            if parties[u] == 0:
                if not dfs(u, 1):
                    return False

        return True

