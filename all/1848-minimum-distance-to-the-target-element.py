'''
2026/04/13 daily challenge

linear search approach (order by distance to start)
'''


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)

        if nums[start] == target:
            return 0
        
        left, right = start - 1, start + 1
        while left >= 0 or right < n:
            if left >= 0:
                if nums[left] == target:
                    return start - left
                left -= 1
            if right < n:
                if nums[right] == target:
                    return right - start
                right += 1

        # undefined: target not found
        return -1

