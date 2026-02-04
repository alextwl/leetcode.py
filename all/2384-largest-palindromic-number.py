'''
counter approach
'''


import collections


class Solution:
    def largestPalindromic(self, num: str) -> str:
        ctr = collections.Counter(num)
        center = max((k for k, v in ctr.items() if v & 1), default="")
        prefix = []
        for k in sorted(ctr.keys(), reverse=True):
            half = ctr[k] // 2
            if half:
                prefix.append(k * half)
        if prefix and prefix[0][0] == '0':
            if center:
                return center
            else:
                return "0"
        return ''.join(prefix) + center + ''.join(prefix[::-1])

