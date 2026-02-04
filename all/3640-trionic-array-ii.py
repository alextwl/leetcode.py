'''
2026/02/04 daily challenge

dynamic programming approach
'''


import itertools


NEG_INF = float('-inf')


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # dp space for 4 phases
        # start -> inc -> dec -> inc
        dp0_prev = nums[0]  # start from i
        dp1_prev = dp1 = NEG_INF  # 1st inc ending at i
        dp2_prev = dp2 = NEG_INF  # dec ending at i
        ans = dp3_prev = dp3 = NEG_INF  # 2nd inc ending at i

        for a, b in itertools.pairwise(nums):
            dp0 = b
            if a < b:
                # increasing
                dp1 = max(dp1_prev + b, dp0_prev + b)
                dp2 = NEG_INF
                dp3 = max(dp3_prev + b, dp2_prev + b)
            elif a > b:
                # decreasing
                dp1 = dp3 = NEG_INF
                dp2 = max(dp2_prev + b, dp1_prev + b)
            else:
                # equal
                dp1 = dp2 = dp3 = NEG_INF

            dp0_prev = dp0
            dp1_prev = dp1
            dp2_prev = dp2
            dp3_prev = dp3
            ans = max(ans, dp3)

        return ans

