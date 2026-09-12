'''
2026/09/12 daily challenge

dynamic programming + binary search approach

learnt from official editorial:
https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/editorial/#approach-dynamic-programming--binary-search

similar to problem 1751
'''


import bisect


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # (right, left, weight, idx)
        ivals = [(b, a, c, i) for i, (a, b, c) in enumerate(intervals)]
        ivals.sort()

        dp = [[0] * 5 for _ in range(n + 1)]
        indices = [[[] for _ in range(5)] for _ in range(n + 1)]
        for i, (right, left, weight, orig_idx) in enumerate(ivals):
            # search a right point < left in the range of ivals[0..i]
            k = bisect.bisect_left(ivals, (left,), hi=i)
            for j in range(1, 5):
                s1 = dp[i][j]
                s2 = dp[k][j - 1] + weight
                if s1 > s2:
                    dp[i + 1][j] = s1
                    indices[i + 1][j] = indices[i][j].copy()
                    continue
                new_picks = indices[k][j - 1].copy()
                new_picks.append(orig_idx)
                new_picks.sort()
                # use a lexicographically smaller one
                if s1 == s2 and indices[i][j] < new_picks:
                    new_picks = indices[i][j].copy()
                dp[i + 1][j] = s2
                indices[i + 1][j] = new_picks

        return indices[-1][-1]

