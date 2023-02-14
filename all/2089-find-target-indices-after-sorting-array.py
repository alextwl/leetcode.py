'''
binary search approach
'''

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left, right = 0, len(nums)-1

        while(left <= right):
            mid = left + (right-left)//2
            if nums[mid] == target:
                left = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # the problem does not guarantee the least occurance of target.
        # if the last index's value is not target, return empty.
        if not(0 <= left < len(nums)) or nums[left] != target:
            return []

        # an occurance of target found
        ans = [left]
        # search left
        for i in range(left-1, -1, -1):
            if nums[i] != target:
                break
            ans.append(i)
        # search right
        for i in range(left+1, len(nums)):
            if nums[i] != target:
                break
            ans.append(i)
        
        ans.sort()
        return ans

