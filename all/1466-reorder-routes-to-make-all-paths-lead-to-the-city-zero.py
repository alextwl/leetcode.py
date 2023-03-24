'''
2023/03/24 daily challenge

depth first search approach

traverse all cities from city 0 regardless of the direction of edges,
and count all edges which need to be changed.
'''

import collections


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()  # (src, dst) tuple
        graph = collections.defaultdict(set)
        for src, dst in connections:
            roads.add((src, dst))
            graph[src].add(dst)
            graph[dst].add(src)
        
        def dfs(node, parent):
            reorders = 0

            '''
            if a road (parent->node) existed,
            we should change the direction to (node->parent)
            so that we can ultimately traverse from the node to city 0 (root).
            '''
            if (parent, node) in roads:
                reorders += 1
            
            for child in graph[node] - {parent}:
                reorders += dfs(child, node)
            
            return reorders
        
        return dfs(0, -1)

