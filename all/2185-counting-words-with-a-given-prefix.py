'''
2025/01/09 daily challenge

oneliner ver
'''


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w[:len(pref)] == pref for w in words)

