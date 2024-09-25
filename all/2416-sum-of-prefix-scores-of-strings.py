'''
2024/09/25 daily challenge

Trie approach
'''


class Trie:
    def __init__(self):
        self.children = {}
        self.score = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # import words to the trie
        root = Trie()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
                node.score += 1

        # sum up the scores
        ans = []
        for w in words:
            score = 0
            node = root
            for c in w:
                node = node.children[c]
                score += node.score
            ans.append(score)

        return ans

