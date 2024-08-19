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


'''
dynamic programming approach (iterative ver)

always consider 1 Copy All + multiple Paste a factor-length substring
for all n.
'''


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)
        dp[1] = 0  # nothing to do if n == 1

        for i in range(2, n + 1):
            min_dp_i = dp[i]
            # find all factors of i to minimize the step
            for j in range(1, i // 2 + 1):
                quo, rem = divmod(i, j)
                # two options:
                # 1. reuse the previous smaller one.
                # 2. steps to get j + (1 Copy All for j + paste (j-1) times)
                #    == dp[j] + i // j
                if rem == 0:
                    min_dp_i = min(min_dp_i, dp[j] + quo)
            dp[i] = min_dp_i

        return dp[-1]

