'''
2023/10/14 daily challenge

dynamic programming approach 
'''

import functools
import math


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        @functools.cache
        def dp(i, unpainted_walls):
            # no more cost if all wall were painted
            if unpainted_walls <= 0: return 0
            # run out of walls, the cost is infinite (will be overrided by minimized)
            if i >= n: return math.inf
            
            # knapsack problem
            # hire a paid painter to paint (1+time[i]) walls
            # the current wall by a paid painter + walls painted by a free painter
            # while paid painters were occupied.
            paid_painter_cost = cost[i] + dp(i+1, unpainted_walls - 1 - time[i])
            # or not to paint.
            dont_paint_cost = dp(i+1, unpainted_walls)
            
            return min(paid_painter_cost, dont_paint_cost)
        
        return dp(0, n)

