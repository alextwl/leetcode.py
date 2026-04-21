'''
2026/04/21 daily challenge

union-find + hash counter approach
'''


import collections


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        ans = 0
        # ss[i][v] = seen count of value in component (parent) i
        ss = collections.defaultdict(collections.Counter)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            a, b = find(a), find(b)
            if a > b:
                parent[a] = b
            elif b > a:
                parent[b] = a

        # convert to graphs
        # indices of source/target are nodes.
        # allowedSwaps are edges.
        for a, b in allowedSwaps:
            union(a, b)

        # count seen values by component (union-find parent)
        for i, src in enumerate(source):
            comp = find(i)
            ss[comp][src] += 1

        # since swapping pairs of indices was unlimited,
        # we can just find the count of missing elements in a component.
        for i, dst in enumerate(target):
            comp = find(i)
            if ss[comp][dst]:
                ss[comp][dst] -= 1
            else:
                # no more value dst in component comp
                ans += 1

        return ans

