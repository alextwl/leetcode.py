'''
2026/06/20 daily challenge

two-pass approach (transitivity of restrictions)

learnt from official editorial:
https://leetcode.com/problems/maximum-building-height/editorial/#approach-transitivity-of-restrictions
'''


import itertools


class Solution:
    def maxBuilding(self, n: int, id_maxh: List[List[int]]) -> int:
        id_maxh.append([1, 0])  # the first building has height limit 0.
        id_maxh.sort()  # sort by id

        # soft limit of last building's height is n - 1 if not specified.
        if id_maxh[-1][0] != n:
            id_maxh.append([n, n - 1])

        # update restrictions by applying the rule of height diff<=1 between two adjacent buildings
        m = len(id_maxh)
        # 1st pass: left to right
        for i in range(1, m):
            id_maxh[i][1] = min(id_maxh[i][1], id_maxh[i - 1][1] + id_maxh[i][0] - id_maxh[i - 1][0])
        # 2nd pass: right to left
        for i in range(m - 2, 0, -1):
            id_maxh[i][1] = min(id_maxh[i][1], id_maxh[i + 1][1] + id_maxh[i + 1][0] - id_maxh[i][0])

        ans = 0
        for (i, ih), (j, jh) in itertools.pairwise(id_maxh):
            # there may be zero, one or more buildings between id_maxh[i][0] and id_maxh[i+1][0],
            # calculate the tallest in the range of [id_maxh[i][0], id_maxh[i+1][0]] inclusive.
            ans = max(ans, (j - i + ih + jh) // 2)

        return ans

