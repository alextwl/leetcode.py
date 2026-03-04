'''
counting approach
'''


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odds = sum(v & 1 for v in nums)
        evens = len(nums) - odds
        # as we've known counts of odds & evens,
        # generate the resulting array directly, no need to sort.
        return [0] * evens + [1] * odds

