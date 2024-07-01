'''
bit manipulation approach

observe some values and its minimum op0 & op1:

1 -> 0b1 -> op0=1  (0, 1)
2 -> 0b10 -> op0=1, op1=1  (0, 1, 2)
3 -> 0b11 -> op0=2, op1=1  (0, 1, 2, 3)
4 -> 0b100 -> op0=1, op1=2  (0, 1, 2, 4)
5 -> 0b101 -> op0=2, op1=2  (0, 1, 2, 4, 5)
6 -> 0b110 -> op0=2, op1=2  (0, 1, 2, 3, 6)
7 -> 0b111 -> op0=3, op1=2  (0, 1, 2, 3, 6, 7)
8 -> 0b1000 -> op0=1, op1=3  (0, 1, 2, 4, 8)
...

we can find that op1 for each value is the bit length minus MSB,
and op0 is the count of 1's bits.
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op0 = 0
        max_op1 = 0

        for v in nums:
            if v:
                op0 += v.bit_count()
                max_op1 = max(max_op1, v.bit_length() - 1)

        return op0 + max_op1

