'''
2023/06/02 daily challenge

depth first search approach
'''

import math


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = {i: set() for i in range(n)}  # uni-directional

        # calculate distances of all pairs of 2 bombs.
        for i in range(n):
            for j in range(i+1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                i2j = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                # add edge only when the distance is within the radius of each bomb.
                if i2j <= r1:
                    graph[i].add(j)
                if i2j <= r2:
                    graph[j].add(i)

        def dfs(i: int, detonated: set):
            detonated.add(i)
            for j in graph[i] - detonated:
                dfs(j, detonated)

        ans = 0
        # just try to detonate each bomb.
        for i in range(n):
            bomb_set = set()
            dfs(i, bomb_set)
            ans = max(ans, len(bomb_set))

        return ans

