'''
2024/02/21 daily challenge

bitwise approach

the answer is the common prefix bits of left & right.

e.g. 0b10110101 and 0b10111011 have the common prefix 0b10110000,
       ^^^^           ^^^^                              ^^^^
left XOR right = 0b1110, we need to remove the leftmost 4bits to get the answer,
so we generate a mask 0b1111 according to previous XOR'd value's length,
and then remove bits filtered by the mask from "left AND right."
'''


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        band = left & right

        # use XOR to find the mask of suffix to be removed.
        xor = left ^ right
        mask = 0
        while(xor):
            xor >>= 1
            mask = (mask << 1) | 1

        return band - (band & mask)

