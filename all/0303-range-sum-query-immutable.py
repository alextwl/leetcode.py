'''
prefix sum approach

sumRange(i, j) = prefixSum(j) - (prefixSum(i-1) if i > 0 else 0)
'''

class NumArray:

    def __init__(self, nums: List[int]):
        # prefix sum array
        self.dp = []
        
        psum = 0
        for i, val in enumerate(nums):
            psum += val
            self.dp.append(psum)

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right] - (self.dp[left-1] if left > 0 else 0)

