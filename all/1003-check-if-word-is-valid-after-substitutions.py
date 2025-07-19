'''
2025/07/19 daily challenge

reverse simulation approach
'''


class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) >= 3 and 'abc' in s:
            s = s.replace('abc', '')
        return s == ''

