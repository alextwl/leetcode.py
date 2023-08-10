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
                '''
                we cannot decide whether mid exists in the 1st or 2nd side,
                we can only shrink the search space from left
                and skip to next round.
                '''
                left += 1
                continue

            isMidInLeft = nums[left] <= v
            isTargetInLeft = nums[left] <= target
            
            if isMidInLeft ^ isTargetInLeft:
                '''
                mid and target exist in different sides.
                '''
                if isMidInLeft:
                    # pivot in left, target in right
                    left = mid + 1
                else:
                    # pivot in right, target in left
                    right = mid - 1
            else:
                '''
                mid and target exist in same side.
                just run binary search in the current space.
                '''
                if v < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
