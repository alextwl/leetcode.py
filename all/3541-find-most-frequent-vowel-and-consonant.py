'''
2025/09/13 daily challenge

counter approach
'''


import collections


class Solution:
    def maxFreqSum(self, s: str) -> int:
        ctr = collections.Counter(s)
        vowel = consonant = 0
        for k, v in ctr.most_common():
            if k in "aeiou":
                vowel = v
                break
        for k, v in ctr.most_common():
            if k not in "aeiou":
                consonant = v
                break
        return vowel + consonant

