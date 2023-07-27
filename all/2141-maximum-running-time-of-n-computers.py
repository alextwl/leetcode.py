'''
2023/07/27 daily challenge

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

