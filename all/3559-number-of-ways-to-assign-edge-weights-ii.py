'''
2026/06/12 daily challenge

lowest common ancestor + math approach

advanced ver of problem 3558
'''


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        m = len(edges).bit_length() + 1
        g = [[] for _ in range(n + 1)]  # 1-indexed

        distance = [0] * (n + 1)  # distance from root to x, 1-indexed
        # ancestor[x][k] = ancestor reached from x by 2**k steps upward
        ancestor = [[0] * m for _ in range(n + 1)]

        ans = []

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(x, src):
            ancestor[x][0] = src
            for y in g[x]:
                if y == src:
                    continue
                distance[y] = distance[x] + 1
                dfs(y, x)
        
        dfs(1, 0)  # traverse from root 1 (src == dummpy node 0)

        for i in range(1, m):
            for x in range(1, n + 1):
                ancestor[x][i] = ancestor[ancestor[x][i - 1]][i - 1]
        
        def lca(x, y):
            # get lowest common ancestor
            if distance[x] > distance[y]:
                x, y = y, x
            
            diff = distance[y] - distance[x]
            for i in range(m - 1, -1, -1):
                if diff & (1 << i):
                    y = ancestor[y][i]
            
            if x == y:
                return x

            for i in range(m - 1, -1, -1):
                if ancestor[x][i] != ancestor[y][i]:
                    x = ancestor[x][i]
                    y = ancestor[y][i]

            return ancestor[x][0]

        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                d = distance[u] + distance[v] - distance[lca(u, v)] * 2
                ans.append(pow(2, d - 1, 1_000_000_007))

        return ans

