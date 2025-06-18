'''
2024/02/01 daily challenge
2025/06/18 daily challenge

greedy method approach

sort & group each 3 consecutive values
'''


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        
        it = iter(nums)
        for v1 in it:
            v2 = next(it)
            v3 = next(it)
            
            if v3 - v1 > k:
                return []
            
            ans.append([v1, v2, v3])

        return ans


'''
python>=3.12 ver
'''


import itertools


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        # use a supplemental function originally from more-itertools.
        for v1, v2, v3 in itertools.batched(nums, 3):
            if v3 - v1 > k:
                return []
            ans.append([v1, v2, v3])
        return ans

