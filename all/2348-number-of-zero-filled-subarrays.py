'''
2023/03/21 daily challenge
'''

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        repeat_zeroes = 0
        ans = 0

        for v in nums:
            if v == 0:
                repeat_zeroes += 1
            elif repeat_zeroes:
                ans += (repeat_zeroes * (repeat_zeroes + 1)) >> 1
                repeat_zeroes = 0
        
        # increment the last zero subarray if available
        ans += (repeat_zeroes * (repeat_zeroes + 1)) >> 1

        return ans

