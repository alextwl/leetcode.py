'''
2024/03/09 daily challenge

greedy method + two pointer approach
'''


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                # greedy method: since both arrays are sorted in non-decreasing order,
                # the first common value is always the minimum.
                return nums1[i]
            
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return -1

