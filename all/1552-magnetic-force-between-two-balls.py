'''
2024/06/20 daily challenge

binary search approach

learnt from official solution:
https://leetcode.com/problems/magnetic-force-between-two-balls/solution/

binary search the minimum required force,
check if the force (== gap) could be used to place all balls,
and maximize it.
'''


import math


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def can_place_balls(min_force):
            balls_placed = 1  # always place a ball at the first basket

            it = iter(position)
            prev_basket = next(it)

            # greedily check if we can place all balls within the specified force
            for next_basket in it:
                if next_basket - prev_basket >= min_force:
                    balls_placed += 1
                    prev_basket = next_basket  # update only when a valid gap occured
                    if balls_placed == m:
                        return True

            return False

        # binary search the force
        req_force = 0
        left, right = 1, math.ceil((position[-1] - position[0]) / (m - 1.0))
        while(left <= right):
            mid = (right - left) // 2 + left
            
            if can_place_balls(mid):
                req_force = mid
                left = mid + 1
            else:
                right = mid - 1

        return req_force

