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


'''
2023/08/04 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        q = collections.deque([0])  # start from index 0 of s.
        visited = set()

        # BFS
        while(q):
            node = q.popleft()

            if node == len(s):
                # we've reached the end of s, the word break is possible.
                return True

            for child in range(node+1, len(s)+1):
                '''
                search if a substring from s[node+1] to s[len(s)-1] existed in the wordDict.
                '''
                if child in visited:
                    '''
                    we can confirm that substring ended at s[child-1] can be segmented,
                    no need to check and queue it again.
                    '''
                    continue

                if s[node:child] in words:
                    q.append(child)  # queue it to search next word started from s[child]
                    visited.add(child)

        # we cannot reach the end of s in the previous searches.
        return False

