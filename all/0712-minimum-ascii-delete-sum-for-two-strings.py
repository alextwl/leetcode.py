'''
2023/07/31 daily challenge

dynamic programming approach

learnt from official solution
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/

also see the editoral's official solution for more optimized approaches.

it's also a kind of longest common sequence (LCS) problem.
'''


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # convert all chars to ASCII codes in advance
        a1 = [ord(c) for c in s1]
        a2 = [ord(c) for c in s2]
        
        '''
        dp[i][j] = the minimum cost to let s1[:i] and s2[:j] to be equivalent.
        '''
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        '''
        base case:
        delete all chars from all s1's substrings to be equal to an empty s2, and vice versa.
        dp[0][0] = "" -> "" costs nothing.
        dp[1][0] = s1[:1] -> "" costs the previous cost (dp[0][0]) + ord(s1[0]),
        dp[2][0] = s1[:2] -> "" costs the previous cost (dp[1][0]) + ord(s1[1]),
        etc.
        '''
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + a1[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + a2[j-1]
        
        # Bellman equation
        for i in range(1, m+1):
            for j in range(1, n+1):
                if a1[i-1] == a2[j-1]:
                    # two chars are equivalent, no need to delete
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # delete the char from a string who costs smaller.
                    dp[i][j] = min(a1[i-1] + dp[i-1][j],
                                   a2[j-1] + dp[i][j-1])

        return dp[m][n]

