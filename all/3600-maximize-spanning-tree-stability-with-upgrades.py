'''
2026/03/12 daily challenge

Union find + binary search + minimum spanning tree (Kruskal's algorithm) approach

learnt from official editorial:
https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/editorial/#approach-binary-answer--minimum-spanning-tree
'''


class UnionFind:
    def __init__(self, parent):
        self.parent = parent
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if x < y:
            self.parent[y] = self.parent[x]
        else:
            self.parent[x] = self.parent[y]


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        if len(edges) < n - 1:
            # we need at least n-1 edges to connect all nodes
            return -1

        # classify edges by must        
        must_edges = []
        opt_edges = []
        for u, v, s, must in edges:
            if must:
                must_edges.append((u, v, s))
            else:
                opt_edges.append((u, v, s))

        if len(must_edges) > n - 1:
            # too many must edges.
            # we need exactly n-1 edges to connect all nodes.
            return -1

        # build initial template for Union-Find structure.
        # import all must edges.
        init_ans = 200000
        init_edge_count = len(must_edges)
        init_uf = UnionFind(list(range(n)))
        for u, v, s in must_edges:
            if init_uf.find(u) == init_uf.find(v):
                # cycle detected
                return -1
            init_uf.union(u, v)
            init_ans = min(init_ans, s)

        # sort optional edges by strength in descending order
        opt_edges.sort(key=lambda x: x[2], reverse=True)

        ans = -1
        # binary search the maximum possible stability
        left, right = 0, init_ans
        while left < right:
            mid = left + (right - left + 1) // 2
            # copy must-edge-only Union-Find instance
            uf = UnionFind(init_uf.parent[:])
            selected = init_edge_count
            doubled = 0

            # modified Kruskal's algorithm
            # it loops through edges by strength (weight) in descending order
            for u, v, s in opt_edges:
                if uf.find(u) == uf.find(v):
                    continue
                if s >= mid:
                    uf.union(u, v)
                    selected += 1
                elif doubled < k and s * 2 >= mid:
                    # the doubled strength should be >= target strength,
                    # or it's insufficient even if it's doubled.
                    uf.union(u, v)
                    selected += 1
                    doubled += 1
                else:
                    # insufficient strength, no need to check further.
                    break
                
                if selected == n - 1:
                    # selected edges are enough.
                    break

            if selected != n - 1:
                # insufficient edges, cannot connect all nodes.
                # we need to decrease the target.
                right = mid - 1
            else:
                # valid connections
                ans = left = mid
        # we need at least one spanning tree validated, or there's no answer.
        # that means we cannot simply return the left variable.
        return ans

