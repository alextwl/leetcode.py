'''
2025/02/12 daily challenge

hashmap approach

maintain the maximum value of nums by sum of digits as its key.
'''


import collections


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dsum_max = dict()  # key=sum of digits, value=max value of nums

        max_val = -1  # init with no answer val=-1
        for v in nums:
            dsum = sum(int(dig) for dig in str(v))
            if dsum in dsum_max:
                max_val = max(max_val, dsum_max[dsum] + v)
            dsum_max[dsum] = max(dsum_max.get(dsum, 0), v)

        return max_val

