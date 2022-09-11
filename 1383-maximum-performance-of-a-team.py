'''
2022/09/11 daily challenge
greedy approach
'''

from heapq import heappush, heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speed_sum = 0
        performance = 0
        heap = []  # a heap to keep at most k engineers' speed
        
        # iterate from the engineer with highest efficiency.
        # it is to gurarantee the next engineer's efficiency is always minimum.
        for eng_eff, eng_spd in sorted(zip(efficiency, speed), reverse=True):
            # we are going to add one more engineer
            # so let's kick 1 engineer with slowest speed out
            # if the heap was out of space.
            while len(heap) > k-1:
                speed_sum -= heappop(heap)
            
            # add an engineer
            heappush(heap, eng_spd)
            speed_sum += eng_spd
            
            # greedy: update the maximum performance.
            # eng_eff is always minimum efficiency
            # because it's already sorted, no need to get min() here.
            performance = max(performance, speed_sum * eng_eff)
        
        return performance % (10**9 + 7)
