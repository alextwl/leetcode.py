'''
2026/02/17 daily challenge

combinations + bitwise operation + string format approach
'''


import itertools


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for sbits in itertools.combinations(range(10), turnedOn):
            v = 0
            for b in sbits:
                v |= 1 << b
            h = v >> 6
            mm = v & 0b111111
            if h > 11 or mm > 59:
                # skip invalid timestamps
                continue
            ans.append("%d:%02d" % (h, mm))
        return ans

