'''
2022/12/19 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        # import & build a graph
        vertices = {i: set() for i in range(0, n)}
        for v1, v2 in edges:
            vertices[v1].add(v2)
            vertices[v2].add(v1)
        
        # BFS
        queue = collections.deque([source])
        seen = set([source])  # it kills loop and those already seen vertices in order to avoid duplicate visits.
        while(queue):
            parent = queue.popleft()
            # check children without those seen before
            for child in vertices[parent] - seen:
                if child == destination:
                    return True
                queue.append(child)
                seen.add(child)

        return False

