'''
2024/03/25 daily challenge

treat the array as a linked list
with input modification to satisfy space=O(1) requirement.

e.g. nums[i] -> nums[nums[i]] and negatify it as visited.
'''


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = list()
        # note the index range is 0..len(nums)-1
        # but the value range is 1..len(nums).
        for i in range(len(nums)):
            j = abs(nums[i]) - 1  # index of nums[original nums[i] - 1]
            if nums[j] < 0:
                # if the value was negative it means it's already visited.
                ans.append(j + 1)  # cycle found == a duplicate
            else:
                nums[j] *= -1  # use negative number to indicate it's visited.

        return ans

