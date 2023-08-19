'''
2023/08/19 daily challenge

minimum spanning tree (MST) question

Kruskal's algorithm + Union-find approach

learnt from official solution:
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/
'''

class UF:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        '''
        return True if we connected x & y.
        return False if x & y were **already** united.
        '''
        x, y = self.find(x), self.find(y)
        
        if x == y:
            return False
        
        if x > y:
            self.parent[x] = y
        else:
            self.parent[y] = x
        
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''
        indexed_edges[*] = (index in edges[], a, b, weight)
        sorted by weight in increasing order.
        '''
        indexed_edges = [(idx, *edge) for idx, edge in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[3])
        
        '''
        find MST weight.
        there may be multiple MSTs, but their weights should be the same.
        '''
        min_weight = 0
        uf = UF(n)
        for _, a, b, weight in indexed_edges:
            if uf.union(a, b):
                min_weight += weight
        
        '''
        find critical and pseudo-critical edges.
        since input n <= 100, running Kruskal's + Union-find many times is feasible.
        '''
        criticals = []
        pseudo_criticals = []
        
        for i, a, b, weight in indexed_edges:
            '''
            ignore the current edge and build an MST.
            '''
            added_vertices = 1
            weight_wo_i = 0  # MST weight without the current edge i.
            uf = UF(n)
            for j, x, y, jweight in indexed_edges:
                if i != j and uf.union(x, y):
                    weight_wo_i += jweight
                    added_vertices += 1
            '''
            if all vertices were not in the same graph (they were disconnected)
            or the weight is greater than the original MST,
            then this edge is a critical edge.
            '''
            if added_vertices < n or weight_wo_i > min_weight:
                criticals.append(i)
                # no need to determine if it's pseudo-critical.
                continue
            
            '''
            force add the current edge and build an MST.
            '''
            weight_w_i = weight  # MST weight with the current edge i.
            uf = UF(n)
            uf.union(a, b)  # force add the edge
            for j, x, y, jweight in indexed_edges:
                if i != j and uf.union(x, y):
                    weight_w_i += jweight
            '''
            if the weight is equal to the minimum weight,
            then this edge is pseudo-critical.
            '''
            if weight_w_i == min_weight:
                pseudo_criticals.append(i)

        return [criticals, pseudo_criticals]

