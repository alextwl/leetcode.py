'''
2026/07/08 daily challenge

prefix sums + prefix array + table lookup method approach

learnt from official editorial:
https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/editorial/#approach-prefix-array
'''


MOD = 1_000_000_007
N = 100001
POW10 = [1] * N


# build prefix concatenation value lookup table
for i in range(1, N):
    POW10[i] = POW10[i - 1] * 10 % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n, m = len(s), len(queries)
        pfx = [0] * (n + 1)
        xval = [0] * (n + 1)  # concatenated non-zero integers of s[:i]
        cnt = [0] * (n + 1)  # prefix counter of non-zero digits in s[:i]
        ans = [0] * m

        for i, v in enumerate(map(int, s)):
            if v:
                pfx[i + 1] = pfx[i] + v
                xval[i + 1] = (xval[i] * 10 + v) % MOD
                cnt[i + 1] = cnt[i] + 1
            else:
                # zero digit, skipping
                pfx[i + 1] = pfx[i]
                xval[i + 1] = xval[i]
                cnt[i + 1] = cnt[i]

        for i, (l, r) in enumerate(queries):
            r += 1  # convert right pointer for (n + 1) based arrays
            sublen = cnt[r] - cnt[l]
            # x * sum
            ans[i] = (xval[r] - xval[l] * POW10[sublen]) * (pfx[r] - pfx[l]) % MOD

        return ans

