'''
2023/07/30 daily challenge

dynamic programming approach

learnt from official solution
https://leetcode.com/problems/strange-printer/solution/

also see the proofs in official solution for more detail.
'''


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        '''
        dp[l][r] = the minimum operations to represent the substring s[l..r] (inclusive)
        
        the maximum is n for printing each single character per round.
        '''
        dp = [[n] * n for _ in range(n)]
        
        '''
        manipulate substrings from the shortest to the longest.
        '''
        for length in range(1, n+1):
            '''
            before we printing s[r] within s[l..r]
            '''
            for l in range(n - length + 1):
                r = l + length - 1
                '''
                check the sub-substring s[j..i..r] for l <= j <= i < r for any s[i] != s[r]
                '''
                j = -1
                for i in range(l, r):
                    if s[i] != s[r] and j == -1:
                        j = i
                    if j != -1:
                        '''
                        if dp[j..i..r] + 1 (for overriding s[j..i] part) has smaller operation counts, honor it.
                        '''
                        dp[l][r] = min(dp[l][r],
                                       1 + dp[j][i] + dp[i+1][r])
                if j == -1:
                    # s[l..r] is already a sequence of the same character, no need to print.
                    dp[l][r] = 0

        return dp[0][n-1] + 1  # for the 1st print not counted in the DP loop.

