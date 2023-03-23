'''
2023/03/23 daily challenge

depth first search approach

the idea is similar to problem 200 number of islands
'''


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < (n-1):
            # not enough cables
            return -1
        
        visited = [False] * n
        neighbor = [set() for _ in range(n)]
        for a, b in connections:
            neighbor[a].add(b)
            neighbor[b].add(a)
        
        '''
        use DFS to traverse a tree.
        the root of a tree will always return 1,
        and we can just count the number of 1's
        to calculate the number of necessary modifications
        '''
        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = True

            for child in neighbor[node]:
                dfs(child)
            
            return 1
        
        group_count = 0
        for i in range(n):
            group_count += dfs(i)
        
        return group_count - 1  # we need to modify n-1 connections in order to combine n groups


'''

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

