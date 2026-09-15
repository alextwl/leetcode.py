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


'''
greedy method approach

always select shortest palindrome greedily
'''


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        if k == 1:
            return n

        def is_pd(start):
            # return the next index of s if a minimal substring
            # starting from s[i] is a palindrome.
            #
            # for k-length substring
            left_bound, right_bound = start, start + k - 1
            if left_bound < 0 or right_bound >= n:
                return -1
            l, r = left_bound, right_bound
            while l < r:
                if s[l] != s[r]:
                    break
                l += 1
                r -= 1
            else:
                return right_bound + 1
            
            # for (k+1)-length substring
            left_bound, right_bound = start, start + k
            if left_bound < 0 or right_bound >= n:
                return -1
            l, r = left_bound, right_bound
            while l < r:
                if s[l] != s[r]:
                    break
                l += 1
                r -= 1
            else:
                return right_bound + 1
            # not a palindrome
            return -1

        ans = 0
        i = 0
        while i < n:
            next_idx = is_pd(i)
            if next_idx == -1:
                i += 1
            else:
                i = next_idx
                ans += 1

        return ans

