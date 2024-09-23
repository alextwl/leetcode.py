'''
2023/09/02 daily challenge

dynamic programming approach
'''

import collections


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        
        '''
        build a dict by word's length
        '''
        dictByLen = collections.defaultdict(set)
        for w in dictionary:
            dictByLen[len(w)].add(w)
        
        wordLens = sorted(dictByLen.keys(), reverse=True)
        
        '''
        dp[i] = the minimum extra chars in [0, i]
        base case: the empty string
        '''
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            '''
            try to match dict, from longest word to shortest word.
            '''
            for m in wordLens:
                if (j := i - m) < 0:
                    # insufficient length of [0:i] to match a m-length of word
                    continue
                if s[j:i] in dictByLen[m]:
                    '''
                    s[j:i] is in the dictionary, so we can break s[0:i] into
                    s[0:j] and s[j:i] and inherit extra chars from dp[j].
                    '''
                    dp[i] = min(dp[i], dp[j])
            '''
            also try to break s[0:i] into s[0:i-1] and s[i-1:i]
            and inherit extra chars from dp[i-1] plus extra s[i-1].
            '''
            dp[i] = min(dp[i], dp[i-1] + 1)

        return dp[-1]


'''
2024/09/23 daily challenge

Trie + dynamic programming approach
'''


class Trie:
    def __init__(self, words = None):
        self.children = {}
        self.end_of_word = False

        if words is not None:
            for w in words:
                node = self
                for c in w:
                    if c not in node.children:
                        node.children[c] = Trie()
                    node = node.children[c]
                node.end_of_word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary)

        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # assume s[i] is an extra char
            dp[i] = dp[i+1] + 1
            # search the trie
            node = trie
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.end_of_word:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]

