class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # find different bits by XOR
        n = x ^ y
        # count number of 1 bits == hamming distance
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans
