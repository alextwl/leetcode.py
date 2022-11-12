'''
linear search approach

the goal is to find all chars of s in t in order,
we can only iterate over the full length of t.

time=O(mn)
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            # an empty s-string is always a subsequence of any t-string.
            return True
        if not t:
            # an empty t-string has no non-empty s-subsequence.
            return False

        i = 0  # index of s.
        
        for c in t:
            if c == s[i]:
                # search next char of s.
                i += 1
                if i >= len(s):
                    # all chars of s found.
                    return True

        # s not found.
        return False

