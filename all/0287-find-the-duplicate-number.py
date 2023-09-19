'''
2023/09/19 daily challenge

cycle detection approach

similar to problem 142 Linked List Cycle II
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            # impossible to find duplicate
            return -1

        # find the cycle first
        slow = nums[0]
        fast = nums[nums[0]]

        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]

        # so the slow & fast pointers meet in the cycle.

        # find the entry of cycle
        slow2 = 0
        while(slow != slow2):
            slow = nums[slow]
            slow2 = nums[slow2]

        # the entry point (== the duplicate number) found
        return slow

