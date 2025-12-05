'''
counter + combinatorics approach

time=O(n * 21)
'''


import collections


# list of valid sums of deliciousness of two food items
# 1 ~ 2**21 because deliciousness[i] <= 2**20
SUMS = [1 << i for i in range(22)]


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = collections.Counter(deliciousness)
        ans = 0
        for k0, v0 in cnt.items():
            for pair_sum in SUMS:
                k1 = pair_sum - k0
                if k1 == k0 and v0 > 1:
                    # two food items with same value of deliciousness
                    ans = (ans + v0 * (v0 - 1) // 2) % 1_000_000_007
                elif k1 > k0 and k1 in cnt:
                    # two food items with different values of deliciousness
                    # search 2nd item only with better deliciousness
                    ans = (ans + v0 * cnt[k1]) % 1_000_000_007
        return ans

