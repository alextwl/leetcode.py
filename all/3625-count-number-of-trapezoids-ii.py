'''
2025/12/03 daily challenge

geometry + hash + counter approach

learnt from official editorial:
https://leetcode.com/problems/count-number-of-trapezoids-ii/editorial/#approach-hash-table--geometry-mathematics

advanced problem of 3623.
'''


import collections


# use a big number as the slope of vertical lines
INF = 1_000_000_007


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        s2i = collections.defaultdict(list)  # slope to intercepts
        m2s = collections.defaultdict(list)  # middle point to slopes

        # build maps of slopes, intercepts & middle points
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]

                if x1 == x2:
                    # two points form a vertical line
                    slope = INF
                    intercept = x1
                else:
                    dx, dy = x1 - x2, y1 - y2
                    slope = (y2 - y1) / (x2 - x1)
                    intercept = (y1 * dx - x1 * dy) / dx

                # middle coordinate combined into an integer key
                mid = (x1 + x2) * 10000 + (y1 + y2)
                s2i[slope].append(intercept)
                m2s[mid].append(slope)

        ans = 0

        # count quadrilaterals including both trapezoid & parallelogram
        for intercept_list in s2i.values():
            if len(intercept_list) == 1:
                continue

            prefix = 0
            for count in collections.Counter(intercept_list).values():
                ans += prefix * count
                prefix += count

        # remove count of parallelograms from answer
        for slope_list in m2s.values():
            if len(slope_list) == 1:
                continue

            prefix = 0
            for count in collections.Counter(slope_list).values():
                ans -= prefix * count
                prefix += count

        return ans

