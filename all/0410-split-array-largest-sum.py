'''
binary search approach

search the minimal largest sum of subarrays.
'''


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def validate(target):
            # validate if we can form k subarrays with largest target sum
            g = 0
            current_sum = 0
            for v in nums:
                if v > target:
                    # if target is greater than any element, we cannot split it into valid subarrays
                    return False
                # try to add v to the current group
                if (next_sum := current_sum + v) <= target:
                    current_sum = next_sum
                else:
                    current_sum = v
                    g += 1
                    if g == k:
                        return False
            return True
        
        l, r = 0, sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

