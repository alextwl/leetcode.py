'''
2023/02/22 daily challenge

binary search approach
learnt from the official solution

the main idea is to search the minimum weight of the ship
by trying the range [max(weights), sum(weights)]
instead of using dynamic programming which will be TLE.
'''


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isLoadable(capacity):
            '''
            try if all packages are loadable with the given days and capacity.
            '''
            dayElapsed = 1
            weightLoaded = 0
            for w in weights:
                new_weight = weightLoaded + w
                if new_weight > capacity:
                    dayElapsed += 1
                    weightLoaded = w
                else:
                    weightLoaded = new_weight
            return dayElapsed <= days
        
        # combine max() & sum() to speed up
        left = right = 0
        for w in weights:
            left = max(left, w)
            right += w

        while(left < right):
            mid = (left + right) >> 1  # it's safe because mid is a capacity value and not an index of an array.
            if isLoadable(mid):
                # the 'right' capacity is always loadable and may be the minimum,
                # we should not exclude it in the next round.
                right = mid
            else:
                left = mid + 1
        
        return left

