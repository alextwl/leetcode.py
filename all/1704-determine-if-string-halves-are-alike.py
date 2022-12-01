'''
2022/12/01 daily challenge

count vowels approach
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        patterns = "aeiouAEIOU"
        bstart = len(s)//2
        vowel_count = 0
        
        for c in s[:bstart]:
            if c in patterns:
                vowel_count += 1
        for c in s[bstart:]:
            if c in patterns:
                vowel_count -= 1
        
        return vowel_count == 0

