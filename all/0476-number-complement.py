'''
2024/08/22 daily challenge

bitwise and & shift approach
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

