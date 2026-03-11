'''
2024/08/22 daily challenge

bitwise and & shift approach

same to problem 1009.
'''


class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        pos = 0

        while(num):
            if num & 1 == 0:
                ans |= 1 << pos
            pos += 1
            num >>= 1

        return ans


'''
oneliner ver
'''


class Solution:
    def findComplement(self, num: int) -> int:
        return sum(1 << i for i, c in enumerate(reversed(bin(num)[2:])) if c == '0')


'''
mathematical oneliner ver

subtract num from an all-ones mask to get the answer.
'''


class Solution:
    def findComplement(self, num: int) -> int:
        return (1 << (len(bin(num)) - 2)) - 1 - num

