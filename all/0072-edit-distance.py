'''
dynamic programming approach

learnt from
https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition

similar to the problem 1143.

calculate the number of operations
when the characters is not part of the longest common subsequence.
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        dp[i][j] = the operations needed for converting word1[0..i] to word2[0..j]
        '''
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        '''
        it needs i ops when converting word1[0..i] to empty word2. (remove i chars.)
        it needs j ops when converting empty word1 to word2[0..j]. (insert j chars.)
        '''
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        
        for i, char1 in enumerate(word1):
            for j, char2 in enumerate(word2):
                if char1 == char2:
                    # when the chars are the same, no operation is done.
                    dp[i+1][j+1] = dp[i][j]
                else:
                    '''
                    we need to do one of the permitted operations here.
                    min(insert, delete, replace)
                    '''
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        
        return dp[-1][-1]

