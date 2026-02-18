'''
only ones expected in the string after trailing zeros stripped
'''


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '0' not in s.rstrip('0')

