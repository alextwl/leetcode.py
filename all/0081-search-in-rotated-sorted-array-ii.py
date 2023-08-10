'''
2023/08/10 daily challenge

onepass binary search approach

learnt from official solution
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        left, right = 0, n-1
        
        while(left <= right):
            mid = left + (right - left) // 2
            v = nums[mid]
            
            if v == target:
                return True
            
            if v == nums[left]:
                # shrink the search space
                left += 1
                continue
            
            isPivotInLeft = nums[left] <= v
            isTargetInLeft = nums[left] <= target
            
            if isPivotInLeft ^ isTargetInLeft:
                '''
                pivot and target exist in different sides.
                '''
                if isPivotInLeft:
                    # pivot in left, target in right
                    left = mid + 1
                else:
                    # pivot in right, target in left
                    right = mid - 1
            else:
                '''
                pivot and target exist in same side.
                just run binary search in the current space.
                '''
                if v < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
