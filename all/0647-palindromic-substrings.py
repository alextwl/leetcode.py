'''
2024/02/10 daily challenge

dynamic programming approach

time=O(n**2) ver, dp used for optimizing the validation of palindrome
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # dp[i][j] indicates s[i:j+1] is a palindrome or not
        dp = [[False] * (n+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # just a shortcut for validating a possible palindrome.
                # for len(sub) > 3 we can check dp instead of reversing the sub.
                if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1

        return ans


'''
time=O(n**2) brute force approach
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            sub = ""
            for j in range(i, n):
                sub += s[j]
                if sub == sub[::-1]:
                    ans += 1

        return ans

