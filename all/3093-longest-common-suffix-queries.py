'''
2026/05/28 daily challenge

Trie approach

convert the problem to longest common **prefix** queries by reversing all words.
'''


class Trie:
    def __init__(self, w_idx, w_len):
        self.children = {}
        self.w_idx = w_idx
        self.w_len = w_len
    
    def add(self, word, w_idx, w_len):
        if w_len < self.w_len:
            # save the smallest even if no common prefix matches.
            self.w_idx = w_idx
            self.w_len = w_len
        
        node = self
        for c in reversed(word):
            if c not in node.children:
                node.children[c] = Trie(w_idx, w_len)
                node = node.children[c]
            else:
                node = node.children[c]
                if w_len < node.w_len:
                    # the earlist & smallest one prevails
                    node.w_idx = w_idx
                    node.w_len = w_len

    def query(self, word):
        node = self
        for c in reversed(word):
            if c not in node.children:
                break
            node = node.children[c]
        return node.w_idx


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        t = Trie(0, len(wordsContainer[0]))
        for i, w in enumerate(wordsContainer):
            t.add(w, i, len(w))
        ans = []
        for w in wordsQuery:
            ans.append(t.query(w))
        return ans

