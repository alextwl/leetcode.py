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

