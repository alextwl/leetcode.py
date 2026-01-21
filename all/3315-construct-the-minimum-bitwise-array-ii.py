'''
2026/01/21 daily challenge

bitwise operations approach

same to problem 3314.
'''


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for v in nums:
            if v == 2:
                ans.append(-1)
            else:
                i = 1
                while v & i:
                    i <<= 1
                ans.append(v ^ (i >> 1))
        return ans

