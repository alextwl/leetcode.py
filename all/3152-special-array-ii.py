'''
2024/12/09 daily challenge

prefix sum (count of pairs of different parity) approach

build a special prefix array that counts the iterated pairs of its adjacent elements
contains two numbers with different parity.
'''


import itertools


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        count = 0
        prefix = [0]
        for a, b in itertools.pairwise(nums):
            if (a ^ b) & 1:
                count += 1
            prefix.append(count)
        
        ans = []
        for i, j in queries:
            ans.append(j - i == prefix[j] - prefix[i])
        return ans

