'''
2024/09/12 daily challenge

set approach
'''


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for w in words:
            if not (set(w) - allowed):
                ans += 1
        return ans

