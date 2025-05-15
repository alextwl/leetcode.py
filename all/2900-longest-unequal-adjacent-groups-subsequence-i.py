'''
2025/05/15 daily challenge
'''


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []

        prev = None
        for c, g in zip(words, groups):
            if prev == g:
                continue
            prev = g
            ans.append(c)

        return ans

