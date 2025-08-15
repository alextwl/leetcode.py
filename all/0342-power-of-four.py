'''
2022/08/22 daily challenge
2023/10/23 daily challenge
2025/08/15 daily challenge

hint: consider any type of occurance of power of 4.
(positive vs non-positive integers)
'''


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            # there's no negative integer which is also power of 4.
            return False
        if n == 0:
            # zero is not power of 4.
            return False

        # positive number
        binstr = bin(n)[2:]  # trim '0b'

        if binstr[0] != '1':
            return False
        if '1' in binstr[1:]:
            return False
        # count how many zeroes
        if (len(binstr) - 1) % 2 != 0:
            return False
        return True


'''
oneliner for Python >= 3.10
'''


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1 and n.bit_length() & 1


'''
bitmasking approach
'''


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0

