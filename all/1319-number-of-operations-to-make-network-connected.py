'''
2023/03/23 daily challenge

Union-Find approach with path-splitting find()

Runtime 2576 ms Beats 5.7% :(
'''


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < (n-1):
            # not enough cables
            return -1
        
        # build Union-Find structure
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            # path splitting version
            while parent[x] != x:
                x, parent[x] = parent[x], parent[parent[x]]
            return x
        
        def union(x, y):
            # rank version
            x = find(x)
            y = find(y)

            if x == y:
                return
            
            if rank[x] < rank[y]:
                rank[x], rank[y] = rank[y], rank[x]
            
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
            return
        
        # union computers by each connection
        for a, b in connections:
            union(a, b)
        
        # count necessary modifications by unioning all groups
        ops = 0
        it = iter(set(parent))
        a = next(it)
        for b in it:
            if find(a) != find(b):
                # modify a connection to make a & b groups of computers connected
                union(a, b)
                ops += 1
            a = b

        return ops

