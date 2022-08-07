class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = list()
        isum = 0
        for i in nums:
            isum += i
            ans.append(isum)
        return ans
