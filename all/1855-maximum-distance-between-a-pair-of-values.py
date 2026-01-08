'''
two pointers approach

both nums1 & nums2 are non-increasing,
maintain pointer of nums1 and increase it only when
it cannot pair with the last seen value of nums2.
this makes a valid i is farthest to j.
'''


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        i = 0
        ans = 0
        for j, v2 in enumerate(nums2):
            while i <= j and i < n:
                if nums1[i] <= v2:
                    ans = max(ans, j - i)
                    break
                else:
                    i += 1
        return ans

