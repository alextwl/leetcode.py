'''
2023/02/11 daily challenge

breadth first search approach
'''

import collections

RED = 0
BLUE = 1


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # build graph
        g = [collections.defaultdict(set),
             collections.defaultdict(set)]
        for a, b in redEdges:
            g[RED][a].add(b)
        for a, b in blueEdges:
            g[BLUE][a].add(b)
        
        # the distance from 0 to any node ending with specific color edge
        minDists = [None, None]
        minDists[RED] = [float('inf')] * n  # end with red edge
        minDists[RED][0] = 0  # dist(0 -> 0) == 0
        minDists[BLUE] = minDists[RED].copy() # end with blue edge

        # initial queue
        q = collections.deque()  # (destination node, last edge color, distance)
        for dest in g[RED][0]:
            q.append((dest, RED, 1))
        for dest in g[BLUE][0]:
            q.append((dest, BLUE, 1))

        # BFS
        while(q):
            node, last_color, d = q.popleft()
            if d >= minDists[last_color][node]:
                # current distance is equal to or larger than last minimum distance
                # no need to traverse further
                continue
            minDists[last_color][node] = d

            # traverse childern with alternative color
            next_color = last_color ^ 1
            d += 1
            for child in g[next_color][node]:
                q.append((child, next_color, d))
        
        # combine minDists of 2 colors and build final ans
        ans = []
        for d1, d2 in zip(*minDists):
            d = min(d1, d2)
            if d == float('inf'):
                ans.append(-1)
            else:
                ans.append(d)
        
        return ans

