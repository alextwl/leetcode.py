'''
2026/09/15 daily challenge

dynamic programming approach

find all possible palindromes and maximize the number of substrings by dp.
'''


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # is_pd[i][j] = true if s[i..j] is a palindrome
        is_pd = [[False] * n for _ in range(n)]
        for sublen in range(1, n + 1):
            for i in range(n - sublen + 1):
                j = i + sublen - 1
                if s[i] == s[j] and (sublen <= 2 or is_pd[i + 1][j - 1]):
                    is_pd[i][j] = True

        dp = [0] * (n + 1)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1]
            for i in range(j - k + 1):
                if is_pd[i][j - 1]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1]

