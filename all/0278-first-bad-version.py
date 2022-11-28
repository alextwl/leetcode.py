class Solution:
    def firstBadVersion(self, n: int) -> int:
        # do binary search
        bad = n
        good = 0
        # set the middle version number
        current = bad // 2 + bad % 2
        while(True):
            if isBadVersion(current):
                if current < bad:
                    # update first seen bad ver
                    bad = current
                else:
                    # first bad ver foundlast seen good ver
                    return bad
            else:
                # update last seen good ver
                good = current
            # set middle version between last seen good ver and first seen bad ver
            current = (good + bad) // 2  + (good + bad) % 2


'''
refined binary search ver
'''

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while(left < right):
            mid = left + (right-left)//2
            if isBadVersion(mid):
                # mid may be the first bad version, so do not exclude it.
                right = mid
            else:
                left = mid + 1
        
        # when left == right, it's the first bad version.
        return left

