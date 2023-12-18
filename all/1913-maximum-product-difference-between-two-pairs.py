'''
2023/12/18 daily challenge

sorting approach
'''


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


'''
find the largest two numbers and the smallest two numbers.

time=O(n)
'''


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = 10001
        
        for v in nums:
            if v >= max1:
                max2, max1 = max1, v
            elif v > max2:
                max2 = v
            
            if v <= min1:
                min1, min2 = v, min1
            elif v < min2:
                min2 = v
        
        return (max1 * max2) - (min1 * min2)

