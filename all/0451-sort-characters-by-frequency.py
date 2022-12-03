'''
2022/12/03 daily challenge

pythonic counter approach

count the occurance of case-sensitive alphabets
and then regenerate the string in descending occurance order.
'''

import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = sorted(collections.Counter(s).items(), key=lambda v: -v[1])
        return ''.join(c * k for c, k in freq)

