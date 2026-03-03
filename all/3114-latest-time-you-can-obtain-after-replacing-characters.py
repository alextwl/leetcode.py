'''
enumeration approach
'''


class Solution:
    def findLatestTime(self, s: str) -> str:
        hh, h, _, mm, m = s
        if hh == "?":
            hh = '1' if h in "?01" else '0'
        if h == "?":
            h = '9' if hh == '0' else '1'
        if mm == "?":
            mm = '5'
        if m == "?":
            m = '9'
        return hh + h + ":" + mm + m

