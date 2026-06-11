'''
2026/06/11 daily challenge

depth first search + math approach

learnt from official editorial:
https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/editorial/#approach-depth-first-search--mathematics
'''


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        # build graph
        g = [[] for _ in range(n + 1)]  # g[0] is unused
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(x, src):
            ret = 0
            for y in g[x]:
                if y == src:
                    continue
                ret = max(ret, dfs(y, x) + 1)
            return ret

        max_depth = dfs(1, 0)
        return pow(2, max_depth - 1, 1_000_000_007)

