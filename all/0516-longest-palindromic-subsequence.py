'''
dynamic programming approach

learnt from
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/1468396/C%2B%2BPython-2-solutions%3A-Top-down-DP-Bottom-up-DP-O(N)-Space-Clean-and-Concise
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99129/Python-DP-O(n)-space-O(n2)-time

the idea is trying to expand the palindromic substring
from every character, starts from the end of string (bottom-up).
'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        '''
        it stores lengthes of maximum palindromic string with ranges.
        dp[i][j] means the max length of palindromic within s[i] to s[j].
        '''
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            # every character is also a length-1 palindromic string
            dp[i][i] = 1
            
            # let's try to expand the substring from s[i] to s[i:n].
            for j in range(i+1, n):
                '''
                no need to do boundary check for dp[i+1].
                it won't enter the loop if i+1 >= n.
                '''
                if s[i] == s[j]:
                    '''
                    if s[i] and s[j] were the same char, we can expand the substring
                    from s[i+1:j] to s[i:j+1] (which is s[i+1]..s[j-1] to s[i]..s[j]).
                    the substring grows 2 chars (that's why it plus 2.)
                    and we'll expand the existed maximum palindromic substring from dp[i+1][j-1].
                    '''
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    '''
                    or we'll delete some or all elements betweem them (deletes s[i] or s[j]),
                    and choose the existed maximum palindromic substring
                    from s[i+1]..s[j] or s[i]..s[j-1].
                    '''
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]

