'''
2025/11/20 daily challenge

sorting approach
'''


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sort intervals by end in ascending order,
        # and then by start in descending order,
        # to ensure for all intervals with the same end
        # the earlier start could contain all later parts.
        intervals.sort(key=lambda x: (x[1], -x[0]))

        v0 = v1 = None
        ans = 0
        for start, end in intervals:
            if v0 is None or v1 < start:
                # if the current interval and the prev one didn't overlap,
                # always select the rightmost 2 values for a chance
                # to be reused by next interval.
                v0, v1 = end-1, end
                ans += 2
            elif v0 < start:
                # partial overlap, reuse one value and select end value.
                v0, v1 = v1, end
                ans += 1

        return ans

