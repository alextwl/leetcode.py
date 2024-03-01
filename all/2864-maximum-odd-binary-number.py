'''
2024/03/01 daily challenge

string manipulation approach

count bits and reserve at least a "1" bit for LSB
to get odd binary number result.
'''


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeroes = len(s) - ones

        # generate leading 1's.
        # note a bit for LSB is required later
        ans = "1" * (ones - 1)

        # fill the middle 0's
        ans += "0" * zeroes

        # generate LSB for the odd binary number
        ans += "1"

        return ans

