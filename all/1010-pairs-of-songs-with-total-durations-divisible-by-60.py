'''
counter approach

count modulo of time elements and calculate combinations of pairs.

each element with modulo 0 & 30 can pair with other elements
with the same modulo, so the number of such pairs is n*(n-1)/2.
'''


import collections


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = collections.Counter(t % 60 for t in time)
        ans = 0
        for k, v in cnt.items():
            # find pairs with mod0 + mod1 == 60
            if 0 < k < 30:
                ans += v * cnt[60 - k]
        if cnt[0]:
            ans += cnt[0] * (cnt[0] - 1) // 2
        if cnt[30]:
            ans += cnt[30] * (cnt[30] - 1) // 2
        return ans

