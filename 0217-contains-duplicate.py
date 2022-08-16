class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashmap solution, may exceed time limit.
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1

        return False

        # faster oneliner benefits from python
        return len(nums) > len(set(nums))
