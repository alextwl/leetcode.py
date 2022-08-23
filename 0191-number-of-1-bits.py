class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            # n & (n-1) removes rightmost '1' digit
            # e.g. 1101100 & 1101011 = 1101000
            #      1101000 & 1100111 = 1100000
            #      1100000 & 1011111 = 1000000
            #      1000000 & 0111111 = 0
            # the number of operations also equal to number of 1-bits.
            n &= (n-1)
            ans += 1
        return ans
