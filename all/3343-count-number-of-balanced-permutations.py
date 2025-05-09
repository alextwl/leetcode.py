'''
2025/05/09 daily challenge

dynamic programming approach

learnt from official editorial 2:
https://leetcode.com/problems/count-number-of-balanced-permutations/editorial/#approach-2-dynamic-programming
'''


import math


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        cnt = [0] * 10
        total = 0
        for d in map(int, num):
            cnt[d] += 1
            total += d
        
        # if the sum of all digits was odd, we're unable to find a valid permutation.
        if total & 1: return 0

        half = total >> 1
        m = (n + 1) >> 1  # the maximum count of odd digits

        dp = [[0] * (m + 1) for _ in range(half + 1)]
        dp[0][0] = 1  # base case

        count_sum = total_sum = 0
        for i, i_cnt in enumerate(cnt):
            count_sum += i_cnt
            total_sum += i * i_cnt
            for odd_count in range(min(count_sum, m), max(0, count_sum - (n - m)) - 1, -1):
                even_count = count_sum - odd_count
                for curr_sum in range(min(total_sum, half), max(0, total_sum - half) - 1, -1):
                    p = 0
                    for j in range(max(0, i_cnt - even_count), min(i_cnt, odd_count) + 1):
                        if i * j > curr_sum: break
                        ways = (math.comb(odd_count, j) * math.comb(even_count, i_cnt - j)) % 1_000_000_007
                        p = (p + ways * dp[curr_sum - i * j][odd_count - j] % 1_000_000_007) % 1_000_000_007
                    dp[curr_sum][odd_count] = p
        return dp[half][m]

