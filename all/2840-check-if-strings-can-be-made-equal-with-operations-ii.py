'''
2026/03/30 daily challenge

counter approach

verify if same parity (even/odd) indices had
equivalent amount of characters in s1 & s2.

same to problem 2839 plus larger inputs
'''


import collections


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return collections.Counter(s1[::2]) == collections.Counter(s2[::2]) and \
            collections.Counter(s1[1::2]) == collections.Counter(s2[1::2])

