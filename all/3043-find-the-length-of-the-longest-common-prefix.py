'''
2024/09/24 daily challenge
2026/05/21 daily challenge

set approach
'''


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def arr2set(arr):
            s = {""}  # an empty string is necessary for no common prefix case
            for w in map(str, arr):
                for i in range(1, len(w)):
                    s.add(w[:i])
                s.add(w)
            return s
        
        s1, s2 = arr2set(arr1), arr2set(arr2)

        return max(map(len, s1 & s2))


'''
yet another set approach
'''


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pfx = set()

        for w in map(str, arr1):
            for i in range(1, len(w) + 1):
                pfx.add(w[:i])

        max_len = 0
        for w in map(str, arr2):
            # we search longer prefix only
            for i in range(max_len + 1, len(w) + 1):
                if w[:i] in pfx:
                    max_len = i
                else:
                    break

        return max_len


'''
Trie ver
'''


class Trie:
    def __init__(self, arr = None):
        self.children = {}
        if arr is not None:
            for w in map(str, arr):
                node = self
                for c in w:
                    if c not in node.children:
                        node.children[c] = Trie()
                    node = node.children[c]
    
    def get_prefix_len(self, w):
        node = self
        prefix_len = 0
        for c in str(w):
            if c in node.children:
                node = node.children[c]
                prefix_len += 1
            else:
                break
        return prefix_len


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie(arr1)
        return max(map(trie.get_prefix_len, arr2))

