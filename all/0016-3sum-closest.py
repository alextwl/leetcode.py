'''
leetcode 75 lv2 day 14

simplified ver, AC with new testcase

focus on minimizing the difference between 3Sum & target,
ignore extra effort to optimize it.

Runtime 735 ms Beats 93.65%
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort the nums in advance in order to get the search faster.
        nums.sort()

        minDiff = float('inf')
        ans = float('inf')

        '''
        reduce the problem by fixing x.
        3Sum = nums[x] + nums[y] + nums[z]

        while searching the array, the index sequence of 3 numbers is:
        [..., x, ..., y, ..., z, ...]
        '''
        for x in range(0, len(nums) - 2):
            '''
            fix x and search y & z.
            `len(nums) - 2` is to make sure we have enough candidates of y & z.
            '''
            num_x = nums[x]
            y = x+1
            z = len(nums) - 1
            # two pointer loop (similar to binary search)
            while(y < z):
                threeSum = num_x + nums[y] + nums[z]
                # get the minimum difference
                diff = abs(threeSum - target)
                if diff < minDiff:
                    minDiff = diff
                    ans = threeSum
                # try to approach the target by adjusting pointers
                if threeSum > target:
                    z -= 1
                elif threeSum < target:
                    y += 1
                else:
                    # exact hit
                    return target

        return ans


'''
2022/10/08 daily challenge

Similar to problem 15: 3Sum.

time=O(n**2) approach.

The key is to simplify the solution from problem 15
and reduce the instructions in all loops,
or we'll exceed the time limit.

** Update: it's no longer AC in 2023 with new testcase
nums=[2,3,8,9,10] target=16
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort the nums in advance in order to get the search faster.
        nums.sort()
        
        ans = float('inf')
        
        '''
        reduce the problem by fixing x.
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
                
                if threesum < target:
                    # we need bigger y.
                    y += 1
                elif threesum > target:
                    # we need smaller z.
                    z -= 1
                else:
                    # exact target hits.
                    return target
                
                '''
                the while-loop will always result in a closet 3Sum to the target in the end.
                do not compare 3Sum & target in the while-loop or get TLE.
                '''

            if abs(target - threesum) < abs(target - ans):
                '''
                compare the absolute difference between the 3Sum and target,
                and update the closest 3Sum to the target.
                '''
                ans = threesum

        return ans

