'''
2023/05/13 daily challenge

dynamic programming approach

learnt from
https://leetcode.com/problems/count-ways-to-build-good-strings/solutions/3517765/python-java-c-simple-solution-easy-to-understand/
'''

import collections


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        '''
        dp[i] = the number of strings with length i constructed by
                performing the operations of appending consecutive '0's or '1's.

        the base case is an empty string which is the only string with length 0.
        '''
        dp = collections.Counter()
        dp[0] = 1

        # count from length 1 to length high.
        for i in range(1, high+1):
            '''
            For example 2:
            when i=1, zero=1, one=2,
            sub1 = prev '' + '0' = dp[0] + '0' = 1
            sub2 = dp[-1] + '11' = non-existent string because there's no string with negative length.
            dp[1] = 1 + 0 = 1

            when i=2,
            sub1 = prev '0' + '0' = dp[1] + '0' = 1
            sub2 = prev '' + '11' = dp[0] + '11' = 1
            dp[2] = 1 + 1 = 2
            '''
            # previous substrings + appending zeroes at current step
            sub1 = dp[i-zero]
            # previous substrings + appending ones at current step
            sub2 = dp[i-one]

            dp[i] = sub1+sub2

        # sum the number of strings with valid lengthes [low, high] only.
        return sum(dp[good] for good in range(low, high+1)) % 1_000_000_007


'''
2024/12/30 daily challenge

dynamic programming approach (optimized)

do modulo in every iteration significantly boosts runtime up 10x times.
'''


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(min(zero, one), high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % 1_000_000_007

        return sum(dp[low:]) % 1_000_000_007

