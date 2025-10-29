'''
divide and conquer approach
'''


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""
        
        charset = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in charset:
                # divide s by excluding ugly c
                return max(self.longestNiceSubstring(s[:i]),
                           self.longestNiceSubstring(s[i+1:]),
                           key=len)
        return s  # it's a nice (sub)string.

