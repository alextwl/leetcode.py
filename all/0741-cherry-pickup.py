'''
dynamic programming approach (recursive ver)

reverse the path of bottom-right to top-left as 2nd person's move,
two persons move to the same terminal simultaneously,
so we can reduce the parameters of dp to 3 variables.

learnt from official solution 2.
'''

import functools


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        @functools.cache
        def dp(x1, y1, y2):
            # consider two persons move t steps simultaneously:
            # t steps == x1 + y1 == x2 + y2
            x2 = x1 + y1 - y2
            
            if (x1 == n or y1 == n or \
                    x2 == n or y2 == n or \
                    grid[x1][y1] == -1 or \
                    grid[x2][y2] == -1):
                # if boundary or blocker reached,
                # return negative infinity to indicate invalid path.
                return float('-inf')
            
            if x1 == y1 == n-1:
                # bottom right terminal reached.
                # just need to check one of the person's coordinate
                # because ppl move the same steps.
                return grid[x1][y1]  # also a base case.
            
            ans = grid[x1][y1]
            
            if x1 != x2:
                # plus the 2nd person's cell cherry if they were not on the same cell.
                # do not count the same cherry twice!
                ans += grid[x2][y2]
            
            # max(p1 moves right & p2 moves right,
            #     p1 moves down & p2 moves right,
            #     p1 moves right & p2 moves down,
            #     p1 moves down & p2 moves down)
            ans += max(dp(x1    , y1 + 1, y2 + 1),
                       dp(x1 + 1, y1    , y2 + 1),
                       dp(x1    , y1 + 1, y2),
                       dp(x1 + 1, y1    , y2))
            
            return ans
        
        # filter the unreachable result
        return max(0, dp(0, 0, 0))

