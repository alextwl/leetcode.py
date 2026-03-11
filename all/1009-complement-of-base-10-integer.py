'''
2026/03/11 daily challenge

flip each bit.

same to problem 476
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


'''
XOR with the same bit length of all-one code
'''


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # corner
        if n == 0: return 1
        return n ^ ((1 << n.bit_length()) - 1)

