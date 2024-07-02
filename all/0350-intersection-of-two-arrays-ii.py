class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # do counting sort
        freq1 = [0] * 1001
        freq2 = [0] * 1001
        
        for num in nums1:
            freq1[num] += 1
        for num in nums2:
            freq2[num] += 1
        
        ans = []
        for num in range(0,1001):
            ans += [num] * min(freq1[num], freq2[num])
        
        return ans


'''
2024/07/02 daily challenge

counter approach
'''


import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

