'''
intuitive approach learnt from 
https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).

btw there's a more pythonic solution:
https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hint 2: sort the nums in advance in order to get the search faster.
        nums.sort()
        
        ans = []
        
        '''
        Hint 1: reduce the problem by fixing the first number.
        3Sum = nums[x] + nums[y] + nums[z]
        
        while searching the array, the index sequence of 3 numbers is:
        [..., x, ..., y, ..., z, ...]
        '''
        for x in range(0, len(nums) - 2):
            '''
            fix x and search y & z.
            `len(nums) - 2` is to make sure we have enough candidates of y & z.
            '''
            
            if x > 0 and nums[x] == nums[x-1]:
                '''
                eliminate duplicate x in advance.
                since the array was sorted,
                we can comfortably bypass x if nums[x] equals to the previous one.
                '''
                continue
            
            '''
            search y starting from the next number of x.
            search z starting from the end of array and recurse reversely.
            '''
            y = x + 1
            z = len(nums) - 1
            
            while y < z:
                threesum = nums[x] + nums[y] + nums[z]
                
                if threesum < 0:
                    '''
                    the array is sorted, if 3Sum < 0,
                    that means we need bigger nums[y] to seek 3Sum==0.
                    '''
                    y += 1
                elif threesum > 0:
                    '''
                    if 3Sum > 0,
                    that means we need smaller nums[z] to seek 3Sum==0.
                    '''
                    z -= 1
                else:
                    # 3Sum == 0 found.
                    ans.append([nums[x], nums[y], nums[z]])
                    
                    '''
                    eliminate duplicate y & z in advance.
                    the next y is y+1 and the next z is z-1.
                    '''
                    while y < z and nums[y] == nums[y+1]:
                        # eliminate duplicate y.
                        y += 1
                    while y < z and nums[z] == nums[z-1]:
                        # eliminate duplicate z.
                        z -= 1
                    
                    # find next y & z.
                    y += 1
                    z -= 1
        return ans
