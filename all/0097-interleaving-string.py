'''
2023/08/25 daily challenge

dynamic programming approach
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        # filter the failure case of mismatch sum of lengthes.
        if n1 + n2 != n3:
            return False
        
        '''
        use dp space to memorize the validation between 2 indexes.
        
        dp[i][j] = whether s3[0:i+j] is formed by an interleaving of s1[0:i] & s2[0:j]
        
        the base case is interleaving dp[0][0] the empty strings can form the target empty string.
        '''
        dp = [[True for _ in range(n2+1)] for _ in range(n1+1)]
        
        '''
        test if we can form s3 by s1 or s2 exclusively.
        '''
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        '''
        O(mn) validation
        '''
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                '''
                pick s1[i-1] or s2[j-1] to match s3[i+j-1]
                after prefix dp[i-1][j] or dp[i][j-1]
                '''
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                            (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]

