'''
2023/07/26 daily challenge

binary search approach
'''

import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        def getCommuteTime(speed):
            it = iter(dist)
            time_elapsed = 0.0
            for _ in range(0, n-1):
                # wait for the next ride except the last ride
                time_elapsed += math.ceil(next(it) / speed)

            # the last ride
            time_elapsed += next(it) / speed
            return time_elapsed

        # check if the input hour limit is feasible
        if math.ceil(hour) < n:
            return -1

        '''
        speed as two pointers
        the question said "Tests are generated such that the answer will not exceed 10**7.
        '''
        left, right = 1, 10_000_000

        while(left < right):
            mid = (left + right) // 2

            if getCommuteTime(mid) > hour:
                left = mid + 1
            else:
                right = mid

        return right

