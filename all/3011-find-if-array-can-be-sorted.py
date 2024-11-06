'''
2024/11/06 daily challenge

the problem asks for swapping any two **adjacent** elements
if they have the same bit count, so we need to group the array
by bit count and sort each group respectively.
'''


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        prev = nums[0].bit_count()
        i = 0
        parts = []

        for j, v in enumerate(nums):
            if (bc := v.bit_count()) != prev:
                parts.sort()
                for w in parts:
                    if w != nums_sorted[i]:
                        return False
                    i += 1
                parts = []

            parts.append(v)
            prev = bc

        return True


'''
bubble sort ver

it works because an element cannot be swapped to the sorted position
if elements between them had different bit counts.
'''


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    if nums[j].bit_count() != nums[j + 1].bit_count():
                        return False
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return True


'''
split array into groups (segments) by set bits
and check min/max integrity.
'''


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_bits = nums[0].bit_count()
        prev_max = float('-inf')
        curr_min = curr_max = nums[0]
        
        for v in nums:
            if v.bit_count() != prev_bits:
                if prev_max > curr_min:
                    return False
                prev_max = curr_max
                # start new group
                prev_bits = v.bit_count()
                curr_min = curr_max = v
            else:
                curr_min = min(curr_min, v)
                curr_max = max(curr_max, v)

        # check the last group
        if prev_max > curr_min:
            return False

        return True

