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
