'''
2025/10/31 daily challenge

counter approach
'''


import collections


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [k for k, _ in collections.Counter(nums).most_common(2)]


'''
XOR approach
'''


import functools


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        # XOR all values in nums
        xorval = functools.reduce(int.__xor__, nums)
        # cancel all values in [0:n)
        xorval = functools.reduce(int.__xor__, range(n), xorval)
        # rightmost (lowest) differing bit between v1 and v2
        rdb = xorval & -xorval

        v1 = v2 = 0
        for x in nums:
            if x & rdb:
                v1 ^= x
            else:
                v2 ^= x
        # here the final answers are temporarily canceled,
        # but the remaining parts are also categorized into v1 & v2 by
        # the rightmost differing bit.
        #
        # non-duplicate parts in nums will be canceled by range(n),
        # and we will get the final answer.
        for y in range(n):
            if y & rdb:
                v1 ^= y
            else:
                v2 ^= y
        return [v1, v2]

