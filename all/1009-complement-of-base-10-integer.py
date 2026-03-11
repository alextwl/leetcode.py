'''
2026/03/11 daily challenge

flip each bit.
'''


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        v = (n & 1) ^ 1
        n >>= 1
        i = 1
        while n:
            if (n & 1) == 0:
                v |= 1 << i
            n >>= 1
            i += 1
        return v

