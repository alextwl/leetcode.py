'''
2026/05/26 daily challenge

hash set + exhaustive method approach
'''


# generate all upper and lower alphabets
UPPERS = [chr(ord('A') + i) for i in range(26)]
LOWERS = [chr(ord('a') + i) for i in range(26)]


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set(word)
        ans = 0
        # check all alphabets
        for upper, lower in zip(UPPERS, LOWERS):
            if upper in seen and lower in seen:
                ans += 1
        return ans

