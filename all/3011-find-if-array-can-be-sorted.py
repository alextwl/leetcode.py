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

