'''
2023/11/25 daily challenge

prefix sum approach

derivation:

abs(a-b) = max(a,b) - min(a,b)

result[i] = (nums[i] - nums[0]) + ... + (nums[i] - nums[i-1]) + \
            (nums[i+1] - nums[i]) + ... + (nums[-1] - nums[i])

          = (nums[i] * i - (nums[0] + ... + nums[i-1])) + \
            ((nums[i+1] + ... + nums[-1]) - nums[i] * (len(nums)-i-1))
'''

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        psum = 0  # prefix sum
        ssum = sum(nums)  # suffix sum
        
        ans = []
        for i, v in enumerate(nums):
            # prepare suffix sum for this round
            ssum -= v
            
            # evaluate the answer
            r = ((v * i) - psum) + (ssum - (v * (n - i - 1)))
            ans.append(r)
            
            # prepare prefix sum for next round
            psum += v

        return ans

