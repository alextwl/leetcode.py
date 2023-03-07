'''
2023/03/07 daily challenge

binary search approach

since the input values are large,
use binary search to approach the minimum time.
'''


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        getTrips = lambda t: sum(t//cost for cost in time)

        left = 1  # the minimum time cannot be lesser than 1 sec
        right = min(time) * totalTrips  # the time of right should be always sufficient for the totalTrips
        minTime = float('inf')

        while(left <= right):
            mid = left + ((right-left)>>1)
            trips = getTrips(mid)

            if trips >= totalTrips:
                # the current value of trips is sufficient,
                # minimize the answer of time.
                minTime = min(minTime, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return minTime

