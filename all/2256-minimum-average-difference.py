'''
2022/12/04 daily challenge

prefix sum approach
'''

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            # i=0 is the only index, so return 0.
            return 0
        
        i = 0
        leftsum, rightsum = 0, sum(nums)  # prefix sum & suffix sum
        leftcnt, rightcnt = 1, n-1
        minAvgDiff, ansIndex = float('inf'), -1
        
        for i, val in enumerate(nums):
            leftsum += val
            rightsum -= val

            if rightcnt:
                diff = abs(leftsum//leftcnt - rightsum//rightcnt)
            else:
                diff = leftsum//leftcnt
            
            if diff < minAvgDiff:
                # memorize the smallest index with the minimum average difference
                minAvgDiff = diff
                ansIndex = i

            leftcnt += 1
            rightcnt -= 1
        
        return ansIndex

