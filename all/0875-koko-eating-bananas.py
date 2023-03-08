'''
2023/03/08 daily challenge

binary search approach
'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        search the minimum speed between 1 banana per hour and max(piles) bananas per hour.
        '''
        left = 1
        right = max(piles)

        '''
        canEatAll(): evaluate how much time Koko needs to eat all the bananas in k speed
                     and compare it with h time to determine whether k speed is sufficient or not.

        note: (bananas - 1) // k + 1 == math.floor(bananas / k)
        '''
        canEatAll = lambda k: sum((bananas - 1) // k + 1 for bananas in piles) <= h

        while(left < right):
            mid = (left + right) >> 1  # speed.
            if canEatAll(mid):
                # the right speed should be always sufficient, so don't assign mid-1 to it.
                right = mid
            else:
                left = mid + 1
        
        return left

