'''
2022/01/08 daily challenge

learnt from official solution

the idea is to find a line containing the most points which
one point to other points' vectors share the same atan2.
'''

import collections
from math import atan2


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            # any line has only 1 point.
            return 1
        # when there're at least 2 points, the minimum points of a line are 2 points.
        ans = 2

        # select any point as a source of vector
        for i, src in enumerate(points):
            pcount = collections.defaultdict(int)  # count of destination points sharing the same atan2
            for j, dst in enumerate(points):
                if i != j:
                    # atan2(y, x) == the arc tangent of y/x.
                    pcount[atan2(dst[1] - src[1], dst[0] - src[0])] += 1
            ans = max(ans, max(pcount.values()) + 1)  # max(ans, max point count of the same atan2 + src itself)

        return ans

