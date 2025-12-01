'''
2023/07/27 daily challenge
2025/12/01 daily challenge

binary search approach
'''

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def isRunTimeAchievable(hour):
            usable = 0  # the sum of usable power from each battery
            
            for power in batteries:
                '''
                if power <= hour, we can use all of its power,
                if power > hour, we can only use input hours of power from the battery
                '''
                usable += min(power, hour)
            
            return usable // n >= hour

        '''
        (left) all computers can run at least 1 hour
               because 1 <= n <= batteries.length and 1 <= batteries[i]
        (right) the maximum hours as an integer quotient that total power
                can feed all computers regardless of distribution.
        '''
        left = 1
        right = sum(batteries)//n
        
        while(left < right):
            mid = left + (right-left) // 2 + 1

            if isRunTimeAchievable(mid):
                left = mid
            else:
                right = mid - 1

        return left


'''
sorting + prefix sum approach
'''


import itertools


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if len(batteries) == n:
            # no battery can be exchanged with spares
            return min(batteries)

        batteries.sort()
        # use larger batteries initially
        bats = batteries[-n:]
        # distribute power of batteries which weren't in the initial allocation
        extras = sum(batteries[:-n])
        for i, (p0, p1) in enumerate(itertools.pairwise(bats), start=1):
            # try to charge batteries prior to p1
            if extras < (diff := (p1 - p0) * i):
                # insufficient powers
                # the max runtime is the duration of extra-charged p0
                return p0 + extras // i
            extras -= diff
        # distribute remaining powers to all N batteries
        return bats[-1] + extras // n

