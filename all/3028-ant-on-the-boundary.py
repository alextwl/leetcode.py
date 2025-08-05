'''
simulation approach

position 0 is the boundary, we count only when ant returns here.
'''


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for v in nums:
            curr += v
            if curr == 0:
                ans += 1
        return ans

