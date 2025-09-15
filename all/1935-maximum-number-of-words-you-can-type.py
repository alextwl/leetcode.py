'''
2025/09/15 daily challenge
'''


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        if len(brokenLetters) == 26:
            return 0
        if len(brokenLetters) == 0:
            return len(text.split(' '))

        ans = 0
        for word in text.split(' '):
            for c in word:
                if c in brokenLetters:
                    break
            else:
                ans += 1
        return ans

