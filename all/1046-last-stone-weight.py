'''
leetcode 75 lv1 day 15

max heap approach
'''

from heapq import heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        # build max heap (min heap with negative values)
        for weight in stones:
            heappush(h, -weight)
        
        while(h):
            x = heappop(h)
            if h:
                y = heappop(h)
            else:
                # the last stone's weight is x.
                return -x
            
            if x != y:
                # destroy x and push new y.
                heappush(h, x-y)

        # there are no stones left.
        return 0

