'''
2026/03/06 daily challenge

only ones expected in the string after trailing zeros stripped
'''


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '0' not in s.rstrip('0')


'''
linear search approach
'''


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n and s[i] == '1':
            i += 1
        while i < n and s[i] == '0':
            i += 1
        return i == n

