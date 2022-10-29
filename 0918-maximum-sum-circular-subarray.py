'''
next array approach

learnt from official solution 1

1. run Kadane's algorithm once for nums[]
2. evaluate all subarrays' sum with circular setup and compare it with previous answer.

time=O(n), space=O(n)
'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        anyway let's run Kadane's for the non-circular nums[] first.
        '''
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(0, current_sum) + num  # restart subarray if sum became negative.
            max_sum = max(max_sum, current_sum)
        
        '''
        and evaluate all subarray's sum with circular setup
        
        1. calculate from sum(nums[-1:]) ... to sum(nums[0:]) in nums[]'s reverse order.
        '''
        n = len(nums)
        rsums = [None] * n
        # sum up nums[] backward.
        rsums[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            rsums[i] = rsums[i+1] + nums[i]
        
        '''
        2. calculate the max sum of right-part subarrays
        the right-part subarray must start from rsums[-1]
        in order to form a circular with left-part,
        so we cannot apply Kadane's here but just sum up & maximize it.
        '''
        max_rsums = [None] * n
        max_rsums[-1] = rsums[-1]
        for i in range(n-2, -1, -1):
            max_rsums[i] = max(max_rsums[i+1], rsums[i])
        
        '''
        3. calculate the max sum of left-part,
        combine it with right-part to form a circular subarray,
        and compare the max sum including the non-circular Kadane's result in the beginning.
        '''
        current_sum = 0  # reset and accumulate from the left.
        for i in range(0, n-2):
            '''
            a circular subarray's length is not longer than len(nums) - 1
            because if len(circular subarray) == len(nums) it's not necessarily a circular,
            so we always keep a gap between left & right parts of subarray.
            (that's why range(0, n-2) & max_rsums[i+2])
            '''
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum + max_rsums[i+2])
        
        return max_sum


'''
3-time kadane's approach (Kadane's sign variant)

learnt from official solution 3 (see the derived sigma equation)

the explanation from official sol is not intuitive,
but the main idea is using kadane's to
find the *minimum* sum from nums[1:] & nums[:-1],
add it to sum(nums[]) (equal to sum(nums[]) subtracted the excluded part.)

it seems the actual runtime does not beat next array method...
'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(g):
            '''
            :param g: an iterable instance of numbers
            :type g: list_iterator or generator
            '''
            max_sum = cur_sum = next(g)  # do *not* initialize it to None or it raises exception when calling max(None).
            for num in g:
                cur_sum = num + max(cur_sum, 0)  # restart subarray if cur_sum was negative.
                max_sum = max(max_sum, cur_sum)
            
            return max_sum
        
        if len(nums) == 1:
            # just return the first element, no need to run Kadane's.
            return nums[0]
        
        sumA = sum(nums)
        
        s1 = kadane(iter(nums))  # for the case of the subarray == nums[].
        s2 = sumA + kadane(-nums[i] for i in range(1, len(nums)))  # == kadane(nums[j:] + nums[i:]), 2nd-part without first element.
        s3 = sumA + kadane(-nums[i] for i in range(0, len(nums)-1))  # == kadane(nums[j:] + nums[i:]), 2nd-part without last element.
        
        return max(s1, s2, s3)
