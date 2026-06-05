'''
2026/06/05 daily challenge

dynamic programming + depth first search approach

learnt from official editorial 1:
https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/editorial/#approach-1-digit-dynamic-programming
'''


import functools


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(num):
            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            @functools.cache
            def dfs(i, prev, curr, is_limit, is_leading):
                if i == n:
                    return (1, 0)
                
                cnt, wave = 0, 0  # return values
                up = int(s[i]) if is_limit else 9  # enumerate digits in [0, up] range
                for dig in range(up + 1):
                    new_leading = is_leading and (dig == 0)
                    new_prev = curr
                    new_curr = -1 if new_leading else dig
                    sub_cnt, sub_sum = dfs(i + 1, new_prev, new_curr, is_limit and (dig == up), new_leading)
                    if not new_leading and prev >= 0 and curr >= 0:
                        if (prev < curr and curr > dig) or (prev > curr and curr < dig):
                            wave += sub_cnt
                    cnt += sub_cnt
                    wave += sub_sum
                return cnt, wave
            return dfs(0, -1, -1, True, True)[1]
        return solve(num2) - solve(num1 - 1)

