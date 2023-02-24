'''
2023/02/24 daily challenge

max heap approach
learnt from
https://leetcode.com/problems/minimize-deviation-in-array/solutions/3223541/day-55-priority-queue-easiest-beginner-friendly-sol/

1. convert the array to an all-even array in order to proceed it easier.
2. use max heap to maintain the maximum number and try to decrease it by doing the operation type-1.
3. minimize the minimum deviation by popping the max number and diffing it with the minNum.
'''

from heapq import heappush, heappop


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # import nums to the heap and multiply all odds to evens.
        h = []
        minNum = float('inf')
        for v in nums:
            if (v & 1):
                # it's odd, multiply it by 2.
                v *= 2
            minNum = min(minNum, v)
            heappush(h, -v)

        minDev = float('inf')
        while(True):
            v = -heappop(h)  # this is the current maximum number
            minDev = min(minDev, v - minNum)  # update minimum deviation

            # check if we can decrease the max number
            if (v & 1):
                # can't because it's an odd
                break
            
            v = v >> 1
            minNum = min(minNum, v)
            heappush(h, -v)
        
        return minDev

