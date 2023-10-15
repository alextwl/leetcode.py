'''
2023/10/15 daily challenge

dynamic programming approach
'''

import functools


MOD = 1_000_000_007


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @functools.cache
        def dp(curr_pos, steps_remaining):
            if steps_remaining == 0:
                if curr_pos == 0:
                    # the final position is at index 0, it forms a valid way
                    return 1
                # invalid final place
                return 0

            next_step = steps_remaining - 1
            # (1) stay in the same place
            ways = dp(curr_pos, next_step)

            # (2) move to the left (except it's at left bound.)
            if curr_pos > 0:
                ways = (ways + dp(curr_pos - 1, next_step)) % MOD

            # (3) move to the right (except it's at right bound.)
            if curr_pos < arrLen - 1:
                ways = (ways + dp(curr_pos + 1, next_step)) % MOD

            return ways

        # start from index 0
        return dp(0, steps)

