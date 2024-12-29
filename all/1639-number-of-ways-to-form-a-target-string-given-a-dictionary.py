'''
2023/04/16 daily challenge

dynamic programming approach
'''

from string import ascii_lowercase

MODULO = 1_000_000_007  # 10**9+7


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(words[0]), len(target)

        # count characters for each index
        counts = [{c: 0 for c in ascii_lowercase} for _ in range(m)]
        for w in words:
            for i, c in enumerate(w):
                counts[i][c] += 1

        # dp[i] == ways to form target[:i]
        dp = [0] * (n+1)
        dp[0] = 1  # initial value: only 1 way to form target[:0] == empty string

        for i in range(m):
            for j in range(n-1, -1, -1):
                '''
                ways to form target[:j+1] == ways to form target[:j] * the count of target[j] we picked up from index i.
                '''
                dp[j+1] += dp[j] * counts[i][target[j]]
        '''
        For example 1:

        picking index 0 from all words
        dp[3] += dp[2] * counts[0][a] == 0 (no way to form target[:3] if target[2] came from words[*][0])
        0 += 0 * 1
        dp[2] += dp[1] * counts[0][b] == 0 (no way to form target[:2] if target[1] came from words[*][0])
        0 += 0 * 1
        dp[1] += dp[0] * counts[0][a] == 1 (1 way to form target[:1] if target[0] came from "acca"[0])
        0 += 1 * 1

        picking index 1 from all words
        dp[3] += dp[2] * counts[1][a] == 0 (no way to form target[:3] if target[2] came from words[*][1])
        0 += 0 * 1
        dp[2] += dp[1] * counts[1][b] == 1 (1 way to form target[:2] if target[1] came from "bbbb"[1])
        0 += 1 * 1
        dp[1] += dp[0] * counts[1][a] == 2 (1 way to form target[:1] if target[0] came from "caca"[1] + previous dp[1] == 2 ways)
        1 += 1 * 1

        picking index 2 from all words
        dp[3] += dp[2] * counts[2][a] == 0 (no way to form target[:3] if target[2] came from words[*][2])
        0 += 1 * 0
        dp[2] += dp[1] * counts[2][b] == 3 (1 way to form target[:2] if target[1] came from "bbbb"[2] * dp[1])
        1 += 2 * 1
        dp[1] += dp[0] * counts[2][a] == 2 (no way to form target[:1] if target[0] came from words[*][2])
        2 += 1 * 0

        picking index 3 from all words
        dp[3] += dp[2] * counts[3][a] == 6 (2 ways to form target[:3] if target[2] came from "acca"[3] & "caca"[3] * dp[2]) --> final ans
        0 += 3 * 2
        dp[2] += dp[1] * counts[3][b] == 5 (1 ways to form target[:2] if target[1] came from "bbbb"[3] * dp[1]) --> unreasonable, won't use it
        3 += 2 * 1
        dp[1] += dp[0] * counts[3][a] == 4 (2 ways to form target[:1] if target[0] came from "acac"[3] & "caca"[3] * dp[0]) --> unreasonable, won't use it
        2 += 1 * 2
        '''

        return dp[-1] % MODULO


'''
2024/12/29 daily challenge

dynamic programming approach (recursive ver)
'''


import collections
import functools


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        kcnts = [collections.Counter(k_chars) for k_chars in zip(*words)]
        m, n = len(target), len(kcnts)

        @functools.cache
        def dp(i, k):
            if i == m:
                return 1
            if k == n:
                return 0

            ways = 0
            # select k-th char
            if target[i] in kcnts[k]:
                ways += kcnts[k][target[i]] * dp(i+1, k+1)
            # not select k-th char
            ways += dp(i, k+1)
            return ways % 1_000_000_007

        return dp(0, 0)

