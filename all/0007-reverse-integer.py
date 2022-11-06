# 2019 submission

MAX_INT32 = 2**31 - 1 
MIN_INT32 = -2**31

def revint(i):
    s = str(i)
    us = s[1:] if s[0] == '-' else s
    rs = 0 
    for idx, c in enumerate(us):
        rs += int(c)*(10**idx)
    rs = -rs if s[0] == '-' else rs
    if rs > MAX_INT32:
        return 0
    if rs < MIN_INT32:
        return 0
    return rs


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return revint(x)
