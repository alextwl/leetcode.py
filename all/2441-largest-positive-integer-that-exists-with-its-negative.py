'''
2024/05/02 daily challenge

sort + two pointer approach
'''


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        
        left, right = 0, len(nums) - 1
        
        while (left < right):
            v1, v2 = nums[left], nums[right]
            if v1 > 0 or v2 < 0:
                break

            v1 = abs(v1)
            if v1 > v2:
                left += 1
            elif v1 < v2:
                right -= 1
            else:
                return v2

        return -1

