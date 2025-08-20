'''
math approach

brain teaser: the costs of all shortest paths are actually equivalent,
we can simply go from startPos[0] to homePos[0] directly and
from startPos[1] to homePos[1] directly. no need to run Dijkstra's.
'''


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        (x, y), (x1, y1) = startPos, homePos
        ans = 0
        while x != x1:
            x += 1 if x < x1 else -1
            ans += rowCosts[x]
        while y != y1:
            y += 1 if y < y1 else -1
            ans += colCosts[y]
        return ans

