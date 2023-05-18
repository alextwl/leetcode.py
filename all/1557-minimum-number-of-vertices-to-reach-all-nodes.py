'''
2023/05/18 daily challenge

set approach

ans = all nodes - all destinations = the minimum source vertices

any node which has at least 1 incoming node,
the node cannot be in the set of the minimum number of vertices to reach all nodes
because there's always one or multiple (parent) nodes can reach it.
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # since the question guaranteed all nodes in the graph are reachable,
        # the source value in the given edges is not important.
        ans = set(range(n)) - set(dst for _, dst in edges)
        return list(ans)

