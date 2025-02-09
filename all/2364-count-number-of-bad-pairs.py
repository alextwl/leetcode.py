'''
2025/02/09 daily challenge

hash + equation rearrangement approach

the equation of a good pair:

(1) j - i = nums[j] - nums[i]
(2) j - nums[j] = i - nums[i]

we can count diffs between each index and its value,
and calculate the number of bad pairs from good pairs.
'''


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bads = 0
        diff_freq = dict()

        for i, v in enumerate(nums):
            diff = i - v
            goods = diff_freq.get(diff, 0)
            # there are i pairs from (0, i) to (i-1, i),
            # subtract good pairs (previous pairs with same diff) from i pairs
            # and then we get the number of bad pairs.
            bads += i - goods
            # accumulate the frequency of current diff
            diff_freq[diff] = goods + 1

        return bads

