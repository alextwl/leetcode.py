'''
intersection set approach
'''


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans1 = ans2 = 0
        for v in set(nums1) & set(nums2):
            ans1 += nums1.count(v)
            ans2 += nums2.count(v)
        return [ans1, ans2]

