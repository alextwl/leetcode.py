'''
2025/01/11 daily challenge

check the length of input string and count its odds.

for k palindromes they can fill at most k single alphabets.
'''


import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        ctr = collections.Counter(s)
        odds = sum(v & 1 for v in ctr.values())
        return odds <= k

