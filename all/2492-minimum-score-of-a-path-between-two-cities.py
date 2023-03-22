'''
2023/03/22 daily challenge

Union-find approach

The problem actually asks for **the minimum distance** of an edge
on the path between city 1 and city n.

Since the constraints guarantee there's at least one path between 1 and n,
we need to find an edge within a graph which contains 1 and n
but the edge is not necessarily on the shortest path between 1 and n.
'''

import collections


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = dict()

        def find(city):
            if uf.setdefault(city, city) != city:
                uf[city] = uf[uf[city]]
            return uf[city]
        
        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a < root_b:
                uf[root_b] = root_a
            elif root_a > root_b:
                uf[root_a] = root_b
        
        # import data to Union-Find structure
        for a, b, _ in roads:
            union(a, b)
        
        min_score = float('inf')
        # find the minimum score (the shortest edge)
        for a, b, distance in roads:
            # find if the group of the city *a* containing city *n*
            if find(a) == find(n) or find(b) == find(n):
                min_score = min(min_score, distance)
        
        return min_score

