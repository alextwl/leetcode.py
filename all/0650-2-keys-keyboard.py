'''
2024/08/19 daily challenge

dynamic programming approach (recursive ver)
'''


import functools


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        @functools.cache
        def get_min_steps(m, copy_len):
            '''
            m: the target length on the screen
            copy_len: the length of chars copied
            '''
            if m == n:
                return 0
            if m > n:
                # since the max input of n is 1000,
                # the max steps are 1000 times of pasting 'A'.
                return 1000

            paste_only = 1 + get_min_steps(m + copy_len, copy_len)
            copy_and_paste = 2 + get_min_steps(m * 2, m)

            return min(paste_only, copy_and_paste)
        
        # always do a Copy All operation in the beginning
        return 1 + get_min_steps(1, 1)

