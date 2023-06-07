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
                if x:
                    flips += 1
                if y:
                    flips += 1
        return flips
    
