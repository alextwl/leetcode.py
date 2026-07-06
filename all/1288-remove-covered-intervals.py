'''
2026/07/06 daily challenge

brute force method approach

Runtime=18ms, Beats 7.78%
'''


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = 0
        for i, (a, b) in enumerate(intervals):
            for j, (c, d) in enumerate(intervals):
                if i == j: continue
                if c <= a and b <= d:
                    # covered
                    break
            else:
                # not covered
                ans += 1
        return ans


'''
sorting approach

Runtime=3ms, Beats 77.50%
'''


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = len(intervals)
        # sort by (a, -b), let early interval cover later & smaller intervals
        intervals.sort(key=lambda x: (x[0], -x[1]))

        it = iter(intervals)
        c, d = next(it)
        for a, b in it:
            # test if the interval [a, b) is covered by the interval [c, d) or not.
            if c <= a and b <= d:
                ans -= 1
            else:
                # not covered, update last interval
                c, d = a, b

        return ans

