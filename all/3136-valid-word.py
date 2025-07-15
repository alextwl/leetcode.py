'''
2025/07/15 daily challenge

note the input is arbitrary and may include '@', '#', and '$'.
all conditions for a word must be validated.
'''


class Solution:
    def isValid(self, word: str) -> bool:
        vowel_found = False
        consonant_found = False
        for c in word:
            if c in "aeiouAEIOU":
                vowel_found = True
            elif c.isalpha():
                consonant_found = True
            elif not c.isdigit():
                return False

        return vowel_found and consonant_found and len(word) >= 3

