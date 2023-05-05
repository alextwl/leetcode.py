'''
2023/05/05 daily challenge

sliding window approach
'''


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 0

        # scan the initial window
        it = iter(s)
        for _ in range(k):
            if next(it) in "aeiou":
                vowels += 1
        
        max_vowels = vowels
        left = 0
        # continue scanning sliding window
        for c in it:
            # remove leftmost char in the previous window
            if s[left] in "aeiou":
                vowels -= 1
            left += 1

            if c in "aeiou":
                vowels += 1
                max_vowels = max(max_vowels, vowels)

        return max_vowels

