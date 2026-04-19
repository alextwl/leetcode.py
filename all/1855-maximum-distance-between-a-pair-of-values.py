'''
2026/04/19 daily challenge

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


'''
binary search approach
'''


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = 0
        # left pointer is preserved after each binary search
        # because all values prior to nums1[left]
        # are greater than the current & next nums2[j].
        left = 0
        for j, v in enumerate(nums2):
            right = min(j, n - 1)
            while left <= right:
                mid = (left + right) // 2
                if nums1[mid] > v:
                    left = mid + 1
                else:
                    ans = max(ans, j - mid)
                    right = mid - 1
        return ans

