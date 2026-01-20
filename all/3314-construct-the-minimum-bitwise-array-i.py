'''
2026/01/20 daily challenge

bitwise operation approach
'''


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for v in nums:
            if v == 2:
                ans.append(-1)
            else:
                # cancel LSB if it's a single 1's bit,
                # or cancel the rightmost bit of leftmost consecutive 1's bits.
                #
                # e.g. 0b10111 -> 0b10011, so that
                #          ^          ^
                # 0b10011 OR (0b10011 + 1) == 0b10011 OR 0b10100 == 0b10111
                i = 1
                while v & i:
                    i <<= 1
                ans.append(v ^ (i >> 1))
        return ans

