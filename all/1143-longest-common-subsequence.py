'''
dynamic programming approach

learnt from the official hints and
https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis

time=O(mn), space=O(mn)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        dp[i][j] = the length of the longest common subsequence of text1[0..i] and text2[0..j]
        '''
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i, char1 in enumerate(text1):
            for j, char2 in enumerate(text2):
                '''
                Implement hint 2's conditions.
                '''
                if char1 == char2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    '''
                    if text1[i] != text[2],
                    we don't accumulate the length of the common subsequence,
                    thus we inherit the maximum of the LCS
                    from LCS(text1[0..i] & text2[0..j+1]) or LCS(text1[0..i+1] & text2[0..j])
                    '''
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]

