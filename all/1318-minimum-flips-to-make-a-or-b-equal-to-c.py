'''
2023/06/07 daily challenge
'''

import itertools

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def toBin(x):
            lst = []
            while(x):
                lst.append(x&1)
                x >>= 1
            return lst
        la = toBin(a)
        lb = toBin(b)
        lc = toBin(c)
        
        flips = 0
        for x, y, z in itertools.zip_longest(la, lb, lc, fillvalue=0):
            if z:
                if not(x or y):
                    flips += 1
            else:
                flips += x + y  # flip all 1-bits
        return flips


'''
non-zip ver
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while(a or b or c):
            if c & 1:
                if not((a&1) or (b&1)):
                    flips += 1
            else:
                flips += (a&1) + (b&1)
            a >>= 1
            b >>= 1
            c >>= 1

        return flips

