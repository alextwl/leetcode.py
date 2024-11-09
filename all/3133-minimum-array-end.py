'''
2024/11/09 daily challenge

bit manipulation approach
'''


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # exclude x itself because we want to build bit combinations between
        # 0..x-1, not 1..x, so we reduce **n** by 1.
        # suffix bits of the first number nums[0] should equal to x.
        n -= 1

        # calculate the number of variants of valid suffices.
        suffix_var = 2 ** (x.bit_length() - x.bit_count())
        if suffix_var == 1:
            return n << x.bit_length() | x
        # build prefix by quotient, suffix by remainder
        q, r = divmod(n, suffix_var)

        # fill remainder bits to zero bits in the suffix
        suffix = 0
        v = x
        for i in range(x.bit_length()):
            b = v & 1 << i
            if b:
                suffix |= b
            else:
                # if the current bit of suffix was zero,
                # try to copy a bit from the remainder instead.
                if r & 1:
                    suffix |= 1 << i
                r >>= 1

        return q << x.bit_length() | suffix

