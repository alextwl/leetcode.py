'''
2025/12/02 daily challenge

geometry + prefix sum + combinatorics approach
'''


import collections


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # count x coordinates grouped by y-axis
        y2xcnt = collections.defaultdict(int)
        for _, y in points:
            y2xcnt[y] += 1

        ans = 0
        psum = 0  # prefix sum of scanned edges parallel to the x-axis
        for xcnt in y2xcnt.values():
            # edge pair count by the number of x coordinates
            pair_cnt = xcnt * (xcnt - 1) // 2
            ans = (ans + pair_cnt * psum) % 1_000_000_007
            psum = (psum + pair_cnt) % 1_000_000_007
        return ans

