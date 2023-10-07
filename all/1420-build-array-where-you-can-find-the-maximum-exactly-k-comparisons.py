'''
2023/10/07 daily challenge

top-down dynamic programming approach

learnt from official solution 1
https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/solution/
'''

import functools


MOD = 1_000_000_007


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @functools.cache
        def dp(i, maxSoFar, remain_k):
            '''
            :param i: the index of array to be placed
            :param maxSoFar: the maximum value of array[:i]
            :param remain_k: the remaining times to do comparsion
            '''
            # the array fulfilled
            if i == n:
                if remain_k == 0:
                    # can find the maximum exactly k comparsion
                    return 1
                # invalid numbers of comparsion
                return 0
            
            # for cases which do not update the maxSoFar
            # we multiply maxSoFar at index i because place any number within [1, maxSoFar]
            # (total maxSoFar numbers) does not trigger the comparsion.
            ans = (maxSoFar * dp(i+1, maxSoFar, remain_k)) % MOD
            # for cases which update the maxSoFar with
            # placing any number within [maxSoFar+1, m] at index i.
            for v in range(maxSoFar+1, m+1):
                ans = (ans + dp(i+1, v, remain_k - 1)) % MOD
            
            return ans
        
        return dp(0, 0, k)

