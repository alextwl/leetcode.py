'''
2025/07/02 daily challenge

dynamic programming + prefix sum approach

learnt from official editorial:
https://leetcode.com/problems/find-the-original-typed-string-ii/editorial/#approach-dynamic-programming--prefix-sum-optimization
'''


import functools
import itertools


MOD = 1_000_000_007


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # build the frequency of each substring of same chars.
        running_len = 1
        freq = []
        for prev, curr in itertools.pairwise(word):
            if prev == curr:
                running_len += 1
            else:
                freq.append(running_len)
                running_len = 1
        freq.append(running_len)

        # calculate the total number of possible strings without condition
        ans = functools.reduce(lambda x, y: x * y % MOD, freq)

        # shortcut: no more possible string length < k
        if len(freq) >= k:
            return ans
        
        # dynamic programming: subtract ans by length 1 to length k
        # f[j] = construct j-length string from (i+1 by for-loop) elements of freq
        f = [0] * k
        f[0] = 1  # base case: 1 way to construct empty string
        g = [1] * k
        for i, cnt in enumerate(freq):
            ff = [0] * k
            for j in range(1, k):
                ff[j] = g[j - 1]
                if j - cnt - 1 >= 0:
                    # subtract by prefix sum to get exact j-length ways
                    ff[j] = (ff[j] - g[j - cnt - 1]) % MOD
            # prefix sum of sigma f
            gg = [0] * k
            gg[0] = ff[0]
            for j in range(1, k):
                gg[j] = (gg[j - 1] + ff[j]) % MOD
            f, g = ff, gg
        # g[k-1] is the prefix sum of ways of [1...k-1] length strings
        return (ans - g[k - 1]) % MOD

