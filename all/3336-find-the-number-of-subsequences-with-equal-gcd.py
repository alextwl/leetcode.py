'''
2026/07/14 daily challenge

dynamic programming approach
'''


import math


MOD = 1_000_000_007


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        maxval = max(nums)

        # dp0[i][j] = count of previous element processed
        #             with seq0's gcd i and seq1's gcd j.
        dp0 = [[0] * (maxval + 1) for _ in range(maxval + 1)]
        dp0[0][0] = 1

        for v in nums:
            # dp1[i][j] = count of current element v processed
            #             with seq0's gcd i and seq1's gcd j.
            dp1 = [[0] * (maxval + 1) for _ in range(maxval + 1)]
            for i in range(maxval + 1):
                gcd0 = math.gcd(i, v)
                for j in range(maxval + 1):
                    cnt = dp0[i][j]
                    if not cnt:
                        continue
                    gcd1 = math.gcd(j, v)
                    # skip adding v to subseqs
                    dp1[i][j] = (dp1[i][j] + cnt) % MOD
                    # add v to seq0
                    dp1[gcd0][j] = (dp1[gcd0][j] + cnt) % MOD
                    # add v to sep1
                    dp1[i][gcd1] = (dp1[i][gcd1] + cnt) % MOD
            dp0 = dp1

        ans = 0
        # the problem asks for equal GCD pairs only.
        for i in range(1, maxval + 1):
            ans = (ans + dp1[i][i]) % MOD
        return ans

