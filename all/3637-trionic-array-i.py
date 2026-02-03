'''
2026/02/03 daily challenge

linear scan approach
'''


import itertools


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 3 or nums[0] >= nums[1]:
            # shortcut: the first slice must be increasing
            return False

        state = 0  # even: increasing, odd: decreasing

        for a, b in itertools.pairwise(nums):
            if a < b:
                # increasing
                if state & 1:
                    # previous pair was decreasing
                    state += 1
            elif a > b:
                # decreasing
                if (state & 1) == 0:
                    # previous pair was increasing
                    state += 1
            else:
                # a == b, definitely non-trionic.
                return False
            if state > 2:
                # pattern beyond trionic
                return False

        return state == 2

