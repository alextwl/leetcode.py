'''
2025/01/15 daily challenge

bit manipulation approach
'''


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_counts = num2.bit_count()
        ans = 0
        # try to cancel set bits from the rightmost of num1
        for b in bin(num1)[2:]:
            ans <<= 1
            if b == '1' and set_counts:
                ans += 1
                set_counts -= 1

        # if not enough set bits in the answer, try to fill from the leftmost
        # in order to minimize the result of x^num1.
        mask = 1
        while set_counts:
            if num1 & mask == 0 and ans & mask == 0:
                ans += mask
                set_counts -= 1
            mask <<= 1

        return ans

