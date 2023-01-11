'''
2023/01/11 daily challenge

recursive depth first search approach

if a vertex itself or its descendent had apples,
we shall walk at least 1 round of trip (2 seconds) between the vertex and its parent,
count it by DFS when found apple at itself or its descendent.
'''

import collections


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # build tree
        vv = collections.defaultdict(set)
        for a, b in edges:
            vv[a].add(b)
            vv[b].add(a)

        # answer
        mintime = 0

        def dfs(v, parent) -> bool:
            '''
            :param v: vertex
            :type v: int
            :param parent: the parent of vertex
            :type parent: int
            :return: itself or descendent has apple.
            :rtype: bool
            '''
            foundApple = hasApple[v]
            for child in vv[v] - {parent}:
                foundApple |= dfs(child, v)
            # add time for travelling between v & parent back and forth.
            if foundApple:
                nonlocal mintime
                mintime += 2
            return foundApple
        
        # traverse from root
        for c in vv[0]:
            dfs(c, 0)

        return mintime

