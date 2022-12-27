'''
2022/12/27 daily challenge

heap + greddy approach
'''

from heapq import heappush, heappop


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        q = []  # a heap for available spaces of bags, sorted from the smallest
        full = 0  # answer, a counter for the maximum number of full bags

        # calculate the remaining spaces to be filled
        for cap, rock in zip(capacity, rocks):
            if space := cap - rock:
                # the bag is not full
                if space <= additionalRocks:
                    # the bag can be filled
                    heappush(q, space)
            else:
                # the bag is already full
                full += 1
        
        # try to fill bags from the smallest remaining space.
        while(q):
            additionalRocks -= heappop(q)
            if additionalRocks >= 0:
                # one more full bag
                full += 1
            else:
                # additional rocks exhausted.
                break
        
        return full

