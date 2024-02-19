'''
2024/02/19 daily challenge

bitwise approach

note any non-positive integer is not a power of two.
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1

