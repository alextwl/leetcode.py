'''
2026/03/09 daily challenge

dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/editorial/#approach-dynamic-programming

note the 3rd constraint actually says:
*NO* subarrays of arr with a size greater than limit contain only 0 or 1,
so we need to prevent from building any consecutive 0s or 1s with size > limit.
'''


MOD = 1_000_000_007


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        # base case: non-one subarrays within limit length
        for a in range(min(zero, limit) + 1):
            dp[a][0][0] = 1
        # base case: non-zero subarrays within limit length
        for b in range(min(one, limit) + 1):
            dp[0][b][1] = 1
        # top-down dp
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # exclude previous limit elements were all zeros
                excluded = dp[i - limit - 1][j][1] if i > limit else 0
                # append zero
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1] - excluded) % MOD

                # exclude previous limit elements were all ones
                excluded = dp[i][j - limit - 1][0] if j > limit else 0
                # append one
                dp[i][j][1] = (dp[i][j-1][1] + dp[i][j-1][0] - excluded) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD

