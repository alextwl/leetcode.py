'''
2023/11/10 daily challenge

depth first search approach
'''

import collections


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = collections.defaultdict(set)
        for v, w in adjacentPairs:
            g[v].add(w)
            g[w].add(v)

        # find the root to start traversing
        for v, wSet in g.items():
            if len(wSet) == 1:
                child = {v}
                break

        ans = []
        parent = set()
        while(child):
            node = child.pop()
            ans.append(node)

            child = g[node] - parent
            parent = {node}

        return ans

