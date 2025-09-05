'''
2025/09/05 daily challenge

enumeration + math approach

learnt from official editorial:
https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/editorial/#approach-enumeration
'''


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            num1 -= num2
            if num1 < k:
                # cannot form num1 by sum of powers of 2
                # because even the smallest power (2**0) * k > num1.
                return -1
            if k >= num1.bit_count():
                # remainings of num1 can be formed by sum of 2**i.
                # for extra operations of k, combine two 2**(i-1) to 2**i.
                return k
        return -1

