'''
Explore binary search: Template I

binary search approach

divide x by middle number till left>right,
then the last middle number is the nearest rounded down integer of x's square root.
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        lastMid = 0  # last rounded down mid
        
        while(left <= right):
            mid = left + (right-left)//2
            quo = x // mid
            if (quo == mid):
                return mid
            elif (quo < mid):
                right = mid - 1
            else:
                left = mid + 1
                lastMid = mid

        return lastMid

