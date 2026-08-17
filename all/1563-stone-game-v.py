'''
2026/08/17 daily challenge

prefix sums + depth first search (dynamic programming) approach

Runtime=7862ms, Beats 34.50%
'''


import functools


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0]
        curr_sum = 0
        for v in stoneValue:
            curr_sum += v
            prefix.append(curr_sum)

        @functools.cache
        def dp(l, r):
            if l == r:
                return 0

            row_sum = prefix[r+1] - prefix[l]
            left_sum = 0
            ret = 0
            for i in range(l, r):
                left_sum += stoneValue[i]
                right_sum = row_sum - left_sum
                if left_sum < right_sum:
                    ret = max(ret, dp(l, i) + left_sum)
                elif left_sum > right_sum:
                    ret = max(ret, dp(i + 1, r) + right_sum)
                else:
                    # equal division
                    ret = max(ret, max(dp(l, i), dp(i + 1, r)) + left_sum)
            return ret

        return dp(0, len(stoneValue) - 1)

