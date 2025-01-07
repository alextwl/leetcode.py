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


'''
Knuth-Morris-Pratt (KMP) approach
'''


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        # kmp string matching
        for i, w0 in enumerate(words):
            # build LPS
            lps = [0] * len(w0)
            k = 1
            l = 0
            while k < len(w0):
                if w0[k] == w0[l]:
                    l += 1
                    lps[k] = l
                    k += 1
                else:
                    if l > 0:
                        l = lps[l-1]
                    else:
                        k += 1
            # match
            for j, w1 in enumerate(words):
                if i == j:
                    continue
                k0 = 0  # substring index
                k1 = 0  # target index
                while k1 < len(w1):
                    if w0[k0] == w1[k1]:
                        k0 += 1
                        k1 += 1
                        if k0 == len(w0):
                            ans.append(w0)
                            break
                    else:
                        if k0 > 0:
                            k0 = lps[k0 - 1]
                        else:
                            k1 += 1
                else:
                    continue
                break
        return ans

