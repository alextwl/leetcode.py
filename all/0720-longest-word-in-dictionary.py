'''
trie approach
'''


ASCII_A = ord('a')


class Trie:
    def __init__(self):
        self.eof = False
        self.children = [None] * 26
    
    def insert(self, s):
        if not s:
            self.eof = True
            return
        b = ord(s[0]) - ASCII_A
        if self.children[b] is None:
            self.children[b] = Trie()
        self.children[b].insert(s[1:])
    
    def get_longest(self):
        ret = []
        for i, child in enumerate(self.children):
            if child is None or child.eof == False:
                continue
            curr = [i] + child.get_longest()
            if len(curr) > len(ret) or (len(curr) == len(ret) and curr < ret):
                ret = curr
        return ret


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for w in words:
            root.insert(w)
        longest = root.get_longest()
        return ''.join(chr(a + ASCII_A) for a in longest)

