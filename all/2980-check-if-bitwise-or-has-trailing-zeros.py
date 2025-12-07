'''
find at least two numbers having trailing zero bits.
'''


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = 0
        for v in nums:
            if v & 1 == 0:
                cnt += 1
                if cnt == 2:
                    return True
        return False

