'''
2024/06/07 daily challenge

Trie approach
'''


import collections


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.end = False
    
    def insert(self, word):
        t = self
        for c in word:
            t = t.children[c]
        t.end = True
    
    def query(self, word):
        t = self
        for i, c in enumerate(word):
            if c in t.children:
                t = t.children[c]
                if t.end:
                    return word[:i+1]
            else:
                break

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()

        for w in dictionary:
            root.insert(w)

        ans = []
        for w in sentence.split():
            if w[0] in root.children:
                ans.append(root.query(w))
            else:
                ans.append(w)

        return ' '.join(ans)

