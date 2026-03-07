'''
2026/03/07 daily challenge

sliding window approach
'''


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        flips = 0
        next_bit = 0  # the target value of next bit
        for v in map(int, s):
            if v != next_bit:
                flips += 1
            next_bit ^= 1

        # min(flips with s[0] == '0', flips with s[0] == '1')
        min_flips = min(flips, n - flips)
        if n & 1 == 0:
            # even-length input, no need to run sliding window.
            # no matter how many times we applied type-1 operations
            # to an even-length s, the count of type-2 operations
            # remains unchanged.
            return min_flips

        next_bit = 0
        # sliding window:
        # it's actually the 2nd part when the full iteration range is s + s.
        # here we slide the window of size n.
        # consider the changes when applying type-1 ops to the following bits.
        for v in map(int, s):
            if v != next_bit:
                flips -= 1
                min_flips = min(min_flips, flips)
            else:
                flips += 1
                min_flips = min(min_flips, n - flips)
            next_bit ^= 1

        return min_flips

