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
                    # shortest prefix found, return only the prefix part.
                    return word[:i+1]
            else:
                # prefix not found, stop searching
                break
        # prefix of word not found in the dictionary,
        # so just output it untouched.
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()

        for w in dictionary:
            root.insert(w)

        ans = []
        for w in sentence.split():
            ans.append(root.query(w))

        return ' '.join(ans)

