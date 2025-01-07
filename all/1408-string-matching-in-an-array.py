'''
2025/01/07 daily challenge

sorting + brute force approach
'''


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: -len(x))
        ans = []
        for i, w0 in enumerate(words):
            for j, w1 in enumerate(words):
                if i == j:
                    continue
                if len(w0) <= len(w1):
                    if w0 in w1:
                        ans.append(w0)
                        break
                else:
                    break
        return ans


'''
Trie + frequency counting approach

it inserts all suffices to the Trie, so it costs.
'''


class Trie:
    def __init__(self):
        self.freq = 0
        self.children = dict()


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        root = Trie()
        ans = []

        # build suffix trie
        for word in words:
            for i in range(len(word)):
                suffix = word[i:]
                node = root
                for c in suffix:
                    if c not in node.children:
                        node.children[c] = Trie()
                    node = node.children[c]
                    node.freq += 1

        # match substring
        for word in words:
            node = root
            for c in word:
                node = node.children[c]
            if node.freq > 1:
                # target word is not itself, it's a valid substring.
                ans.append(word)

        return ans

