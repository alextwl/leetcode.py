'''
2026/07/28 daily challenge

counter + sorting approach
'''


import collections


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ctr = collections.Counter(s)
        center = ""
        prefix = []
        for key in sorted(ctr.keys()):
            if ctr[key] & 1:
                center = key
            prefix.append(key * (ctr[key] >> 1))
        return ''.join(prefix) + center + ''.join(reversed(prefix))

