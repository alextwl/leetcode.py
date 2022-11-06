# 2019 submission

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rn = 0
        for _ in range(32):
            rn = (rn<<1) + (n&1)
            n = n>>1

        return rn
