'''
2022/12/28 daily challenge

heap approach
'''

from heapq import heappush, heappop


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []  # heap with negative values of piles
        total = 0  # total stones to be minimized

        # sum the piles and build the heap
        for stone in piles:
            heappush(h, -stone)
            total += stone
        
        # time to remove stones
        for _ in range(k):
            remaining = -heappop(h)
            removal = remaining >> 1
            total -= removal
            # push remaining stones back to the heap
            heappush(h, removal - remaining)
        
        return total

