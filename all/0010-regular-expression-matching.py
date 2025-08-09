'''
recursion approach
'''


import functools


class Solution:
    @functools.cache
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True
        if p == '':
            return False

        n = len(s)
        # determine if it's a wildcard or a single char matching
        c = p[0]
        if len(p) >= 2 and p[1] == '*':
            # wildcard
            next_p = p[2:]
            i = 0
            # skip matching any char because of wildcard
            if self.isMatch(s, next_p):
                return True
            # match chars
            while i < n and (c == '.' or s[i] == c):
                if self.isMatch(s[i+1:], next_p):
                    return True
                i += 1
        else:
            # single match
            if s == '':
                # insufficient char to be matched
                return False
            next_p = p[1:]
            # match single char
            if c == '.' or s[0] == c:
                return self.isMatch(s[1:], next_p)

        return False

