'''
2025/10/11 daily challenge

counter + dynamic programming approach
'''


import collections


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ctr = collections.Counter(power)
        k2 = k1 = k0 = 0
        dp4 = dp3 = dp2 = dp1 = dp0 = 0
        for k in sorted(ctr.keys()):
            k_3 = k - 3
            damage = ctr[k] * k
            new_dp0 = max(dp4, dp3, dp2, dp1 if k1 <= k_3 else 0, dp0 if k0 <= k_3 else 0) + damage
            dp4, dp3, dp2, dp1, dp0 = dp3, dp2, dp1, dp0, new_dp0
            k2, k1, k0 = k1, k0, k
        return max(dp4, dp3, dp2, dp1, dp0)

