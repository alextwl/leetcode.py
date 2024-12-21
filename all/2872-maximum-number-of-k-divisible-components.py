'''
2024/12/21 daily challenge

depth first search approach (recursive ver)

search subtrees and count edges we can cut.
'''


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = {i: set() for i in range(n)}
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        def dfs(node, parent = None):
            sum_val = values[node]
            sum_cuts = 0
            for child in g[node] - {parent}:
                val, cuts = dfs(child, node)
                if val % k:
                    sum_val += val
                    sum_cuts += cuts
                else:
                    sum_cuts += cuts + 1
            return (sum_val, sum_cuts)

        return dfs(0)[1] + 1

