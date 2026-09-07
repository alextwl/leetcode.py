'''
2026/09/07 daily challenge

dynamic programming approach
'''


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # dummy base count (empty subseq) to be inherited
        last_seen = {}  # last_seen[c] = last seen index of char c

        for i, c in enumerate(s):
            dp[i + 1] = dp[i] * 2 - (dp[last_seen[c]] if c in last_seen else 0)
            last_seen[c] = i

        return (dp[-1] - 1) % 1_000_000_007

