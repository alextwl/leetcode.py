class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        calculate Sigma(length of nums) and substract each element in the nums
        final remaining part is the missing number

        time=O(n), space=O(1)
        '''
        n = len(nums)
        remaining = int(n * (n+1) / 2)  # do not return float ans
        for num in nums:
            remaining -= num
        
        return remaining


'''
2024/02/20 daily challenge

exclusive or approach

doing XOR the same number twice will cancel it,
so the remaining value that wasn't cancelled is the answer.
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0

        # XOR [0, n]
        for i in range(1, len(nums)+1):
            ans ^= i
        # XOR nums
        for i in nums:
            ans ^= i
        
        return ans

