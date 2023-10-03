'''
2023/10/03 daily challenge

math approach

if there're [1,1,1,1] numbers, the pairs are:
(0,1), (0,2), (0,3)
(1,2), (1,3)
(2,3)

so we can assign n = nums.count(1) - 1 = 3

                   n * (n + 1)
the sum of pairs = -----------
                        2
'''

import collections

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return sum((n * (n-1)) >> 1 for n in counter.values())


'''
time=O(n) ver
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        counter = dict()
        
        for v in nums:
            pairs += counter.setdefault(v, 0)
            counter[v] += 1
        
        return pairs

