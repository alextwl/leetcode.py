'''
2024/02/11 daily challenge

dynamic programming approach (recursive ver)

the intuition is the same as problem 741 Cherry Pickup I.
two robots' x-coordinates are always the same,
so we don't need to calculate x1 or x2,
and just take dp[x][y1][y2] as parameters.
'''

import functools


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @functools.cache
        def dp(x, y1, y2):
            # consider two robots move t steps simultaneously,
            # they share the same x-coordinate.
            if not(x < m and 0 <= y1 < n and 0 <= y2 < n):
                return float('-inf')
            
            ans = grid[x][y1]
            if y1 != y2:
                # do not count the same cell's cheeries twice.
                ans += grid[x][y2]
            
            if x == m - 1:
                # bottom reached
                return ans
            
            x += 1  # robots always move down
            ans += max(dp(x, y1, y2),
                       dp(x, y1 + 1, y2),
                       dp(x, y1 - 1, y2),
                       dp(x, y1, y2 + 1),
                       dp(x, y1 + 1, y2 + 1),
                       dp(x, y1 - 1, y2 + 1),
                       dp(x, y1, y2 - 1),
                       dp(x, y1 + 1, y2 - 1),
                       dp(x, y1 - 1, y2 - 1))

            return ans
        
        return max(0, dp(0, 0, n-1))

