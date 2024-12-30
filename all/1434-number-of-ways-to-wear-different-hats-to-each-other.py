'''
dynamic programming approach (recursive ver)
'''


import functools


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        hat2ppl = [list() for _ in range(41)]  # note the index of hat starts from 1.
        for person, perferred_hats in enumerate(hats):
            for hat in perferred_hats:
                hat2ppl[hat].append(1 << person)

        # the mask of all persons weared hats
        full = (1 << len(hats)) - 1

        @functools.cache
        def dp(i, mask):
            # dp(index of hat, mask of people who weared hats)
            if mask == full:
                # base case: all persons weared, form a valid combination
                return 1
            if i > 40:
                # not every person weared but all hats were scanned
                return 0

            # case 1: not choosing i-th hat
            ret = dp(i + 1, mask)

            # case 2: choose i-th hat
            for person_mask in hat2ppl[i]:
                if mask & person_mask == 0:
                    # this guy is available for wearing a mask
                    ret = (ret + dp(i + 1, mask | person_mask)) % 1_000_000_007

            return ret

        return dp(1, 0)

