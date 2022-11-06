class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Kadane's algorithm
        https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
        '''
        # at least one element in the nums is guaranteed in the constraints
        # thus the following sums default to nums[0].
        best_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(0, current_sum) + num  # it restarts subarray if current sum became negative.
            best_sum = max(best_sum, current_sum)
        
        return best_sum
