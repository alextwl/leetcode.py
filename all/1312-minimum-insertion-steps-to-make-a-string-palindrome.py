'''
2023/04/22 daily challenge

dynamic programming approach (2D space ver)

learnt from
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/solutions/3442303/python-java-c-simple-solution-easy-to-understand/ (1D space)

similar to problem 1143 (LCS)
'''

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        '''
        dp[i][j] = the minimum insertion number to make s[i:j+1] a palindrome.
        '''
        dp = [[0] * n for _ in range(n)]

        '''
        break s into characters (subproblems) and try to expand s[i].
        '''
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    # s[i:j+1] is already a palindrome
                    dp[i][j] = dp[i+1][j-1]
                else:
                    '''
                    insertion needed to make dp[i][j]:
                    (1) new char + dp[i+1][j], or
                    (2) dp[i][j-1] + new char.
                    '''
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

        # the minimum insertion number for the full string (dp[0][n-1] -> s[0:n]) is the answer
        return dp[0][-1]

