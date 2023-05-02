'''
2023/05/02 daily challenge
'''

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for x in nums:
            if x < 0:
                s = -s
            elif not x:
                return 0
        return s

