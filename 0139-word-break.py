'''
dynamic programming approach

learnt from official solution 4
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # convert to set() makes it searching faster
        
        '''
        dp[] memorize index next to a char
        which is a char in s and also an end char of a word in wordDict.
        
        in other words, for any s[j:i] in wordDict, dp[j] = dp[i] = True.
        '''
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                '''
                a valid s[j:i] must follow another valid word (as a previous valid s[j:i]) which ends at s[j-1],
                so we need to check dp[j] == True first.
                
                the reason of j starting from 0 is because wordDict may have words starting from s[0].
                '''
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        '''
        if the last segment of s could form a valid word in wordDict,
        then s can be splited into valid dictionary words
        because we've check each segment from the beginning of s.
        '''
        return dp[-1]
