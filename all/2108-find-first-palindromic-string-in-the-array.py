'''
2024/02/13 daily challenge

greedy method + reverse string approach
'''


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""

