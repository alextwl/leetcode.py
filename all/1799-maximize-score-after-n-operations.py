'''
2023/05/14 daily challenge

dynamic programming approach

since the range of input is small (1 <= n <= 7),
it's reasonable to proceed all pairs of GCD and memorize each state of operations.
'''

import collections
import math


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        '''
        calculate each pair's GCD for further lookup.

        gcd_lookup[i][j] = i-th num & j-th num's GCD
        (also equal to gcd_lookup[j][i] for pair-swapped lookup)
        '''
        gcd_lookup = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                gcd_lookup[i][j] = gcd_lookup[j][i] = math.gcd(nums[i], nums[j])
        
        '''
        the maximum score of given subarray's bitmask.

         nums' index = 543210
        e.g. n=6, dp[0b110011] = the maximum score of subarray:
        [nums[0],nums[1],nums[4],nums[5]] with 2 operations performed.
        '''
        dp = collections.defaultdict(int)

        '''
        iterate from 0 (no nums picked) to (1 << n) - 1  (all nums picked, e.g. 0b111111)
        and perform operation on even-1s pairs only (e.g. 0b11, 0b110011, etc.)
        '''
        for mask in range(1<<n):
            ones = mask.bit_count()  # count the number of 1 bit  (Python >= 3.10)
            if ones & 1:
                # non-paired bit found in the mask, skip it.
                continue

            # the number of current operation
            # e.g. 0b11 -> 1 op performed, 0b110011 -> 2 ops performed        
            curr_ops = ones>>1

            # time to iterate two nums pair
            for i in range(n):
                i_mask = 1 << i
                if not(mask & i_mask):
                    # if the first num is not picked in the mask, skip it.
                    # e.g. i=3 not picked in 0b110011 (4th bit disabled.)
                    continue
                for j in range(i+1, n):
                    j_mask = 1 << j
                    if not(mask & j_mask):
                        # if the second num is not picked in the mask, skip it.
                        continue
                    '''
                    query the previous operation's mask.
                    e.g. the current mask is 0b110011, i=4, and j=5,
                    the previous mask is 0b11 (because 0b110000 is Xor'd.)
                    '''
                    prev_mask = mask ^ i_mask ^ j_mask

                    '''
                    choose the greater one of the maximum score from
                    (1) the current mask's, or
                    (2) the previous mask's max score + operation score
                    '''
                    dp[mask] = max(dp[mask], dp[prev_mask] + curr_ops * gcd_lookup[i][j])
                    #print("%s max = %d" % (bin(mask), dp[mask]))

        return dp[(1 << n) - 1]

