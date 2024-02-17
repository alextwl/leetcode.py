'''
2024/02/17 daily challenge

min heap approach
'''

import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_used = []  # min heap
        brick_used = 0
        prev = heights[0]
        
        for i, h in enumerate(heights):
            if prev < h:
                diff = h - prev
                if ladders:
                    # use ladders if available, regardless the size of gap
                    # we may replace it in further steps
                    heapq.heappush(ladder_used, diff)
                    ladders -= 1
                else:
                    # using ladders for the larger gap is always optimal
                    if ladder_used and diff > ladder_used[0]:
                        # pull a ladder from a prev bldg and use bricks instead
                        brick_used += heapq.heappop(ladder_used)
                        # use ladder for the current step
                        heapq.heappush(ladder_used, diff)
                    else:
                        # use bricks for the current step
                        brick_used += diff
                    # check if we exhausted those bricks
                    if brick_used > bricks:
                        # we cannot reach the current building,
                        # so turn back to the previous bldg.
                        return i - 1
            prev = h
        # the last building reached
        return i

