'''
2026/08/21 daily challenge

binary search + inclusion-exclusion principle approach

learnt from official editorial 1:
https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/editorial/#approach-1-binary-answer--inclusion-exclusion-principle
'''


import math


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        m = 1 << n

        coins.sort()
        # counts & least common multiple (LCM) by mask
        cnt = [0] * m
        lcm = [0] * m

        for mask in range(1, m):
            curr_lcm = 1
            for i, coin in enumerate(coins):
                if mask >> i & 1:
                    curr_lcm = curr_lcm // math.gcd(curr_lcm, coin) * coin
                    cnt[mask] += 1
            lcm[mask] = curr_lcm

        def count(x):
            # determine the priority of x
            ret = 0
            for mask in range(1, m):
                if lcm[mask] <= x:
                    # inclusion-exclusion principle
                    if cnt[mask] & 1:
                        ret += x // lcm[mask]
                    else:
                        ret -= x // lcm[mask]
            return ret

        # binary search the ans
        left, right = k, coins[0] * k + 1
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

