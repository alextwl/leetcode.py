'''
2024/05/25 daily challenge

Trie approach
'''


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.has_term = False
    
    def insert(self, word):
        node = self
        for c in word:
            i = ord(c) - ord('a')
            if node.children[i] is None:
                node.children[i] = Trie()
            node = node.children[i]
        node.has_term = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Trie()
        
        # insert all words to the root of trie
        for w in wordDict:
            root.insert(w)
        
        dp = dict()
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            output = []
            
            node = root
            for j in range(i, n):
                ci = ord(s[j]) - ord('a')
                
                if node.children[ci] is None:
                    # inefficient char in trie, word not found
                    break
                
                node = node.children[ci]
                if node.has_term:
                    target = s[i:j+1]
                    if j == n - 1:
                        # if it's the last word
                        output.append(target)
                    else:
                        # append the word to previous memorized sentenences
                        for sentence in dp.get(j + 1, []):
                            output.append(target + ' ' + sentence)
            dp[i] = output
        
        return dp.get(0, [])

