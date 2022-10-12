'''
2022/10/12 daily challenge
'''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        sort the nums first.
        
        the biggest number of any consecutive triplet is
        always the longest sidelength of a triangle.
        
        find a valid `a + b > c` to form a valid triangle of non-zero area.
        '''
        nums.sort(reverse=True)
        
        for i in range(0, len(nums) - 2):
            # c < b + a forms a triangle of non-zero area
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        # a triangle of non-zero area is not found.
        return 0
